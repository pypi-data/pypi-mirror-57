# -*- coding: utf-8 -*-
# Copyright (c) 2015, inaz2
# All rights reserved. BSD 3-Clause "New" or "Revised" License
# https://github.com/inaz2/proxy2
# Copyright (c) 2019, KeyChest Ltd  support@keychest.net
# updated for Python3, logging replaced with async logging using logbook, smaller changes throughout
import logging
import sys
import socket
import ssl
import select
import http.client as httplib
from urllib.parse import urlsplit
from urllib.parse import parse_qsl as urllib_qsl
from urllib.parse import urlparse as urlparse

import threading
import gzip
import zlib
import json
import re
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from io import StringIO
from html.parser import HTMLParser

from keychestamp.acme_log import AcmeLog
from keychestamp.ampconfig import AmpConfig

COLOR_ON = False


def with_color(c, s):
    if COLOR_ON:
        return "\x1b[%dm%s\x1b[0m" % (c, s)
    else:
        return s


class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    address_family = socket.AF_INET6
    daemon_threads = True

    def handle_error(self, request, client_address):
        # suppress socket/ssl related errors
        cls, e = sys.exc_info()[:2]
        if cls is socket.error or cls is ssl.SSLError:
            pass
        else:
            return HTTPServer.handle_error(self, request, client_address)


