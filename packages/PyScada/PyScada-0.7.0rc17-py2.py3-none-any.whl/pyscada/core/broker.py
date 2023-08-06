#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from pyscada.utils.scheduler import Process as BaseProcess
from django.conf import settings
from multiprocessing.connection import Client, Listener

import logging

logger = logging.getLogger(__name__)

BROKER_ADDRESS = ('localhost', 6000)


class BrokerProcess(BaseProcess):
    """
    receives cov signals from daq task and notifies the recivers about the changes
    """
    def __init__(self, dt=5, **kwargs):
        super(BrokerProcess, self).__init__(dt=dt, **kwargs)

    def loop(self):
        pass


class BrokerClient(object):
    authkey = settings.SECRET_KEY.encode()
    address = BROKER_ADDRESS
    conn = None

    def __init__(self):
        self.connect()

    def connect(self):
        if self.conn is not None:
            return False

        try:
            self.conn = Client(self.address, authkey=self.authkey)
            return True
        except ConnectionRefusedError:
            self.conn = None
            return False
        except:
            self.conn = None
            return False

    def cov_notification(self,rd):
        return self._send_data(1,rd)

    def _send_data(self, msg_type, data):
        if self.connect():
            self.conn.send(int(msg_type))
            if self.conn.recv() == 1:
                self.conn.send(data)
                if self.conn.recv() == 1:
                    return True
        return False


class BrokerListener(object):
    def __init__(self):
        pass


