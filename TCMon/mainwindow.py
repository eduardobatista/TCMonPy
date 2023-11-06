from pathlib import Path
from os import getenv

from .TCMonWindow import Ui_MainWindow
from .MainPlot import MainPlot
from .Updater import Updater
from .driverhardware import driverhardware

from PySide2 import QtWidgets, QtGui, QtCore
from PySide2.QtWidgets import QMessageBox,QFileDialog,QMessageBox,QProgressDialog
from PySide2.QtCore import QThread

class mainwindow(QtWidgets.QMainWindow):


    def __init__(self, app):
        super(mainwindow, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.workdir = Path.home()
        self.saveconfigtypes = [QtWidgets.QCheckBox, QtWidgets.QComboBox,
                                QtWidgets.QDoubleSpinBox, QtWidgets.QSpinBox, QtWidgets.QLineEdit]
        
        self.checksT = [self.ui.checkT1,self.ui.checkT2,self.ui.checkT3,self.ui.checkT4,self.ui.checkT5,self.ui.checkT6,self.ui.checkT7,self.ui.checkT8]
        self.checksE = [self.ui.checkE1, self.ui.checkE2]
        self.valsT = [self.ui.valT1,self.ui.valT2,self.ui.valT3,self.ui.valT4,self.ui.valT5,self.ui.valT6,self.ui.valT7,self.ui.valT8]
        self.valsE = [self.ui.valE1, self.ui.valE2]
        self.valPower = self.ui.valPower

        self.disabledWhenRunning = self.checksT + self.checksE + [ self.ui.comboTermoparCtrl, self.ui.comboPorta, 
                                                                   self.ui.comboTipoTermopar,
                                                                   self.ui.spinKd, self.ui.spinKi, self.ui.spinKp, self.ui.bLimpar]

        self.ui.bIniciar.clicked.connect(self.bInit)
        self.ui.bLimpar.clicked.connect(self.bLimpar)

        self.ui.checkCtrlManual.toggled.connect(self.ctrlManualChanged)
        self.ui.checkCtrlAuto.toggled.connect(self.ctrlAutoChanged)

        self.ui.spinSetPoint.editingFinished.connect(self.setPointChanged)
        self.ui.spinCtrlManual.editingFinished.connect(self.manualCtrlLevelChanged)

        self.mainplot = MainPlot(nplots=1,samplingperiod=1)
        self.ui.plotWidgetLayout.addWidget(self.mainplot)
        # self.mainplot.updateSignal.connect(self.updatePlot)

        self.ui.spinJanela.editingFinished.connect(self.changePlotWindow)
        self.ui.bPageDown.clicked.connect(self.mainplot.pageDown)
        self.ui.bPageUp.clicked.connect(self.mainplot.pageUp)

        self.ui.actionSalvar_Dados.triggered.connect(self.saveData)
        self.ui.actionAtualizarViaGit.triggered.connect(self.updateViaGit)

        self.driver = None

        self.flagsaved = True

        self.saveprefix = "TCMon"

        self.readConfig()


    def updateViaGit(self):  
        reply = QMessageBox().question(self,"Atualização","Deseja atualizar o software?")
        if (reply == QMessageBox.Yes):
            self.pdialog = QProgressDialog("Updating files...", "Abort update", 0, 100, self)
            # self.pdialog.setWindowModality(.WindowModal)
            self.pdialog.show()
            self.updt = Updater()
            self.updt.updated.connect(self.progressUpdate)
            self.updt.start()
    

    def progressUpdate(self,val):
        self.pdialog.setValue(val)

    
    def saveData(self):        
        if self.driver.flagrunning:
            self.ui.statusbar.showMessage("Leituras sendo realizadas, dados não podem ser salvos.")
            return
        if self.driver.dman.globalctreadings == 0:
            self.ui.statusbar.showMessage("Nada a ser salvo...")
            return
        filename = QFileDialog.getSaveFileName(self, "Salvar Arquivo", getenv('HOME'), 'csv (*.csv)')
        if (filename[0] != ''):
            try:
                self.driver.dman.saveFile(filename[0])
                self.flagsaved = True
            except Exception as err:
                QMessageBox.question(self.app, "Erro!", str(err), QMessageBox.Ok)
        

    
    
    def bInit(self):
        if self.driver is not None:
            self.flagsaved = False
            if self.driver.flagrunning:
                self.driver.paraLeituras()
                for comp in self.disabledWhenRunning:
                    comp.setEnabled(True)                 
                # self.ui.spinCtrlManual.setEnabled(True)
                # self.ui.spinSetPoint.setEnabled(True)
                for val in self.valsT+self.valsE:
                    val.setEnabled(True)
            else:
                for comp in self.disabledWhenRunning:
                    comp.setEnabled(False)
                self.ui.comboAmostragem.setEnabled(False)
                self.enablemap = []
                for val,chk in zip(self.valsT+self.valsE,self.checksT+self.checksE):
                    self.enablemap.append(chk.isChecked())
                    val.setEnabled(chk.isChecked())
                self.ui.spinSetPoint.setEnabled(self.ui.checkCtrlAuto.isChecked())
                self.ui.spinCtrlManual.setEnabled(self.ui.checkCtrlManual.isChecked())
                self.configCtrl()
                self.setPointChanged()
                self.manualCtrlLevelChanged()                
                amostr = self.ui.comboAmostragem.currentIndex() + 1
                self.mainplot.plotSetup(amostr,self.enablemap,self.driver.dman)            
                self.driver.iniciaLeituras(amostr,self.enablemap,self.ui.comboTipoTermopar.currentText())


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
        # self.driver.dman.resetData()
        self.driver.limpaLeituras()
        self.mainplot.setDataman(self.driver.dman)
        self.mainplot.updateFig()
        self.ui.comboAmostragem.setEnabled(True)


    def populatePorts(self):
        self.ui.comboPorta.clear()
        ports = self.driver.listPorts()
        for port, desc, hwid in sorted(ports):
            # print("{}: {} [{}]".format(port, desc, hwid))
            # if port == self.Port:
            #     port = f">{port}"
            self.ui.comboPorta.addItem(port)
            # self.ui.menuSelecionar_Porta.addAction(port)
        # for acc in self.ui.menuSelecionar_Porta.actions():
        #     self.mapper.setMapping(acc, acc.text())
        #     acc.triggered.connect(self.mapper.map)


    def setDriver(self,driver : driverhardware):
        self.driver = driver
        self.populatePorts()
        self.driver.newdata.connect(self.updateGUI)
    

    # def setCurTime(self,time):
    #     self.ui.timeLabel.setText(f'{time} s')

    # def setValText(self,text,idx):
    #     if idx <= 8:
    #         self.valsT[idx].setText(text)
    #     else:
    #         self.valsE[idx-8].setText(text)
    
    # def setPowerText(self,text):
    #     self.valPower.setText(text)

    # def setJunta(self,text):
    #     self.ui.valRef.setText(text)

    def changePlotWindow(self):
        newwindow = self.ui.spinJanela.value()
        self.mainplot.setTimeWindow(newwindow)
        if not self.driver.flagrunning:
            self.mainplot.updateFig()


    def updateGUI(self,mydict):       
        self.ui.timeLabel.setText(f'{mydict["readtime"]} s')      
        self.ui.valRef.setText(mydict["junta"])
        for k in range(8):
            if self.enablemap[k]:
                self.valsT[k].setText(mydict[f"termop{k}"])
        self.valPower.setText(mydict["power"])
        self.mainplot.updateFig()
        QtCore.QCoreApplication.processEvents()


    def ctrlAutoChanged(self):
        if self.ui.checkCtrlAuto.isChecked():            
            self.ui.checkCtrlManual.setChecked(False)
            self.ui.spinCtrlManual.setEnabled(False)
            self.ui.spinSetPoint.setEnabled(True)
            if self.driver is not None:
                self.driver.changeCtrlType('Auto')
                self.setPointChanged()
        else:
            self.ui.spinSetPoint.setEnabled(False)
            if (not self.ui.checkCtrlManual.isChecked()) and (self.driver is not None):
                self.driver.changeCtrlType('Off')
        
    def ctrlManualChanged(self):
        if self.ui.checkCtrlManual.isChecked():
            self.ui.checkCtrlAuto.setChecked(False)
            self.ui.spinSetPoint.setEnabled(False)
            self.ui.spinCtrlManual.setEnabled(True)
            if self.driver is not None:
                self.driver.changeCtrlType('Manual')
                self.manualCtrlLevelChanged()
        else:
            self.ui.spinCtrlManual.setEnabled(False)
            if (not self.ui.checkCtrlAuto.isChecked()) and (self.driver is not None):
                self.driver.changeCtrlType('Off')

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
        settings.setValue("MainPlotCfg",self.mainplot.getConfigString())


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
        
        if settings.value("MainPlotCfg") is not None:
            self.mainplot.parseConfigString(settings.value("MainPlotCfg"))
            self.ui.spinJanela.setValue(self.mainplot.janelax[0])

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
 
