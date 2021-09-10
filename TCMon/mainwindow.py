from pathlib import Path

from .TCMonWindow import Ui_MainWindow
from .MainPlot import MainPlot

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox

class mainwindow(QtWidgets.QMainWindow):


    def __init__(self, app):
        super(mainwindow, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = "D://"
        self.saveconfigtypes = [QtWidgets.QCheckBox, QtWidgets.QComboBox,
                                QtWidgets.QDoubleSpinBox, QtWidgets.QSpinBox, QtWidgets.QLineEdit]
        
        self.checksT = [self.ui.checkT1,self.ui.checkT2,self.ui.checkT3,self.ui.checkT4,self.ui.checkT5,self.ui.checkT6,self.ui.checkT7,self.ui.checkT8]
        self.checksE = [self.ui.checkE1, self.ui.checkE2]
        self.valsT = [self.ui.valT1,self.ui.valT2,self.ui.valT3,self.ui.valT4,self.ui.valT5,self.ui.valT6,self.ui.valT7,self.ui.valT8]
        self.valsE = [self.ui.valE1, self.ui.valE2]

        self.disabledWhenRunning = self.checksT + self.checksE + [self.ui.checkCtrlAuto, self.ui.checkCtrlManual, 
                              self.ui.comboTermoparCtrl, self.ui.comboPorta, self.ui.comboTipoTermopar, self.ui.comboAmostragem,
                              self.ui.spinKd, self.ui.spinKi, self.ui.spinKp, self.ui.bLimpar]

        self.ui.bIniciar.clicked.connect(self.bInit)
        self.ui.bLimpar.clicked.connect(self.bLimpar)

        self.ui.checkCtrlManual.toggled.connect(self.ctrlManualChanged)
        self.ui.checkCtrlAuto.toggled.connect(self.ctrlAutoChanged)

        self.ui.spinSetPoint.editingFinished.connect(self.setPointChanged)
        self.ui.spinCtrlManual.editingFinished.connect(self.manualCtrlLevelChanged)
        # cc.editingFinished.connect(self.changeGeneratorConfig)editingFinished

        self.mainplot = MainPlot(nplots=1,samplingperiod=1)
        self.ui.plotWidgetLayout.addWidget(self.mainplot)

        self.driver = None

        self.flagsaved = True

        self.saveprefix = "TCMon"

        self.readConfig()

    
    
    def bInit(self):
        if self.driver is not None:
            self.flagsaved = False
            if self.driver.flagrunning:
                self.driver.paraLeituras()
                for comp in self.disabledWhenRunning:
                    comp.setEnabled(True)  
                self.ui.spinCtrlManual.setEnabled(True)
                self.ui.spinSetPoint.setEnabled(True)
                for val in self.valsT+self.valsE:
                    val.setEnabled(True)
            else:
                for comp in self.disabledWhenRunning:
                    comp.setEnabled(False)
                enablemap = []
                for val,chk in zip(self.valsT+self.valsE,self.checksT+self.checksE):
                    enablemap.append(chk.isChecked())
                    if not enablemap[-1]:
                        val.setEnabled(False)                  
                if not self.ui.checkCtrlAuto.isChecked():
                    self.ui.spinSetPoint.setEnabled(False)                    
                if not self.ui.checkCtrlManual.isChecked():
                    self.ui.spinCtrlManual.setEnabled(False)
                self.configCtrl()
                self.setPointChanged()
                self.manualCtrlLevelChanged()                
                amostr = self.ui.comboAmostragem.currentIndex() + 1
                self.mainplot.plotSetup(amostr,enablemap,self.driver.dman)            
                self.driver.iniciaLeituras(amostr,enablemap,self.ui.comboTipoTermopar.currentText())


    def errorStarting(self,msg):
        self.ui.statusbar.showMessage(msg)
        for comp in self.disabledWhenRunning:
                    comp.setEnabled(True)  
        self.ui.spinCtrlManual.setEnabled(True)
        self.ui.spinSetPoint.setEnabled(True)
        for val in self.valsT+self.valsE:
            val.setEnabled(True)



    def bLimpar(self):
        # TODO: confirmar se flagsaved = False
        self.flagsaved = True
        self.ui.statusbar.clearMessage()
        self.driver.dman.resetData()
        self.mainplot.setDataman(self.driver.dman)
        self.mainplot.updateFig()


    def setDriver(self,driver):
        self.driver = driver
    

    def setCurTime(self,time):
        self.ui.timeLabel.setText(f'{time} s')


    def setValText(self,text,idx):
        if idx <= 8:
            self.valsT[idx].setText(text)
        else:
            self.valsE[idx-8].setText(text)

    def setJunta(self,text):
        self.ui.valRef.setText(text)

    def updatePlot(self):
        self.mainplot.updateFig()

    def ctrlAutoChanged(self):
        if self.ui.checkCtrlAuto.isChecked():
            self.ui.checkCtrlManual.setChecked(False)

        
    def ctrlManualChanged(self):
        if self.ui.checkCtrlManual.isChecked():
            self.ui.checkCtrlAuto.setChecked(False)

    def configCtrl(self):
        if self.driver is not None:
            self.driver.setCtrlConfig(
                'Manual' if self.ui.checkCtrlManual.isChecked() else ('Auto' if self.ui.checkCtrlAuto.isChecked() else 'Off'),
                self.ui.comboTermoparCtrl.currentIndex(),
                self.ui.spinKp.value(),
                self.ui.spinKi.value(),
                self.ui.spinKd.value()
            )

    def setPointChanged(self):
        if self.driver is not None:
            self.driver.changeSetPoint(self.ui.spinSetPoint.value())

    def manualCtrlLevelChanged(self):
        if self.driver is not None:
            self.driver.changeManualCtrlLevel(self.ui.spinCtrlManual.value())


    '''
        Salvar estado atual da aplicação (checks, combos, etc)
    '''
    def saveState(self, settings: QtCore.QSettings):
        if self.saveprefix is None:
            self.saveprefix = "TCMon"
        centralwidget = self.ui.centralwidget
        wdgs = centralwidget.findChildren(QtWidgets.QComboBox) 
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            settings.setValue(keyval, ww.currentIndex())
            settings.setValue(f'EN{keyval}', str(ww.isEnabled()))
        wdgs = centralwidget.findChildren(QtWidgets.QCheckBox)
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            settings.setValue(keyval, str(ww.isChecked()))
            settings.setValue(f'EN{keyval}', str(ww.isEnabled()))
        wdgs = centralwidget.findChildren(QtWidgets.QDoubleSpinBox) + centralwidget.findChildren(QtWidgets.QSpinBox)
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            # print(f'{keyval} - {ww.isEnabled()}')
            settings.setValue(keyval, ww.value())
            settings.setValue(f'EN{keyval}', str(ww.isEnabled()))


    '''
        Restaurar estado atual da aplicação (checks, combos, etc)
    '''
    def restoreState(self, settings: QtCore.QSettings):
        if self.saveprefix is None:
            self.saveprefix = "TCMon"
        centralwidget = self.ui.centralwidget
        wdgs = centralwidget.findChildren(QtWidgets.QComboBox,QtCore.QRegExp("combo.*")) 
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            if settings.value(keyval) is not None:
                ww.setCurrentIndex(int(settings.value(keyval)))
            if settings.value(f'EN{keyval}') is not None:
                ww.setEnabled(settings.value(f'EN{keyval}') == 'True')

        wdgs = centralwidget.findChildren(QtWidgets.QCheckBox,QtCore.QRegExp("check.*"))
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            if settings.value(keyval) is not None:
                ww.setChecked(settings.value(keyval) == 'True')
            if settings.value(f'EN{keyval}') is not None:
                ww.setEnabled(settings.value(f'EN{keyval}') == 'True')
        
        wdgs = centralwidget.findChildren(QtWidgets.QDoubleSpinBox)
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            # aux = settings.value(f'EN{keyval}')
            # print(f'{keyval} - {aux}')
            if settings.value(keyval) is not None:
                ww.setValue(float(settings.value(keyval)))
            if settings.value(f'EN{keyval}') is not None:
                ww.setEnabled(settings.value(f'EN{keyval}') == 'True')
        
        wdgs = centralwidget.findChildren(QtWidgets.QSpinBox)
        for ww in wdgs:
            keyval = f'{self.saveprefix}{ww.objectName()}'
            if settings.value(keyval) is not None:
                ww.setValue(int(settings.value(keyval)))
            if settings.value(f'EN{keyval}') is not None:
                ww.setEnabled(settings.value(f'EN{keyval}') == 'True')

    def writeConfig(self):
        settings = QtCore.QSettings("TCMonSoftware", "TCMon")    
        self.saveState(settings)

    def readConfig(self):        
        settings = QtCore.QSettings("TCMonSoftware", "TCMon")
        self.restoreState(settings)

    def closeEvent(self, event):
        if not event:
            # self.writeConfig()
            event = QtGui.QCloseEvent()
            event.accept = self.close
            event.ignore = (lambda *args: None)
        if self.driver.flagrunning:
            self.ui.statusbar.showMessage("Pare as leituras antes de fechar...")
            event.ignore()
        elif not self.flagsaved:
            reply = QMessageBox.question(self, 'Saindo', 'Existem dados não salvos, deseja mesmo sair?',
                                         QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
            if reply == QMessageBox.Yes:
                self.writeConfig()
                event.accept()
            else:
                event.ignore()
        else:
            self.writeConfig()
            event.accept()
 
