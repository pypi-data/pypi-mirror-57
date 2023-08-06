#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module:
***

 Copyright (C) KeyChest Ltd, registered in the United Kingdom.
 This file is owned exclusively by KeyChest Ltd.
 Unauthorized copying of this file, via any medium is strictly prohibited
 Proprietary and confidential
 Written by Dan Cvrcek <support@keychest.net>, 2019
"""
import logging
import multiprocessing
import signal
import sys
import time

from keychestamp import ampconfig
from keychestamp.ampconfig import AmpConfig
from keychestamp.proxy import ProxyRequestHandler, ThreadingHTTPServer

__copyright__ = 'KeyChest Ltd'
__email__ = 'support@keychest.net'
__status__ = 'Development'

main_stop = multiprocessing.Event()


# noinspection PyUnusedLocal
def signal_handler(sig, frame):
    """
    Signal handler
    :param sig:
    :param frame:
    :return:
    """
    global main_stop  # type: multiprocessing.Event()

    main_stop.set()
    sys.stderr.write("Waiting 1 second to exit\n")
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    time.sleep(1)

    raise SystemExit('Terminating FoxyProxy')  # this is supposed to kill main()


def process_watch():
    """
    A simple process watch function that will try to close worker processes that died
    :return:
    """

    re_raise = False
    while True:
        time.sleep(10)
        logging.debug("watcher run started at %d" % int(time.time()))
        # noinspection PyBroadException
        try:
            pass
        except Exception:
            pass
        finally:
            logging.debug("watch run finished at %d" % int(time.time()))
            if re_raise:
                raise Exception("terminating process_watch")


def process_proxy():

    server_address = (AmpConfig.address, AmpConfig.port)

    ProxyRequestHandler.protocol_version  = "HTTP/1.1"
    httpd = ThreadingHTTPServer(server_address, ProxyRequestHandler)

    sa = httpd.socket.getsockname()
    logging.info("Serving HTTP Proxy on", iface=sa[0], port=sa[1])
    httpd.serve_forever()
    pass


def main():
    """
    Main entry function
    """

    # noinspection PyBroadException
    try:
        signal.signal(signal.SIGINT, signal_handler)
    except Exception:
        pass
    # noinspection PyBroadException
    try:
        signal.signal(signal.SIGTERM, signal_handler)
    except Exception:
        pass

    if len(sys.argv) > 1:
        if ampconfig.AmpConfig.parse_params() != 0:
            sys.stdout.write("Error in parameters\n\n")
            sys.exit(-1)

    # alternative logbook logging
    # log_dispatcher_thread = LogDispatcher(logger_stop_event, ip="127.0.0.1")
    # log_dispatcher_thread.name = "LogDispatcher"
    # log_dispatcher_thread.start()

    # setup_logging(log_level, true_socket=True)  # alternative logbook logging
    # logging.getLogger().setLevel(log_level)


if __name__ == '__main__':
    try:

        AmpConfig.set_logging()
        logging.usage("KeyChestAmp started")
        logging.usage("KeyChestAmp started", x=3, y="s")
        logging.info("KeyChestAmp 2")
        logging.critical("KeyChestAmp 3")

        main()
        time.sleep(100000)
        sys.stderr.write("KeyChestAmp terminated\n")
        sys.stderr.flush()
    finally:
        pass
