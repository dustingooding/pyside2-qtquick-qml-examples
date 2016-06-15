#!/usr/bin/env python

from PyQt5 import QtCore
import time
import datetime

class NowPure(object):

    def __init__(self):
        self.timestamp_pure = ''

    def update(self):
        self.timestamp_pure = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


class NowModel(QtCore.QObject):

    updated = QtCore.pyqtSignal()

    def __init__(self):
        super(NowModel, self).__init__()
        self.now_pure = NowPure()
        self.timestamp_model = ''

    @QtCore.pyqtSlot()
    def update(self):
        self.now_pure.update()
        self.timestamp_model = self.now_pure.timestamp_pure
        self.updated.emit()

    @QtCore.pyqtSlot(result=str)
    def timestamp(self):
        return self.timestamp_model