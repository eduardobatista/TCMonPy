import os
import sys

from PyQt5 import QtWidgets

from .mainwindow import mainwindow
from .driverhardware import driverhardware

app = QtWidgets.QApplication([])
app.setStyle('Fusion')

mwindow = mainwindow(app)

driver = driverhardware(mwindow)

mwindow.setDriver(driver)

mwindow.show()

sys.exit(app.exec())
