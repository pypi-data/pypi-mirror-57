#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module:
***
"""
#  Copyright (c) KeyChest Ltd, 2019. File provided under the license as described in the "LICENSE" file
#   included with this project. A copy of the license is also available from https://gitlab.com/keychest,
#   when you select the relevant project or you can request it at support@keychest.net.
#
#   This file is owned exclusively by KeyChest Ltd. Unauthorized copying of this file, via any medium is
#    strictly prohibited
#
import errno
import getopt
import logging
import multiprocessing
import os
import socket
import sys
import time
from subprocess import Popen, PIPE

from keychestamp.queue_handler import QueueHandler
from keychestamp.version import proxy_version

__copyright__ = 'KeyChest Ltd'
__email__ = 'support@keychest.net'
__status__ = 'Development'


class AmpConfig(object):
    """
    A static class with the configuration of the process.
    """

    port = 8443
    address = "0.0.0.0"
    api_logging = True
    file_logging = None
    log_level = logging.INFO
    api_timeout = 5
    ch = None
    working_dir = None
    temp_ca = None
    config_dir = '/etc/keychestamp'
    main_stop = multiprocessing.Event()

    ca_dir = './ca'
    ca_key = ca_dir + '/private/ca.key'
    ca_cert = ca_dir + '/certs/ca.crt'
    cert_key = ca_dir + '/private/cert.key'
    cert_dir = ca_dir + '/certs/'
    config = ca_dir + '/openssl.conf'

    @staticmethod
    def print_help():
        """
        A simple help printing
        """
        print("keychestamp, version %s. \n(c) 2019 KeyChest Ltd. Visit https://gitlab.com/keychest .\n"
              "The proxy accepts the following parameters:" % proxy_version)
        print("  -h, --help - this help, if present it will stop the process")
        print("  -l, --level <DEBUG|ERROR|WARNING|INFO|CRITICAL> - minimum level to log, default is INFO")
        print("  -n, --noapi - disables API logging, starts logging into /var/log/keychestamp/audit.json")
        print("  -f --file <file> - enable local login and set a custom location")
        print("  -p, --port <int> - setting the listening port of the proxy")
        print("  -a, --addr <IP addr> - by default it responds to all requests")
        print("  -e, --etc <folder> - working directory for storing config. data")
        print("  -c, --ca - just returns its root certificate in PEM format and exits\n\n")

    @staticmethod
    def _test_writable(_path):
        # test if we can read and write
        _file = _path + "/.test_file"
        try:
            with open(_file, "w") as f:
                x = str(time.time())
                f.write(x)
            with open(_file, "r") as f:
                x2 = f.read()
            if x != x2:
                sys.stderr.write("working directory not writeable\n")
                return -1
            os.remove(_file)
        except Exception as ex:
            sys.stderr.write("can't write into the working directory: %s\n" % str(ex))
            return -1

        _dir = _path + '/.test_dir'
        try:
            if os.path.exists(_dir):
                os.rmdir(_dir)
            os.mkdir(_dir, 0x770)
            os.rmdir(_dir)
        except Exception as ex:
            sys.stderr.write("can't create folder in the working directory: %s\n" % str(ex))
            return -1
        return 0

    @staticmethod
    def _test_config(path):

        try:
            with open(path, 'a') as f:
                f.write('')
            AmpConfig.file_logging = path
            return 0
        except IOError as x:
            if x.errno == errno.EACCES:
                sys.stderr.write("Can't access the file: %s" % path)
            elif x.errno == errno.EISDIR:
                sys.stderr.write("This is a folder, a file expected: %s" % path)
            return -1

    @staticmethod
    def parse_params():

        logging.getLogger().setLevel(logging.INFO)  # default level

        just_send_ca = False

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hl:nf:cp:a:e:',
                                       ['help', 'level=', 'noapi', 'file=', 'ca', 'port=', 'addr=', 'etc='])
        except getopt.GetoptError:
            # print help information and exit:
            AmpConfig.print_help()
            print("You provided %s" % ' '.join(sys.argv[1:]))
            if AmpConfig.ch:
                AmpConfig.ch.close()
            return -1

        for o, a in opts:
            if o in ('-h', '--help'):
                AmpConfig.print_help()
                if AmpConfig.ch:
                    AmpConfig.ch.close()
                return 1
            else:
                if o in ('-n', '--noapi'):
                    AmpConfig.api_logging = None
                    if AmpConfig.file_logging is None:
                        AmpConfig.file_logging = '/var/log/keychestamp/audit.json'
                if o in ('-l', '--level'):
                    if a.lower() in ['debug', 'info', 'warning', 'error', 'critical']:
                        if a.lower() == 'debug':
                            AmpConfig.log_level = logging.DEBUG
                        elif a.lower() == 'info':
                            AmpConfig.log_level = logging.INFO
                        elif a.lower() == 'warning':
                            AmpConfig.log_level = logging.WARNING
                        elif a.lower() == 'error':
                            AmpConfig.log_level = logging.ERROR
                        elif a.lower() == 'critical':
                            AmpConfig.log_level = logging.CRITICAL
                        logging.getLogger().setLevel(AmpConfig.log_level)
                if o in ('-e', '--etc'):
                    try:
                        AmpConfig.working_dir = a
                        if AmpConfig.working_dir and (AmpConfig.working_dir[len(AmpConfig.working_dir) - 1] == os.path.sep):
                            AmpConfig.working_dir = AmpConfig.working_dir[:-1]

                        if os.path.exists(a):
                            if os.path.isdir(a):
                                if AmpConfig._test_writable(AmpConfig.working_dir) != 0:
                                    return -1
                            else:
                                sys.stderr.write("working directory is not a directory")
                                return -1

                        else:
                            os.makedirs(a)
                            if AmpConfig._test_writable(AmpConfig.working_dir) != 0:
                                return -1
                            pass
                    except Exception as ex:
                        sys.stderr.write("working directory is incorrect: %s" % str(ex))
                if o in ('-f', '--file'):
                    _x = AmpConfig._test_config(a)
                    if _x != 0:
                        return -1
                if o in ('-p', '--port'):
                    try:
                        new_port = int(a)
                        if (new_port < 1) or (new_port > 65535):
                            sys.stderr.write("The port is not a valid value between 1-65535\n\n")
                            return -1
                        AmpConfig.port = new_port
                    except ValueError:
                        sys.stderr.write("The port you entered is not an integer\n\n")
                        return -1
                if o in ('-a', '--addr'):
                    AmpConfig.address = a.strip()
                if o in ('-c', '--ca'):
                    just_send_ca = True

        if AmpConfig.working_dir is None:
            AmpConfig.working_dir = os.getcwd()
            if AmpConfig._test_writable(AmpConfig.working_dir) != 0:
                return -1
        sys.stderr.write("working directory is %s\n" % AmpConfig.working_dir)

        # we can set folders for CA
        AmpConfig.ca_dir = AmpConfig.working_dir + '/ca'
        AmpConfig.ca_key = AmpConfig.ca_dir + '/private/ca.key'
        AmpConfig.ca_cert = AmpConfig.ca_dir + '/certs/ca.crt'
        AmpConfig.cert_key = AmpConfig.ca_dir + '/private/cert.key'
        AmpConfig.cert_dir = AmpConfig.ca_dir + '/certs/'
        AmpConfig.config = AmpConfig.ca_dir + '/openssl.conf'

        AmpConfig.ensureCA()

        if just_send_ca:
            cert = None
            try:
                with open(AmpConfig.ca_cert, "r") as f:
                    cert = f.read()
            except Exception as ex:
                sys.stderr.write("Reading CA cert was not successful: %s\n\n" % str(ex))
                pass
            if cert:
                sys.stdout.write(cert)
                sys.stdout.flush()
            return 1
        else:
            if AmpConfig.file_logging is not None:
                _x = AmpConfig._test_config(AmpConfig.file_logging)
                if _x != 0:
                    return -1
            return 0  # all ok

    @staticmethod
    def set_logging():
        # noinspection PyUnusedLocal
        def usage_log(message, *args, **kws):
            # noinspection PyUnresolvedReferences
            if logging.getLogger().isEnabledFor(logging.OPS_LEVEL):
                # let's do JSON encoding here
                # noinspection PyUnresolvedReferences
                message = QueueHandler.create_json_msg(message, **kws)
                # noinspection PyUnresolvedReferences
                logging.log(logging.OPS_LEVEL, message)

        # noinspection PyUnusedLocal
        def debug_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.DEBUG):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.DEBUG, message)

        # noinspection PyUnusedLocal
        def info_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.INFO):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.INFO, message)

        # noinspection PyUnusedLocal
        def warning_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.WARNING):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.WARNING, message)

        # noinspection PyUnusedLocal
        def error_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.ERROR):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.ERROR, message)

        # noinspection PyUnusedLocal
        def critical_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.CRITICAL):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.CRITICAL, message)

        logging.OPS_LEVEL = 60
        # noinspection PyUnresolvedReferences
        logging.addLevelName(logging.OPS_LEVEL, "USE")
        logging.Logger.usage = usage_log
        logging.usage = usage_log

        logging.Logger.debug = debug_log
        logging.debug = debug_log
        logging.Logger.warning = warning_log
        logging.warning = warning_log
        logging.Logger.warn = warning_log
        logging.warn = warning_log
        logging.Logger.info = info_log
        logging.info = info_log
        logging.Logger.error = error_log
        logging.error = error_log
        logging.Logger.critical = critical_log
        logging.critical = critical_log

        # items to be added to all usage logs
        logging.use_counter = 1
        logging.host = socket.gethostname()
        logging.ipaddress = socket.gethostbyname(socket.gethostname())

        logger = logging.getLogger()
        logging.basicConfig(datefmt='%Y-%m-%d %H:%M:%S')
        logger.setLevel(AmpConfig.log_level)
        AmpConfig.ch = QueueHandler(api_logging=AmpConfig.api_logging, file_logging=AmpConfig.file_logging)
        fmt = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
        AmpConfig.ch.setFormatter(fmt)
        AmpConfig.ch.setLevel(logging.INFO)
        for x in logger.handlers:
            logger.removeHandler(x)
        logger.addHandler(AmpConfig.ch)
        pass

    @staticmethod
    def join_with_script_dir(path):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)

    @staticmethod
    def ensure_name_cert(hostname):

        cert_path = "%s/%s.crt" % (AmpConfig.cert_dir.rstrip('/'), hostname)
        AmpConfig.update_pki_config(AmpConfig.config, hostname)
        if not os.path.isfile(cert_path):
            epoch = "%d" % (time.time() * 1000)
            # openssl 1.1. allows req with   "-addext", "subjectAltName = DNS:%s" % hostname
            p1 = Popen(["openssl", "req", "-new", '-inform', 'pem', "-nodes", "-key", AmpConfig.cert_key, "-extensions", "server_cert",
                        "-subj", "/CN=%s" % hostname, '-config', AmpConfig.config],
                       stdout=PIPE)

            p2 = Popen(["openssl", "x509", "-req", "-days", "365", "-CA", AmpConfig.ca_cert, "-CAkey", AmpConfig.ca_key,
                        "-set_serial", epoch, "-sha256", "-extfile", AmpConfig.config, '-extensions', 'server_cert', "-out", cert_path],
                       stdin=p1.stdout, stderr=PIPE)
            p2.communicate()
        return None

    @staticmethod
    def update_pki_config(_path, domain=None):
        # create the configuration file for the CA
        with open(_path, 'w') as f:
            f.writelines([
                '[ ca ]\n',
                'default_ca = CA_default\n',
                '\n',
                '[ CA_default ]\n',
                'dir               = %s/ca\n' % AmpConfig.working_dir,
                'certs             = $dir/certs\n',
                'crl_dir           = $dir/crl\n',
                'new_certs_dir     = $dir/newcerts\n',
                'database          = $dir/index.txt\n',
                'serial            = $dir/serial\n',
                'default_days      = 3650\n',
                'RANDFILE          = $dir/private/.rand\n',
                'private_key       = $dir/private/ca.key\n',
                'certificate       = $dir/certs/ca.crt\n',
                'default_md        = sha256\n',
                'preserve          = no\n',
                'name_opt          = ca_default\n',
                'cert_opt          = ca_default\n',
                'policy            = policy_strict\n',
                'copy_extensions   = copy\n',
                '\n',
                '[ req ]\n',
                'default_bits            = 2048\n',
                'default_md              = sha256\n',
                'distinguished_name      = req_dn\n',
                'prompt                  = yes\n',
                'encrypt_key             = no\n',
                'string_mask             = utf8only\n',
                '\n',
                '[ v3_ca ]\n',
                'basicConstraints        = critical,CA:true\n',
                'subjectKeyIdentifier    = hash\n',
                'authorityKeyIdentifier = keyid:always,issuer\n',
                'keyUsage                = critical,keyCertSign,cRLSign,digitalSignature\n',
                '\n',
                '[ req_dn ]\n',
                'countryName                     = Country Name (2 letter code)\n',
                '0.organizationName              = Organization Name\n',
                'organizationalUnitName          = Organizational Unit Name\n',
                'commonName                      = Common Name\n',
                '\n',
                'countryName_default             = US\n',
                '0.organizationName_default        = KeyChest\n',
                'organizationalUnitName_default  = KeyChestAmp\n',
                '\n',
                '[ policy_loose ]\n',
                'countryName             = optional\n',
                'organizationName        = optional\n',
                'organizationalUnitName  = optional\n',
                'commonName              = supplied\n',
                '\n',
                '[ policy_strict ]\n,'
                'countryName             = match\n',
                'organizationName        = match\n',
                'organizationalUnitName  = optional\n',
                'commonName              = supplied\n',
                '\n',
                '[ server_cert ]\n',
                'basicConstraints       = CA:FALSE\n',
                'subjectKeyIdentifier   = hash\n',
                'authorityKeyIdentifier = keyid,issuer:always\n',
                'keyUsage               = critical,digitalSignature,keyEncipherment\n',
                'extendedKeyUsage       = serverAuth\n'
            ])
            if domain:
                f.writelines([
                    'subjectAltName=DNS:%s\n' % domain
                ])

    @staticmethod
    def ensureCA():
        if not os.path.exists(AmpConfig.ca_dir):
            os.mkdir(AmpConfig.ca_dir, 0o770)
        if not os.path.exists(AmpConfig.ca_dir + '/index.txt'):
            with open(AmpConfig.ca_dir + '/index.txt', 'w') as f:
                f.write("")
        if not os.path.exists(AmpConfig.ca_dir + '/serial'):
            with open(AmpConfig.ca_dir + '/serial', 'w') as f:
                f.write("1000")
        if not os.path.exists(AmpConfig.ca_dir + '/certs'):
            os.mkdir(AmpConfig.ca_dir + '/certs', 0o770)
        if not os.path.exists(AmpConfig.ca_dir + '/crl'):
            os.mkdir(AmpConfig.ca_dir + '/crl', 0o770)
        if not os.path.exists(AmpConfig.ca_dir + '/newcerts'):
            os.mkdir(AmpConfig.ca_dir + '/newcerts', 0o770)
        if not os.path.exists(AmpConfig.ca_dir + '/private'):
            os.mkdir(AmpConfig.ca_dir + '/private', 0o700)

        AmpConfig.update_pki_config(AmpConfig.config)

        if (not os.path.isfile(AmpConfig.ca_key)) or (not os.path.isfile(AmpConfig.ca_cert)) or (not os.path.isfile(AmpConfig.cert_key)):
            # and os.path.isfile(certkey) and os.path.isdir(certdir):
            # generate a new CA key
            p1 = Popen(["openssl", "genrsa", "-out", AmpConfig.ca_key], stderr=PIPE)
            # create a new CA cert
            p1.communicate()
            p2 = Popen(["openssl", "req", "-new", "-x509", '-inform', 'pem', "-nodes", "-key", AmpConfig.ca_key,
                        "-extensions", "v3_ca", "-out", AmpConfig.ca_cert, "-days", "3650", "-config", AmpConfig.config,
                        '-subj', '/C=US/O=KeyChest/OU=KeyChest ACMEv2 Proxy'],
                       stdout=PIPE, stderr=PIPE)
            p2.communicate()
            p3 = Popen(['openssl', 'genrsa', '-out', AmpConfig.cert_key, "2048"],
                       stderr=PIPE)
            p3.communicate()
        pass

    @staticmethod
    def cert_ready():
        return os.path.isfile(AmpConfig.ca_key) and os.path.isfile(AmpConfig.ca_cert) \
               and os.path.isfile(AmpConfig.cert_key) and os.path.isdir(AmpConfig.cert_dir)
        pass

    @staticmethod
    def get_cert_path(hostname):

        _path = "%s/%s.crt" % (AmpConfig.cert_dir.rstrip('/'), hostname)
        return _path
