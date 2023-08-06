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
import base64
import json
import logging
import time
import traceback
from urllib.parse import urlparse

__copyright__ = 'KeyChest Ltd'
__email__ = 'support@keychest.net'
__status__ = 'Development'


class AcmeLog(object):

    @staticmethod
    def repeater(req_hdrs, code, path, req_body, resp_body, resp_hdrs):
        """
        This is a simple method that checks messages, parses selected ones and logs them
        :param resp_body:
        :type code: int
        :param code: response code
        :param req_hdrs: headers of the request - it includes 'Host'/server we assume prod/staging for LE but it can be any
        :param path: path of the GET/POST request
        :param req_body: data sent from the client
        :return:
        """
        try:
            client = req_hdrs['X-Forwarded-For']
            server = req_hdrs['Host']
            agent = req_hdrs['User-Agent']
            if resp_hdrs:
                location = resp_hdrs['Location']
            else:
                location = None

            body = AcmeLog.decode_acme2(req_body)
            response = AcmeLog.decode_response(resp_body)

            logging.debug("repeater call", path=path, code=code, server=server, client=client, agent=agent)
            _path = path.lower()
            if '/directory' in path:
                logging.usage("directory", epoch=int(time.time()), client=client, server=server, code=code, agent=agent)
                pass
            elif 'acme/new-acct' in path:
                if ('contact' not in response) or ('initialIp' not in response) or ('status' not in response):
                    logging.error("Unrecognized body of new-acct", msg=req_body)
                elif location is None:
                    logging.error("Missing header Location in new-acct", msg=req_body, resp=resp_body)
                else:
                    email = "acme@keychest.net"
                    for each_contact in response['contact']:  # type: str
                        if each_contact.startswith('mailto:'):
                            email = each_contact.split(":")[1].strip().lower()

                    account = urlparse(location).path

                    logging.usage("new-acct", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  contact=response['contact'], email=email, account=account, source=response['initialIp'],
                                  status=response['status'])
                    pass
            elif 'acme/new-nonce' in path:
                logging.usage("new-nonce", epoch=int(time.time()), client=client, server=server, code=code, agent=agent)
                pass
            elif 'acme/new-order' in path:
                if (body is None) or ('kid' not in body):
                    logging.error("Unrecognized body of new-order", msg=req_body)
                elif ('identifiers' not in response) or ('authorizations' not in response) or ('finalize' not in response):
                    logging.error("Unrecognized response to new-order", msg=response)
                elif location is None:
                    logging.error("Missing location header in new-order", msg=response)
                else:
                    authz = []
                    for x in response['authorizations']:
                        _x = urlparse(x)
                        authz.append(_x.path)
                    finalize = urlparse(response['finalize']).path
                    kid = urlparse(body['kid']).path
                    loc = urlparse(location).path
                    identifiers = response['identifiers']
                    logging.usage("new-order", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  domains=identifiers, authz=authz, finalize=finalize, account=kid, order=loc)
                pass
            elif 'acme/revoke-cert' in path:
                if (body is None) or ('kid' not in body):
                    logging.error("Unrecognized body of revoke-cert", msg=req_body)
                else:
                    kid = urlparse(body['kid']).path
                    logging.usage("revoke-cert", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  account=kid)
            elif 'acme/key-change' in path:
                if (body is None) or ('kid' not in body):
                    logging.error("Unrecognized body of key-change", msg=req_body)
                else:
                    kid = urlparse(body['kid']).path
                    logging.usage("key-change", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  account=kid)
                pass
            elif 'acme/auth' in path:
                if (body is None) or ('kid' not in body) or ('url' not in body):
                    logging.error("Unrecognized body of auth", msg=req_body)
                elif (response is None) or ('status' not in response) or ('expires' not in response) or ('identifier' not in response):
                    logging.error("Unrecognized body of auth response", msg=resp_body)
                else:
                    kid = urlparse(body['kid']).path
                    authz = urlparse(body['url']).path
                    status = response['status']
                    expires = response['expires']
                    identifier = response['identifier']
                    logging.usage("auth", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  account=kid, authz=authz, status=status, expires=expires, identifier=identifier)
                pass
            elif 'acme/accnt' in path:
                pass
            elif 'acme/final' in path:
                if (body is None) or ('kid' not in body) or ('url' not in body):
                    logging.error("Unrecognized body of final", msg=req_body)
                elif (response is None) or ('certificate' not in response) or ('status' not in response):
                    logging.error("Unrecognized response of final", msg=resp_body)
                else:
                    kid = urlparse(body['kid']).path
                    loc = urlparse(body['url']).path
                    status = response['status']
                    cert = response['certificate']
                    cert = urlparse(cert).path
                    logging.usage("final", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  account=kid, status=status, cert=cert)
                pass
            elif 'acme/chall' in path:
                if (body is None) or ('kid' not in body) or ('url' not in body):
                    logging.error("Unrecognized body of chall", msg=req_body)
                elif (response is None) or ('status' not in response):
                    logging.error("Unrecognized response of chall", msg=resp_body)
                else:
                    kid = urlparse(body['kid']).path
                    loc = urlparse(body['url']).path
                    status = response['status']
                    logging.usage("chall", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  account=kid, chall=loc, status=status)
                pass
            elif 'acme/order' in path:
                if (body is None) or ('kid' not in body) or ('url' not in body):
                    logging.error("Unrecognized body of order", msg=req_body)
                elif (response is None) or ('identifiers' not in response) or ('status' not in response) \
                        or ('authorizations' not in response) or ('finalize' not in response):
                    logging.error("Unrecognized response of order", msg=resp_body)
                else:
                    kid = urlparse(body['kid']).path
                    loc = urlparse(body['url']).path
                    status = response['status']
                    identifiers = response['identifiers']
                    authorizations = response['authorizations']
                    finalize = response['finalize']
                    if 'certificate' in response:
                        certificate = response['certificate']
                    else:
                        certificate = ""
                    authz = []
                    for _x in authorizations:
                        authz.append(urlparse(_x).path)
                    final = urlparse(finalize).path
                    logging.usage("order", epoch=int(time.time()), client=client, server=server, code=code, agent=agent,
                                  account=kid, chall=loc, status=status, identifiers=identifiers, finalize=final, certificate=certificate)
            else:
                logging.error("Unrecognized message", path=path)
        except Exception as ex:
            tb = "; ".join(traceback.format_exc(3).splitlines())
            logging.error("Unexpected exception in repeater", cause=str(ex), traceback=tb)
        return

    @staticmethod
    def decode_acme2(msg):

        if (msg is None) or len(msg) < 2:
            return None
        try:
            tamper = json.loads(msg)

            if 'protected' in tamper:
                protected = tamper['protected']
                protected_plain = base64.b64decode(protected + "=" * ((4 - len(protected) % 4) % 4))
                protected_json = json.loads(protected_plain.decode())
                return protected_json
            else:
                return tamper
        except Exception as ex:
            logging.info("Error parsing ACMEv2 message", msg=msg.decode(), cause=str(ex))
            return None

    @staticmethod
    def decode_response(msg):

        if (msg is None) or len(msg) < 2:
            return None
        try:
            j_msg = json.loads(msg)
            return j_msg
        except Exception as ex:
            logging.info("Error parsing ACMEv2 response", msg=msg.decode(), cause=str(ex))
            return None