class ProxyRequestHandler(BaseHTTPRequestHandler):

    timeout = AmpConfig.api_timeout
    lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        self.tls = threading.local()
        self.tls.conns = {}
        self.connection = None
        self.rfile = None
        self.wfile = None
        self.close_connection = None

        BaseHTTPRequestHandler.__init__(self, *args, **kwargs)

    def log_error(self, _format, *args):
        # suppress "Request timed out: timeout('timed out',)"
        if isinstance(args[0], socket.timeout):
            return
        self.log_message(_format, *args)

    def do_CONNECT(self):
        if AmpConfig.cert_ready():
            self.connect_intercept()
        else:
            logging.error("Proxy key or certificate are not ready")
            self.connect_relay()

    def connect_intercept(self):
        hostname = self.path.split(':')[0]

        with self.lock:
            AmpConfig.ensure_name_cert(hostname)

        message = "%s %d %s\r\n\r\n" % (self.protocol_version, 200, 'Connection Established')

        self.wfile.write(message.encode())

        self.connection = ssl.wrap_socket(self.connection, keyfile=AmpConfig.cert_key, certfile=AmpConfig.get_cert_path(hostname),
                                          server_side=True)
        self.rfile = self.connection.makefile("rb", self.rbufsize)
        self.wfile = self.connection.makefile("wb", self.wbufsize)

        conntype = self.headers.get('Proxy-Connection', '')
        if self.protocol_version == "HTTP/1.1" and conntype.lower() != 'close':
            self.close_connection = 0
        else:
            self.close_connection = 1

    def connect_relay(self):
        address = self.path.split(':', 1)
        address[1] = int(address[1]) or 443
        try:
            s = socket.create_connection(address, timeout=self.timeout)
        except Exception as e:
            logging.info("Relay error", cause=str(e))
            self.send_error(502)
            return
        self.send_response(200, 'Connection Established')
        self.end_headers()

        conns = [self.connection, s]
        self.close_connection = 0
        while not self.close_connection:
            rlist, wlist, xlist = select.select(conns, [], conns, self.timeout)
            if xlist or not rlist:
                break
            for r in rlist:
                other = conns[1] if r is conns[0] else conns[0]
                data = r.recv(8192)
                if not data:
                    self.close_connection = 1
                    break
                other.sendall(data)

    def do_GET(self):
        if self.path == 'http://amp.keychest.net/':
            self.send_ca_cert()
            return

        req = self
        content_length = int(req.headers.get('Content-Length', 0))
        req_body = self.rfile.read(content_length) if content_length else None

        # req.path = "http://127.0.0.1:6443" + req.path
        if req.path[0] == '/':
            if isinstance(self.connection, ssl.SSLSocket):
                req.path = "https://%s%s" % (req.headers['Host'], req.path)
            else:
                req.path = "http://%s%s" % (req.headers['Host'], req.path)

        # noinspection PyNoneFunctionAssignment
        req_body_modified = self.request_handler(req, req_body)
        if req_body_modified is False:
            self.send_error(403)
            return
        elif req_body_modified is not None:
            req_body = req_body_modified
            # noinspection PyTypeChecker
            req.headers['Content-length'] = str(len(req_body))

        req.headers['X-Forwarded-For'] = req.client_address[0]

        u = urlparse(req.path)
        scheme, netloc, path = u.scheme, u.netloc, (u.path + '?' + u.query if u.query else u.path)
        assert scheme in ('http', 'https')
        if netloc:
            req.headers['Host'] = netloc
        setattr(req, 'headers', self.filter_headers(req.headers))

        origin = (scheme, netloc)
        res_body = None
        res_code = None
        res = None
        try:
            if origin not in self.tls.conns:
                if scheme == 'https':
                    if (ssl.get_default_verify_paths().cafile is None) and (ssl.get_default_verify_paths().capath is None):
                        logging.error("No root CA bundle configured for Python")
                        # noinspection PyProtectedMember
                        context = ssl._create_unverified_context()
                    else:
                        context = ssl.create_default_context()
                    self.tls.conns[origin] = httplib.HTTPSConnection(netloc, timeout=self.timeout, context=context)
                else:
                    self.tls.conns[origin] = httplib.HTTPConnection(netloc, timeout=self.timeout)
            conn = self.tls.conns[origin]
            conn.request(self.command, path, req_body, dict(req.headers))
            res = conn.getresponse()
            res_code = res.code

            version_table = {10: 'HTTP/1.0', 11: 'HTTP/1.1'}
            setattr(res, 'headers', res.msg)
            setattr(res, 'response_version', version_table[res.version])

            # support streaming
            if ('Content-Length' not in res.headers) and ('no-store' in res.getheader('Cache-Control', '')):
                self.response_handler(req, req_body, res, '')
                setattr(res, 'headers', self.filter_headers(res.headers))
                self.relay_streaming(res)
                with self.lock:
                    self.save_handler(req, req_body, res, '')
                return

            res_body = res.read()
        except Exception as e:
            logging.info("Get request error", cause=str(e))
            if origin in self.tls.conns:
                del self.tls.conns[origin]
            self.send_error(502)
            return
        finally:
            res_hdrs = None
            if res and res.headers:
                res_hdrs = res.headers
            AcmeLog.repeater(req.headers, res_code, req.path, req_body, res_body, res_hdrs)

        content_encoding = res.getheader('Content-Encoding', 'identity')
        res_body_plain = self.decode_content_body(res_body, content_encoding)

        # noinspection PyNoneFunctionAssignment
        res_body_modified = self.response_handler(req, req_body, res, res_body_plain)
        if res_body_modified is False:
            self.send_error(403)
            return
        elif res_body_modified is not None:
            res_body_plain = res_body_modified
            res_body = self.encode_content_body(res_body_plain, content_encoding)
            res.headers['Content-Length'] = str(len(res_body))

        setattr(res, 'headers', self.filter_headers(res.headers))

        message = "%s %d %s\r\n" % (self.protocol_version, res.status, res.reason)
        self.wfile.write(message.encode())
        for line in res.getheaders():
            self.send_header(line[0], line[1])
        self.end_headers()
        if res_body and len(res_body) > 0:
            self.wfile.write(res_body)
        self.wfile.flush()

        with self.lock:
            self.save_handler(req, req_body, res, res_body_plain)

    def relay_streaming(self, res):
        message = "%s %d %s\r\n" % (self.protocol_version, res.status, res.reason)
        self.wfile.write(message.encode())
        for line in res.getheaders():
            self.send_header(line[0], line[1])
        self.end_headers()
        try:
            while True:
                chunk = res.read(8192)
                if not chunk:
                    break
                self.wfile.write(chunk)
            self.wfile.flush()
        except socket.error:
            # connection closed by client
            pass

    do_HEAD = do_GET
    do_POST = do_GET
    do_PUT = do_GET
    do_DELETE = do_GET
    do_OPTIONS = do_GET

    @staticmethod
    def filter_headers(headers):
        # http://tools.ietf.org/html/rfc2616#section-13.5.1
        hop_by_hop = ('connection', 'keep-alive', 'proxy-authenticate', 'proxy-authorization', 'te', 'trailers',
                      'transfer-encoding', 'upgrade')
        for k in hop_by_hop:
            del headers[k]

        # accept only supported encodings
        if 'Accept-Encoding' in headers:
            ae = headers['Accept-Encoding']
            filtered_encodings = [x for x in re.split(r',\s*', ae) if x in ('identity', 'gzip', 'x-gzip', 'deflate')]
            headers['Accept-Encoding'] = ', '.join(filtered_encodings)

        return headers

    @staticmethod
    def encode_content_body(text, encoding):
        if encoding == 'identity':
            data = text
        elif encoding in ('gzip', 'x-gzip'):
            io = StringIO()
            with gzip.GzipFile(fileobj=io, mode='wb') as f:
                f.write(text)
            data = io.getvalue()
        elif encoding == 'deflate':
            data = zlib.compress(text)
        else:
            raise Exception("Unknown Content-Encoding: %s" % encoding)
        return data

    @staticmethod
    def decode_content_body(data, encoding):
        if encoding == 'identity':
            text = data
        elif encoding in ('gzip', 'x-gzip'):
            io = StringIO(data)
            with gzip.GzipFile(fileobj=io) as f:
                text = f.read()
        elif encoding == 'deflate':
            try:
                text = zlib.decompress(data)
            except zlib.error:
                text = zlib.decompress(data, -zlib.MAX_WBITS)
        else:
            raise Exception("Unknown Content-Encoding: %s" % encoding)
        return text

    def send_ca_cert(self):
        with open(AmpConfig.ca_cert, 'rb') as f:
            data = f.read()

        first_line = "%s %d %s\r\n" % (self.protocol_version, 200, 'OK')
        self.wfile.write(first_line.encode())
        self.send_header('Content-Type', 'application/x-x509-ca-cert')
        self.send_header('Content-Length', len(data))
        self.send_header('Connection', 'close')
        self.end_headers()
        self.wfile.write(data)

    @staticmethod
    def print_info(req, req_body, res, res_body):
        def parse_qsl(s):
            return '\n'.join("%-20s %s" % (k, v) for k, v in urllib_qsl(s, keep_blank_values=True))

        req_header_text = "%s %s %s\n%s" % (req.command, req.path, req.request_version, req.headers)
        res_header_text = "%s %d %s\n%s" % (res.response_version, res.status, res.reason, res.headers)

        logging.debug(with_color(33, req_header_text))

        u = urlsplit(req.path)
        if u.query:
            query_text = parse_qsl(u.query)
            logging.debug(with_color(32, "==== QUERY PARAMETERS ====\n%s\n" % query_text))

        cookie = req.headers.get('Cookie', '')
        if cookie:
            cookie = parse_qsl(re.sub(r';\s*', '&', cookie))
            logging.debug(with_color(32, "==== COOKIE ====\n%s\n" % cookie))

        auth = req.headers.get('Authorization', '')
        if auth.lower().startswith('basic'):
            token = auth.split()[1].decode('base64')
            logging.debug(with_color(31, "==== BASIC AUTH ====\n%s\n" % token))

        if req_body is not None:
            req_body_text = None
            content_type = req.headers.get('Content-Type', '')

            if content_type.startswith('application/x-www-form-urlencoded'):
                req_body_text = parse_qsl(req_body)
            elif content_type.startswith('application/json'):
                try:
                    json_obj = json.loads(req_body)
                    json_str = json.dumps(json_obj, indent=2)
                    if json_str.count('\n') < 50:
                        req_body_text = json_str
                    else:
                        lines = json_str.splitlines()
                        req_body_text = "%s\n(%d lines)" % ('\n'.join(lines[:50]), len(lines))
                except ValueError:
                    req_body_text = req_body
            elif len(req_body) < 1024:
                req_body_text = req_body

            if req_body_text:
                logging.debug(with_color(32, "==== REQUEST BODY ====\n%s\n" % req_body_text))

        logging.debug(with_color(36, res_header_text))

        cookies = res.getheader('Set-Cookie')
        if cookies:
            cookies = '\n'.join(cookies)
            logging.debug(with_color(31, "==== SET-COOKIE ====\n%s\n" % cookies))

        if res_body is not None:
            res_body_text = None
            content_type = res.getheader('Content-Type', "")

            if content_type.startswith('application/json'):
                try:
                    json_obj = json.loads(res_body)
                    json_str = json.dumps(json_obj, indent=2)
                    if json_str.count('\n') < 50:
                        res_body_text = json_str
                    else:
                        lines = json_str.splitlines()
                        res_body_text = "%s\n(%d lines)" % ('\n'.join(lines[:50]), len(lines))
                except ValueError:
                    res_body_text = res_body
            elif content_type.startswith('text/html'):
                m = re.search(r'<title[^>]*>\s*([^<]+?)\s*</title>', res_body.decode(), re.I)
                if m:
                    # noinspection PyUnusedLocal
                    h = HTMLParser()
                    # print(with_color(32, "==== HTML TITLE ====\n%s\n" % h.unescape(m.group(1).decode('utf-8'))))
            elif content_type.startswith('text/') and len(res_body) < 1024:
                res_body_text = res_body.decode()

            if res_body_text:
                logging.debug(with_color(32, "==== RESPONSE BODY ====\n%s\n" % res_body_text))

    def request_handler(self, req, req_body):
        pass

    def response_handler(self, req, req_body, res, res_body):
        pass

    def save_handler(self, req, req_body, res, res_body):
        self.print_info(req, req_body, res, res_body)


# noinspection PyPep8Naming
def test(HandlerClass=ProxyRequestHandler, ServerClass=ThreadingHTTPServer, protocol="HTTP/1.1"):
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8080
    server_address = ('127.0.0.1', port)

    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)

    sa = httpd.socket.getsockname()
    logging.info("Serving HTTP Proxy on", iface=sa[0], port=sa[1])
    httpd.serve_forever()


if __name__ == '__main__':
    logging.debug("keychestamp proxy")
    test()
