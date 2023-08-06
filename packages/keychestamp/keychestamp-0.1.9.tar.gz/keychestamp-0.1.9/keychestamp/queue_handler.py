#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
***
Module:
***

https://mattgathu.github.io/multiprocessing-logging-in-python/

 Copyright (C) KeyCHest Ltd, registered in the United Kingdom.
 This file is owned exclusively by KeyChest Ltd.
 Unauthorized copying of this file, via any medium is strictly prohibited
 Proprietary and confidential
 Written by Dan Cvrcek <support@keychest.net>, 2019
"""
import datetime
import json
import time
import requests

__author__ = "Dan Cvrcek"
__copyright__ = 'KeyChest Ltd'
__email__ = 'support@keychest.net'
__status__ = 'Development'

import sys
import logging
import traceback
import threading
import multiprocessing
# noinspection PyCompatibility
from queue import Empty  # future is required by setup for py3
# noinspection PyPep8Naming
from logging import FileHandler as FH

from keychestamp.version import proxy_version


# ============================================================================
# Define Log Handler
# ============================================================================
# noinspection PyMissingOrEmptyDocstring
class QueueHandler(logging.Handler):
    """multiprocessing log handler

    This handler makes it possible for several processes
    to log to the same file by using a queue.

    """
    def __init__(self, api_logging=True, file_logging=None, fname=None):
        logging.Handler.__init__(self)

        if fname:
            self._handler = FH(fname)
        else:
            self._handler = logging.StreamHandler(sys.stderr)

        self.queue = multiprocessing.Queue(-1)
        self.queue_usage = multiprocessing.Queue(-1)
        self.queue_lock = threading.Lock()

        self.queue_usage_len = 0
        self.queue_len = 0
        self.usage_file = file_logging
        self.file_handle = None
        if api_logging:
            self.usage_url = "https://keychest.net/api/v1.0/amp"
        else:
            self.usage_url = None
        self.headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

        self.stop = multiprocessing.Event()

        thrd = threading.Thread(target=self.receive, args=(self.stop,), name="log listener")
        thrd.daemon = True
        thrd.start()
        thrd2 = threading.Thread(target=self.send_usage, args=(self.stop,), name="log pusher")
        thrd2.daemon = True
        thrd2.start()

    def setUsageFile(self, path):
        """

        :param path:
        :return:
        """
        pass

    def setUsageURL(self, path):
        """

        :param path:
        :return:
        """
        pass

    def setFormatter(self, fmt):
        logging.Handler.setFormatter(self, fmt)
        self._handler.setFormatter(fmt)

    def setLevel(self, level):
        self._handler.setLevel(level)

    def send_usage(self, stop_event):
        """

        :param stop_event
        :type stop_event: multiprocessing.Event
        :rtype: None
        """
        while not stop_event.is_set():  # type: multiprocessing.Event
            try:
                record = self.queue_usage.get(timeout=1)
                if record is None:
                    continue

                with self.queue_lock:
                    self.queue_len -= 1

                if self.usage_url or self.usage_file:
                    j_record = json.loads(record)
                    j_record['backlog'] = self.queue_len
                    j_record['log_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                if self.usage_file:
                    if (self.file_handle is None) or self.file_handle.closed:
                        self.file_handle = open(self.usage_file, 'a')
                    # noinspection PyUnboundLocalVariable
                    self.file_handle.write(json.dumps(j_record)+"\n")
                    pass
                if self.usage_url is not None:
                    code = 0
                    while (code != 200) and (not stop_event.is_set()):
                        r = requests.post(url=self.usage_url, data=j_record, headers=self.headers, timeout=5)
                        code = r.status_code
                        if code != 200:
                            time.sleep(5)
                        # todo gracious treatment of the API down - create a temp file and store the data there till the API is ready

                    pass
            except Empty:
                if self.file_handle:
                    self.file_handle.flush()
                pass  # empty queue
            except (KeyboardInterrupt, SystemExit):
                if self.file_handle:
                    self.file_handle.flush()
                raise
            except EOFError:
                if self.file_handle:
                    self.file_handle.flush()
                break
            except BaseException as ex:
                if self.file_handle:
                    self.file_handle.flush()
                traceback.print_exc(file=sys.stderr)
                sys.stderr.write("Exception in queue_handler %s" % str(ex))

    def receive(self, stop_event):
        """

        :param stop_event
        :type stop_event: multiprocessing.Event
        :rtype: object
        """
        while not stop_event.is_set():  # type: multiprocessing.Event
            try:
                record = self.queue.get(timeout=2)
                if record is not None:
                    self._handler.emit(record)
            except Empty:
                pass  # empty queue
            except (KeyboardInterrupt, SystemExit):
                raise
            except EOFError:
                break
            except BaseException as ex:
                traceback.print_exc(file=sys.stderr)
                sys.stderr.write("Exception in queue_handler %s" % str(ex))

    def send(self, s):
        self.queue.put_nowait(s)
        with self.queue_lock:
            self.queue_len += 1

    def _format_record(self, record):
        if record.args:
            record.msg = record.msg % record.args
            record.args = None
        if record.exc_info:
            # noinspection PyUnusedLocal
            dummy = self.format(record)
            record.exc_info = None

        return record

    def emit(self, record):
        """

        :param self:
        :param record:
        """
        # noinspection PyBroadException
        try:
            if record.levelname == 'USE':
                self.queue_usage.put_nowait(record.msg)
                with self.queue_lock:
                    self.queue_len += 1
                pass
            else:
                s = self._format_record(record)
                self.send(s)
        except (KeyboardInterrupt, SystemExit):
            raise
        except BaseException:
            self.handleError(record)

    @staticmethod
    def create_json_msg(message, **kws):
        # noinspection PyUnresolvedReferences
        _temp = {
            'msg': message,
            'params': {},
            'id': logging.use_counter,
            'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'host': logging.host,
            'ip': logging.ipaddress,
            'version': proxy_version
        }
        # noinspection PyUnresolvedReferences
        logging.use_counter += 1
        if kws and (len(kws) > 0):
            for key, item in kws.items():
                if key.lower() == 'code':
                    _temp['code'] = item
                else:
                    _temp['params'][key] = item

        message = json.dumps(_temp)
        return message

    def close(self):
        self.stop.set()
        if self._handler:
            self._handler.close()
        if logging.Handler:
            logging.Handler.close(self)
