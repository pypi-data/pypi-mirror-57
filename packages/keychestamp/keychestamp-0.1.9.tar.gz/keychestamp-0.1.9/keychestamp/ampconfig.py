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
import datetime
import errno
import getopt
import logging
import multiprocessing
import os
import socket
import sys
import tempfile

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
    temp_ca = None
    config_dir = '/etc/keychestamp'
    main_stop = multiprocessing.Event()

    @staticmethod
    def print_help():
        """
        A simple help printing
        """
        print("keychestamp, version %s. \n(c) KeyChest Ltd. Visit https://gitlab.com/keychest .\n\n"
              "The proxy accepts the following parameters:" % proxy_version)
        print("  -h, --help - this help, if present it will stop the process\n")
        print("  -l, --level <DEBUG|ERROR|WARNING|INFO|CRITICAL> - minimum level to log, default is INFO\n")
        print("  -n, --noapi - you can disable API logging\n")
        print("  -f --file <file> - path to a file where to store the logs, be default this is disabled\n")
        print("  -p, --port <int> - setting the listening port of the proxy\n")
        print("  -a, --addr <IP addr> - by default it responds to all requests\n")
        print("  -c, --ca - just returns its root certificate in PEM format and exits")

    @staticmethod
    def parse_params():

        logging.getLogger().setLevel(logging.INFO)  # default level

        try:
            opts, args = getopt.getopt(sys.argv[1:], 'hl:nf:cp:a:',
                                       ['help', 'level=', 'noapi', 'file=', 'ca', 'port=', 'addr='])
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

                if o in ('-f', '--file'):
                    try:
                        with open(a, 'a') as f:
                            f.write('')
                        AmpConfig.file_logging = a
                    except IOError as x:
                        if x.errno == errno.EACCES:
                            sys.stderr.write("Can't access the file: %s" % a)
                        elif x.errno == errno.EISDIR:
                            sys.stderr.write("This is a folder, a file expected: %s" % a)
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
                    cert = AmpConfig.getRootCert()
                    if AmpConfig.temp_ca is None:
                        _, temp_path = tempfile.mkstemp(suffix='.pem', prefix='keychestamp')
                        AmpConfig.temp_ca = temp_path

                    file = open(AmpConfig.temp_ca, 'wb')
                    file.write(cert)
                    file.close()

                    sys.stdout.write(AmpConfig.temp_ca)
                    return 1
        return 0
        pass

    @staticmethod
    def set_logging():
        def usage_log(message, *args, **kws):
            # noinspection PyUnresolvedReferences
            if logging.getLogger().isEnabledFor(logging.OPS_LEVEL):
                # let's do JSON encoding here
                # noinspection PyUnresolvedReferences
                message = QueueHandler.create_json_msg(message, **kws)
                # noinspection PyUnresolvedReferences
                logging.log(logging.OPS_LEVEL, message)

        def debug_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.DEBUG):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.DEBUG, message)

        def info_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.INFO):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.INFO, message)

        def warning_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.WARNING):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.WARNING, message)

        def error_log(message, *args, **kws):
            if logging.getLogger().isEnabledFor(logging.ERROR):
                message = QueueHandler.create_json_msg(message, **kws)
                logging.log(logging.ERROR, message)

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
        logger.setLevel(logging.INFO)
        AmpConfig.ch = QueueHandler(api_logging=AmpConfig.api_logging, file_logging=AmpConfig.file_logging)
        fmt = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s: %(message)s')
        AmpConfig.ch.setFormatter(fmt)
        AmpConfig.ch.setLevel(logging.INFO)
        for x in logger.handlers:
            logger.removeHandler(x)
        logger.addHandler(AmpConfig.ch)
        pass

    @classmethod
    def getRootCert(cls):

        ca_cert = AmpConfig.join_with_script_dir('ca.crt')
        with open(ca_cert, 'rb') as f:
            data = f.read()
        return data

    @staticmethod
    def join_with_script_dir(path):
        return os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
