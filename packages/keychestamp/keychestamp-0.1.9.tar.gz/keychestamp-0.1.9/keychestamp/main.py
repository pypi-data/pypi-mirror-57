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
import signal
import sys
import time
import threading

from keychestamp import ampconfig
from keychestamp.ampconfig import AmpConfig
from keychestamp.proxy import ProxyRequestHandler, ThreadingHTTPServer

__copyright__ = 'KeyChest Ltd'
__email__ = 'support@keychest.net'
__status__ = 'Development'


# noinspection PyUnusedLocal
def signal_handler(sig, frame):
    """
    Signal handler
    :param sig:
    :param frame:
    :return:
    """

    AmpConfig.main_stop.set()
    AmpConfig.ch.close()
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

    # noinspection PyTypeChecker
    counter = 1
    watched_thread = None  # type: threading.Thread
    logging.debug("Proxy watcher started at %d" % int(time.time()))
    while not AmpConfig.main_stop.set():
        # noinspection PyBroadException
        try:
            if (watched_thread is None) or (not watched_thread.is_alive()):
                watched_thread = threading.Thread(target=process_proxy, args=())
                watched_thread.name = "proxy_thread_" + str(counter)
                counter += 1
                watched_thread.start()
            time.sleep(1)
            pass
        except Exception as e:
            logging.error("Exception in the proxy watcher: %s" % str(e))
            pass


def process_proxy():

    server_address = (AmpConfig.address, AmpConfig.port)

    ProxyRequestHandler.protocol_version  = "HTTP/1.1"
    httpd = ThreadingHTTPServer(server_address, ProxyRequestHandler)

    sa = httpd.socket.getsockname()
    logging.usage("x", x=3)
    logging.info("Serving HTTP Proxy on", iface=sa[0], port=sa[1])
    httpd.serve_forever()
    pass


def main():
    """
    Main entry function
    """

    sys.stdout.write("KeyChestAmp started\n")
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

    to_exit = ampconfig.AmpConfig.parse_params()
    if to_exit < 0:
        sys.stdout.write("Error in parameters\n\n")
        sys.exit(-1)
    elif to_exit > 0:
        sys.exit(0)

    AmpConfig.set_logging()
    logging.debug("KeyChestAmp launching the proxy")

    process_watch()  # start the watcher, which will keep the proxy running
    # the above is blocking - only get past when terminating
    sys.stdout.write("KeyChestAmp terminated\n")
    sys.stdout.flush()

    # let's launch the watcher thread

    # alternative logbook logging
    # log_dispatcher_thread = LogDispatcher(logger_stop_event, ip="127.0.0.1")
    # log_dispatcher_thread.name = "LogDispatcher"
    # log_dispatcher_thread.start()

    # setup_logging(log_level, true_socket=True)  # alternative logbook logging
    # logging.getLogger().setLevel(log_level)


if __name__ == '__main__':
    # !!!! just for testing - not executed once installed
    try:
        main()
    except Exception as ex:
        sys.stderr.write(str(ex))
        sys.stderr.flush()
    finally:
        sys.stderr.write("KeyChestAmp terminated\n")
        sys.stderr.flush()
        pass
