#!/usr/bin/env python

from PyQt5 import QtGui, QtCore, QtQml
import os
import sys
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


def main():
    app = QtGui.QGuiApplication([])
    engine = QtQml.QQmlApplicationEngine()

    context = engine.rootContext()
    now_model = NowModel()
    context.setContextProperty('now_model', now_model)

    qml_filename = os.path.join(os.path.dirname(__file__), 'now_example.qml')
    engine.load(qml_filename)

    qml_root = engine.rootObjects()[0]
    qml_root.updateModel.connect(now_model.update)

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
