import json
import math
import numpy as np

from PyQt5 import QtWidgets, uic, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QDialog, QVBoxLayout

import pyqtgraph as pg
from pyqtgraph import PlotWidget, PlotItem, GraphicsWidget, GraphicsLayout, GraphicsLayoutWidget

class MainPlot(GraphicsLayoutWidget):

    updateSignal = QtCore.pyqtSignal()

    def __init__(self, nplots=1, samplingperiod=1):
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        super().__init__()
        self.pitens = []
        for k in range(nplots):
            self.pitens.append(self.addPlot(row=k, col=0))
        for pi in self.pitens:
            pi.showAxis('top')
            pi.getAxis('top').setStyle(showValues=False)
            pi.showAxis('right')
            pi.getAxis('right').setStyle(showValues=False)
            pi.hideButtons()
            pi.setMouseEnabled(False, True)
            pi.setMenuEnabled(True, None)
            pi.setClipToView(True)
        self.samplingperiod = samplingperiod
        self.janelax, self.miny, self.maxy, self.autoy, self.vetoreixox, self.npontosjanela = [], [], [], [], [], []
        for k in range(len(self.pitens)):
            self.janelax.append(30)
            self.miny.append(0)
            self.maxy.append(256)
            self.autoy.append(False)
            self.vetoreixox.append(0)
            self.npontosjanela.append(0)
        self.flagchangeranges = True
        for pi in self.pitens:
            pi.sigXRangeChanged.connect(self.sigXRangeChanged)
            pi.sigYRangeChanged.connect(self.sigYRangeChanged)
        self.pens = [ pg.mkPen('b', width=2), 
                    pg.mkPen('r', width=2), 
                    pg.mkPen('m', width=2), 
                    pg.mkPen('k', width=2), 
                    pg.mkPen('g', width=2),
                    pg.mkPen('b', width=2, style=QtCore.Qt.DashLine), 
                    pg.mkPen('r', width=2, style=QtCore.Qt.DashLine), 
                    pg.mkPen('m', width=2, style=QtCore.Qt.DashLine), 
                    pg.mkPen('k', width=2, style=QtCore.Qt.DashLine), 
                    pg.mkPen('g', width=2, style=QtCore.Qt.DashLine) ]
        self.plotSetup()

    def setDataman(self,dataman):
        self.dman = dataman

    def plotSetup(self, samplingperiod=1, enablemap=[], dataman=None):
        self.dman = dataman
        self.samplingperiod = samplingperiod 
        self.lines = []   
        self.setpointline = None     
        for k in range(1):
            self.pitens[k].disableAutoRange()
            self.pitens[k].setLabel('bottom', 'Tempo (s)')
            self.pitens[k].setLabel('left', 'Temperatura (°C)')
            self.pitens[k].setXRange(-self.janelax[k], 0, padding=0.01)
            self.pitens[k].setYRange(self.miny[k], self.maxy[k], padding=0.01)            
            # self.npontosjanela[k] = int(self.janelax[k] / self.samplingperiod)
            # self.vetoreixox[k] = np.linspace(-self.janelax[k], 0, self.npontosjanela[k])
            self.npontosjanela[k] = math.floor(self.janelax[k] / self.samplingperiod) + 1
            self.vetoreixox[k] = np.linspace(-self.janelax[k], 0, self.npontosjanela[k])
            ctlines = 0
            self.lineidxs = []
            self.pitens[k].clear()
            for idx,en in enumerate(enablemap):
                if en:
                    self.lines.append( self.pitens[k].plot(np.array([]), np.array([]), pen=self.pens[ctlines]) )
                    self.lines[-1].setClipToView(False)
                    ctlines += 1
                    self.lineidxs.append(idx)
            self.setpointline = self.pitens[k].plot(np.array([]), np.array([]), pen= pg.mkPen('r', width=1, style=QtCore.Qt.DotLine))
            self.setpointline.setClipToView(False)
        

    def updateFig(self):
        limi = [0, 0]
        limf = [0, 0]
        npontos = [0, 0]
        for k in range(1):
            limi[k] = self.dman.globalctreadings - self.npontosjanela[k]
            limf[k] = self.dman.globalctreadings
            if limi[k] < 0:
                limi[k] = 0
                npontos[k] = limf[k] - limi[k] #+ 1
            else:
                npontos[k] = self.npontosjanela[k]
        if npontos[0] > 0:
            if self.dman.setpoint is not None:
                # print(np.array([float(-self.janelax[0]), 0.0]),np.array([self.dman.setpoint, self.dman.setpoint]))
                self.setpointline.setData(np.array([float(-self.janelax[0]), 0.0]),np.array([self.dman.setpoint, self.dman.setpoint]))
            else:
                self.setpointline.setData([], [])
            self.vetoreixox[0][0:npontos[0]] = self.dman.TTime[0][limi[0]:limf[0]] - self.dman.TTime[0][limf[0]-1]
            for k,idx in enumerate(self.lineidxs):
                # self.lines[k].setData(self.vetoreixox[0][-npontos[0]:], self.dman.TData[idx][limi[0]:limf[0]])
                self.lines[k].setData(self.vetoreixox[0][0:npontos[0]], np.nan_to_num(self.dman.TData[idx][limi[0]:limf[0]]))
            
        else:
            for k in range(len(self.lines)):
                self.lines[k].setData([], [])
            self.setpointline.setData([], [])       


    def sizeHint(self):
        if self.parent() is None:
            return QtCore.QSize(30, 30)
        else:
            return QtCore.QSize(self.parent().frameGeometry().width(), self.parent().frameGeometry().height())

    def sigYRangeChanged(self):
        for k, pi in enumerate(self.pitens):
            rgs = pi.viewRange()
            if self.flagchangeranges:
                self.miny[k] = rgs[1][0]
                self.maxy[k] = rgs[1][1]

    def sigXRangeChanged(self):        
        for k, pi in enumerate(self.pitens):
            if self.flagchangeranges:
                self.janelax[k] = round(-pi.viewRange()[0][0])
            self.npontosjanela[k] = math.floor(self.janelax[k] / self.samplingperiod) + 1
            self.vetoreixox[k] = np.linspace(-self.janelax[k], 0, self.npontosjanela[k])


    def getConfigString(self):
        mvars = vars(self)
        d = {}
        for k in ('janelax', 'miny', 'maxy', 'autoy'):
            d[k] = mvars[k]
        return json.dumps(d)

    def parseConfigString(self, strdata):
        d = json.loads(strdata)
        ll = len(d['janelax'])
        self.janelax[0:ll] = d['janelax']
        self.miny[0:ll] = d['miny']
        self.maxy[0:ll] = d['maxy']
        self.autoy[0:ll] = d['autoy']
        self.flagchangeranges = False
        for k, pi in enumerate(self.pitens):
            self.pitens[k].setXRange(-self.janelax[k], 0.0, padding=0.01)
            self.pitens[k].setYRange(self.miny[k], self.maxy[k], padding=0.01)
        self.flagchangeranges = True
