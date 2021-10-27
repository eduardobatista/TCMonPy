import os
import sys

from PySide2 import QtWidgets
from PySide2.QtCore import QThread,QTimer,QMutex,QWaitCondition

from . import mytimer, wthread, condwait, mutex

from .mainwindow import mainwindow
from .driverhardware import driverhardware

app = QtWidgets.QApplication([])
app.setStyle('Fusion')

mwindow = mainwindow(app)

driver = driverhardware(mwindow)

driver.moveToThread(wthread)
wthread.started.connect(driver.realizaLeituras) 

def pp():
    driver.sampletimeout()

mytimer.connectWithTimer(pp)
mytimer.start()

wthread.start()

mwindow.setDriver(driver)

mwindow.show()

sys.exit(app.exec_())
