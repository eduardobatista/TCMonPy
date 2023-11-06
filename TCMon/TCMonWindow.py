# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TCMon.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1076, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionSalvar_Dados = QAction(MainWindow)
        self.actionSalvar_Dados.setObjectName(u"actionSalvar_Dados")
        self.actionPorta_Serial = QAction(MainWindow)
        self.actionPorta_Serial.setObjectName(u"actionPorta_Serial")
        self.actionCOM1 = QAction(MainWindow)
        self.actionCOM1.setObjectName(u"actionCOM1")
        self.actionCOM2 = QAction(MainWindow)
        self.actionCOM2.setObjectName(u"actionCOM2")
        self.actionCOM3 = QAction(MainWindow)
        self.actionCOM3.setObjectName(u"actionCOM3")
        self.actionCOM4 = QAction(MainWindow)
        self.actionCOM4.setObjectName(u"actionCOM4")
        self.actionCOM5 = QAction(MainWindow)
        self.actionCOM5.setObjectName(u"actionCOM5")
        self.actionCOM6 = QAction(MainWindow)
        self.actionCOM6.setObjectName(u"actionCOM6")
        self.actionCOM7 = QAction(MainWindow)
        self.actionCOM7.setObjectName(u"actionCOM7")
        self.actionCOM8 = QAction(MainWindow)
        self.actionCOM8.setObjectName(u"actionCOM8")
        self.actionCOM9 = QAction(MainWindow)
        self.actionCOM9.setObjectName(u"actionCOM9")
        self.actionCOM10 = QAction(MainWindow)
        self.actionCOM10.setObjectName(u"actionCOM10")
        self.actionCOM11 = QAction(MainWindow)
        self.actionCOM11.setObjectName(u"actionCOM11")
        self.actionCOM12 = QAction(MainWindow)
        self.actionCOM12.setObjectName(u"actionCOM12")
        self.action1_s = QAction(MainWindow)
        self.action1_s.setObjectName(u"action1_s")
        self.action2_s = QAction(MainWindow)
        self.action2_s.setObjectName(u"action2_s")
        self.action3_s = QAction(MainWindow)
        self.action3_s.setObjectName(u"action3_s")
        self.action4_s = QAction(MainWindow)
        self.action4_s.setObjectName(u"action4_s")
        self.action5_s = QAction(MainWindow)
        self.action5_s.setObjectName(u"action5_s")
        self.action6_s = QAction(MainWindow)
        self.action6_s.setObjectName(u"action6_s")
        self.action7_s = QAction(MainWindow)
        self.action7_s.setObjectName(u"action7_s")
        self.action8_s = QAction(MainWindow)
        self.action8_s.setObjectName(u"action8_s")
        self.action9_s = QAction(MainWindow)
        self.action9_s.setObjectName(u"action9_s")
        self.action10_s = QAction(MainWindow)
        self.action10_s.setObjectName(u"action10_s")
        self.actionAtualizarViaGit = QAction(MainWindow)
        self.actionAtualizarViaGit.setObjectName(u"actionAtualizarViaGit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.Painel = QWidget(self.centralwidget)
        self.Painel.setObjectName(u"Painel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Painel.sizePolicy().hasHeightForWidth())
        self.Painel.setSizePolicy(sizePolicy1)
        self.Painel.setMinimumSize(QSize(200, 0))
        self.gridLayout = QGridLayout(self.Painel)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.groupBox = QGroupBox(self.Painel)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 4)
        self.checkE1 = QCheckBox(self.groupBox)
        self.checkE1.setObjectName(u"checkE1")
        self.checkE1.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.checkE1.sizePolicy().hasHeightForWidth())
        self.checkE1.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.checkE1, 0, 0, 1, 1)

        self.checkE2 = QCheckBox(self.groupBox)
        self.checkE2.setObjectName(u"checkE2")
        self.checkE2.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.checkE2.sizePolicy().hasHeightForWidth())
        self.checkE2.setSizePolicy(sizePolicy2)

        self.gridLayout_4.addWidget(self.checkE2, 2, 0, 1, 1)

        self.valE2 = QLabel(self.groupBox)
        self.valE2.setObjectName(u"valE2")
        self.valE2.setEnabled(False)
        self.valE2.setAutoFillBackground(False)
        self.valE2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valE2.setFrameShape(QFrame.Box)
        self.valE2.setLineWidth(1)
        self.valE2.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.valE2, 0, 1, 1, 1)

        self.valE1 = QLabel(self.groupBox)
        self.valE1.setObjectName(u"valE1")
        self.valE1.setEnabled(False)
        self.valE1.setAutoFillBackground(False)
        self.valE1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valE1.setFrameShape(QFrame.Box)
        self.valE1.setLineWidth(1)
        self.valE1.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.valE1, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox, 11, 0, 1, 2)

        self.groupBox_3 = QGroupBox(self.Painel)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.gridLayout_7 = QGridLayout(self.groupBox_3)
        self.gridLayout_7.setSpacing(2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(2, 2, 2, 4)
        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_7.addWidget(self.label_8, 0, 0, 1, 1)

        self.comboPorta = QComboBox(self.groupBox_3)
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.addItem("")
        self.comboPorta.setObjectName(u"comboPorta")

        self.gridLayout_7.addWidget(self.comboPorta, 0, 1, 1, 1)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_7.addWidget(self.label_9, 1, 0, 1, 1)

        self.comboAmostragem = QComboBox(self.groupBox_3)
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.addItem("")
        self.comboAmostragem.setObjectName(u"comboAmostragem")

        self.gridLayout_7.addWidget(self.comboAmostragem, 1, 1, 1, 1)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_7.addWidget(self.label_10, 2, 0, 1, 1)

        self.comboTipoTermopar = QComboBox(self.groupBox_3)
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.addItem("")
        self.comboTipoTermopar.setObjectName(u"comboTipoTermopar")

        self.gridLayout_7.addWidget(self.comboTipoTermopar, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 15, 0, 1, 2)

        self.grupoControle = QGroupBox(self.Painel)
        self.grupoControle.setObjectName(u"grupoControle")
        self.grupoControle.setAlignment(Qt.AlignCenter)
        self.grupoControle.setFlat(False)
        self.gridLayout_6 = QGridLayout(self.grupoControle)
        self.gridLayout_6.setSpacing(2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 4)
        self.spinCtrlManual = QSpinBox(self.grupoControle)
        self.spinCtrlManual.setObjectName(u"spinCtrlManual")
        self.spinCtrlManual.setMaximum(100)

        self.gridLayout_6.addWidget(self.spinCtrlManual, 1, 1, 1, 1)

        self.valPower = QLabel(self.grupoControle)
        self.valPower.setObjectName(u"valPower")
        self.valPower.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valPower.setFrameShape(QFrame.Box)
        self.valPower.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.valPower, 4, 0, 1, 1)

        self.checkCtrlAuto = QCheckBox(self.grupoControle)
        self.checkCtrlAuto.setObjectName(u"checkCtrlAuto")

        self.gridLayout_6.addWidget(self.checkCtrlAuto, 2, 0, 1, 1)

        self.comboTermoparCtrl = QComboBox(self.grupoControle)
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.addItem("")
        self.comboTermoparCtrl.setObjectName(u"comboTermoparCtrl")

        self.gridLayout_6.addWidget(self.comboTermoparCtrl, 3, 0, 1, 1)

        self.checkCtrlManual = QCheckBox(self.grupoControle)
        self.checkCtrlManual.setObjectName(u"checkCtrlManual")

        self.gridLayout_6.addWidget(self.checkCtrlManual, 1, 0, 1, 1)

        self.widget_3 = QWidget(self.grupoControle)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy2.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy2)
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setSpacing(2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.spinSetPoint = QDoubleSpinBox(self.widget_3)
        self.spinSetPoint.setObjectName(u"spinSetPoint")
        self.spinSetPoint.setDecimals(0)

        self.gridLayout_2.addWidget(self.spinSetPoint, 0, 1, 1, 2)

        self.label_2 = QLabel(self.widget_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_2, 1, 1, 1, 1)

        self.spinKp = QDoubleSpinBox(self.widget_3)
        self.spinKp.setObjectName(u"spinKp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.spinKp.sizePolicy().hasHeightForWidth())
        self.spinKp.setSizePolicy(sizePolicy4)
        self.spinKp.setMinimum(-1000.000000000000000)
        self.spinKp.setMaximum(1000.000000000000000)
        self.spinKp.setValue(1.000000000000000)

        self.gridLayout_2.addWidget(self.spinKp, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.spinKi = QDoubleSpinBox(self.widget_3)
        self.spinKi.setObjectName(u"spinKi")
        sizePolicy2.setHeightForWidth(self.spinKi.sizePolicy().hasHeightForWidth())
        self.spinKi.setSizePolicy(sizePolicy2)
        self.spinKi.setMinimum(-1000.000000000000000)
        self.spinKi.setMaximum(1000.000000000000000)

        self.gridLayout_2.addWidget(self.spinKi, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        sizePolicy3.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy3)

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.spinKd = QDoubleSpinBox(self.widget_3)
        self.spinKd.setObjectName(u"spinKd")
        sizePolicy2.setHeightForWidth(self.spinKd.sizePolicy().hasHeightForWidth())
        self.spinKd.setSizePolicy(sizePolicy2)
        self.spinKd.setMinimum(-1000.000000000000000)
        self.spinKd.setMaximum(1000.000000000000000)
        self.spinKd.setValue(0.000000000000000)

        self.gridLayout_2.addWidget(self.spinKd, 3, 2, 1, 1)

        self.line_3 = QFrame(self.widget_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.VLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 0, 0, 4, 1)


        self.gridLayout_6.addWidget(self.widget_3, 2, 1, 4, 1)


        self.gridLayout.addWidget(self.grupoControle, 13, 0, 1, 2)

        self.groupBox_2 = QGroupBox(self.Painel)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 4)
        self.valT6 = QLabel(self.groupBox_2)
        self.valT6.setObjectName(u"valT6")
        self.valT6.setAutoFillBackground(False)
        self.valT6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT6.setFrameShape(QFrame.Box)
        self.valT6.setLineWidth(1)
        self.valT6.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT6, 6, 1, 1, 1)

        self.valT7 = QLabel(self.groupBox_2)
        self.valT7.setObjectName(u"valT7")
        self.valT7.setAutoFillBackground(False)
        self.valT7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT7.setFrameShape(QFrame.Box)
        self.valT7.setLineWidth(1)
        self.valT7.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT7, 7, 1, 1, 1)

        self.checkT7 = QCheckBox(self.groupBox_2)
        self.checkT7.setObjectName(u"checkT7")
        sizePolicy2.setHeightForWidth(self.checkT7.sizePolicy().hasHeightForWidth())
        self.checkT7.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT7, 7, 0, 1, 1)

        self.valT8 = QLabel(self.groupBox_2)
        self.valT8.setObjectName(u"valT8")
        self.valT8.setAutoFillBackground(False)
        self.valT8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT8.setFrameShape(QFrame.Box)
        self.valT8.setLineWidth(1)
        self.valT8.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT8, 8, 1, 1, 1)

        self.checkT8 = QCheckBox(self.groupBox_2)
        self.checkT8.setObjectName(u"checkT8")
        sizePolicy2.setHeightForWidth(self.checkT8.sizePolicy().hasHeightForWidth())
        self.checkT8.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT8, 8, 0, 1, 1)

        self.valT2 = QLabel(self.groupBox_2)
        self.valT2.setObjectName(u"valT2")
        self.valT2.setAutoFillBackground(False)
        self.valT2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT2.setFrameShape(QFrame.Box)
        self.valT2.setLineWidth(1)
        self.valT2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT2, 2, 1, 1, 1)

        self.valT3 = QLabel(self.groupBox_2)
        self.valT3.setObjectName(u"valT3")
        self.valT3.setAutoFillBackground(False)
        self.valT3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT3.setFrameShape(QFrame.Box)
        self.valT3.setLineWidth(1)
        self.valT3.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT3, 3, 1, 1, 1)

        self.checkT4 = QCheckBox(self.groupBox_2)
        self.checkT4.setObjectName(u"checkT4")
        sizePolicy2.setHeightForWidth(self.checkT4.sizePolicy().hasHeightForWidth())
        self.checkT4.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT4, 4, 0, 1, 1)

        self.checkT3 = QCheckBox(self.groupBox_2)
        self.checkT3.setObjectName(u"checkT3")
        sizePolicy2.setHeightForWidth(self.checkT3.sizePolicy().hasHeightForWidth())
        self.checkT3.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT3, 3, 0, 1, 1)

        self.checkT1 = QCheckBox(self.groupBox_2)
        self.checkT1.setObjectName(u"checkT1")
        sizePolicy2.setHeightForWidth(self.checkT1.sizePolicy().hasHeightForWidth())
        self.checkT1.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT1, 1, 0, 1, 1)

        self.valT4 = QLabel(self.groupBox_2)
        self.valT4.setObjectName(u"valT4")
        self.valT4.setAutoFillBackground(False)
        self.valT4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT4.setFrameShape(QFrame.Box)
        self.valT4.setLineWidth(1)
        self.valT4.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT4, 4, 1, 1, 1)

        self.valT1 = QLabel(self.groupBox_2)
        self.valT1.setObjectName(u"valT1")
        self.valT1.setAutoFillBackground(False)
        self.valT1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT1.setFrameShape(QFrame.Box)
        self.valT1.setLineWidth(1)
        self.valT1.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT1, 1, 1, 1, 1)

        self.checkT2 = QCheckBox(self.groupBox_2)
        self.checkT2.setObjectName(u"checkT2")
        sizePolicy2.setHeightForWidth(self.checkT2.sizePolicy().hasHeightForWidth())
        self.checkT2.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT2, 2, 0, 1, 1)

        self.checkT5 = QCheckBox(self.groupBox_2)
        self.checkT5.setObjectName(u"checkT5")
        sizePolicy2.setHeightForWidth(self.checkT5.sizePolicy().hasHeightForWidth())
        self.checkT5.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT5, 5, 0, 1, 1)

        self.valT5 = QLabel(self.groupBox_2)
        self.valT5.setObjectName(u"valT5")
        self.valT5.setAutoFillBackground(False)
        self.valT5.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valT5.setFrameShape(QFrame.Box)
        self.valT5.setLineWidth(1)
        self.valT5.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valT5, 5, 1, 1, 1)

        self.checkT6 = QCheckBox(self.groupBox_2)
        self.checkT6.setObjectName(u"checkT6")
        sizePolicy2.setHeightForWidth(self.checkT6.sizePolicy().hasHeightForWidth())
        self.checkT6.setSizePolicy(sizePolicy2)

        self.gridLayout_5.addWidget(self.checkT6, 6, 0, 1, 1)

        self.label_11 = QLabel(self.groupBox_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1)

        self.valRef = QLabel(self.groupBox_2)
        self.valRef.setObjectName(u"valRef")
        self.valRef.setAutoFillBackground(False)
        self.valRef.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.valRef.setFrameShape(QFrame.Box)
        self.valRef.setLineWidth(1)
        self.valRef.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.valRef, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 2, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 24, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 14, 0, 1, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 12, 0, 1, 2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 3, 0, 1, 2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 0, 0, 1, 2)


        self.horizontalLayout.addWidget(self.Painel)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(3, 3, 3, 3)
        self.plotWidget = QWidget(self.widget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidgetLayout = QVBoxLayout(self.plotWidget)
        self.plotWidgetLayout.setSpacing(0)
        self.plotWidgetLayout.setObjectName(u"plotWidgetLayout")
        self.plotWidgetLayout.setContentsMargins(2, 3, 2, 2)

        self.gridLayout_3.addWidget(self.plotWidget, 1, 0, 1, 1)

        self.bLimpar = QPushButton(self.widget)
        self.bLimpar.setObjectName(u"bLimpar")

        self.gridLayout_3.addWidget(self.bLimpar, 4, 0, 1, 1)

        self.timeLabel = QLabel(self.widget)
        self.timeLabel.setObjectName(u"timeLabel")
        sizePolicy2.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy2)
        self.timeLabel.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.timeLabel.setFont(font)
        self.timeLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.timeLabel.setFrameShape(QFrame.Box)
        self.timeLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.timeLabel, 0, 0, 1, 1)

        self.bIniciar = QPushButton(self.widget)
        self.bIniciar.setObjectName(u"bIniciar")

        self.gridLayout_3.addWidget(self.bIniciar, 3, 0, 1, 1)

        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.bPageDown = QPushButton(self.widget_2)
        self.bPageDown.setObjectName(u"bPageDown")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.bPageDown.sizePolicy().hasHeightForWidth())
        self.bPageDown.setSizePolicy(sizePolicy5)
        font1 = QFont()
        font1.setPointSize(7)
        font1.setBold(True)
        self.bPageDown.setFont(font1)

        self.horizontalLayout_2.addWidget(self.bPageDown)

        self.spinJanela = QSpinBox(self.widget_2)
        self.spinJanela.setObjectName(u"spinJanela")
        self.spinJanela.setAlignment(Qt.AlignCenter)
        self.spinJanela.setMinimum(10)
        self.spinJanela.setMaximum(1200)
        self.spinJanela.setSingleStep(10)
        self.spinJanela.setValue(120)

        self.horizontalLayout_2.addWidget(self.spinJanela)

        self.bPageUp = QPushButton(self.widget_2)
        self.bPageUp.setObjectName(u"bPageUp")
        self.bPageUp.setFont(font1)

        self.horizontalLayout_2.addWidget(self.bPageUp)


        self.gridLayout_3.addWidget(self.widget_2, 2, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1076, 21))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionSalvar_Dados)
        self.menuMenu.addAction(self.actionAtualizarViaGit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TCMonPy v0.2", None))
        self.actionSalvar_Dados.setText(QCoreApplication.translate("MainWindow", u"Salvar Dados...", None))
        self.actionPorta_Serial.setText(QCoreApplication.translate("MainWindow", u"Porta Serial", None))
        self.actionCOM1.setText(QCoreApplication.translate("MainWindow", u"COM1", None))
        self.actionCOM2.setText(QCoreApplication.translate("MainWindow", u" COM2", None))
        self.actionCOM3.setText(QCoreApplication.translate("MainWindow", u" COM3", None))
        self.actionCOM4.setText(QCoreApplication.translate("MainWindow", u" COM4", None))
        self.actionCOM5.setText(QCoreApplication.translate("MainWindow", u"COM5", None))
        self.actionCOM6.setText(QCoreApplication.translate("MainWindow", u"COM6", None))
        self.actionCOM7.setText(QCoreApplication.translate("MainWindow", u"COM7", None))
        self.actionCOM8.setText(QCoreApplication.translate("MainWindow", u"COM8", None))
        self.actionCOM9.setText(QCoreApplication.translate("MainWindow", u"COM9", None))
        self.actionCOM10.setText(QCoreApplication.translate("MainWindow", u"COM10", None))
        self.actionCOM11.setText(QCoreApplication.translate("MainWindow", u"COM11", None))
        self.actionCOM12.setText(QCoreApplication.translate("MainWindow", u"COM12", None))
        self.action1_s.setText(QCoreApplication.translate("MainWindow", u"1 s", None))
        self.action2_s.setText(QCoreApplication.translate("MainWindow", u"2 s ", None))
        self.action3_s.setText(QCoreApplication.translate("MainWindow", u"3 s", None))
        self.action4_s.setText(QCoreApplication.translate("MainWindow", u"4 s", None))
        self.action5_s.setText(QCoreApplication.translate("MainWindow", u"5 s", None))
        self.action6_s.setText(QCoreApplication.translate("MainWindow", u"6 s", None))
        self.action7_s.setText(QCoreApplication.translate("MainWindow", u"7 s", None))
        self.action8_s.setText(QCoreApplication.translate("MainWindow", u"8 s", None))
        self.action9_s.setText(QCoreApplication.translate("MainWindow", u"9 s", None))
        self.action10_s.setText(QCoreApplication.translate("MainWindow", u"10 s", None))
        self.actionAtualizarViaGit.setText(QCoreApplication.translate("MainWindow", u"Atualizar Software via Github...", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Entradas Auxiliares", None))
        self.checkE1.setText(QCoreApplication.translate("MainWindow", u"Entrada 1", None))
        self.checkE2.setText(QCoreApplication.translate("MainWindow", u"Entrada 2", None))
        self.valE2.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.valE1.setText(QCoreApplication.translate("MainWindow", u"0.0 V", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Porta:", None))
        self.comboPorta.setItemText(0, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboPorta.setItemText(1, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.comboPorta.setItemText(2, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.comboPorta.setItemText(3, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.comboPorta.setItemText(4, QCoreApplication.translate("MainWindow", u"COM5", None))
        self.comboPorta.setItemText(5, QCoreApplication.translate("MainWindow", u"COM6", None))
        self.comboPorta.setItemText(6, QCoreApplication.translate("MainWindow", u"COM7", None))
        self.comboPorta.setItemText(7, QCoreApplication.translate("MainWindow", u"COM8", None))
        self.comboPorta.setItemText(8, QCoreApplication.translate("MainWindow", u"COM9", None))
        self.comboPorta.setItemText(9, QCoreApplication.translate("MainWindow", u"COM10", None))
        self.comboPorta.setItemText(10, QCoreApplication.translate("MainWindow", u"COM11", None))
        self.comboPorta.setItemText(11, QCoreApplication.translate("MainWindow", u"COM12", None))
        self.comboPorta.setItemText(12, QCoreApplication.translate("MainWindow", u"COM13", None))
        self.comboPorta.setItemText(13, QCoreApplication.translate("MainWindow", u"COM14", None))
        self.comboPorta.setItemText(14, QCoreApplication.translate("MainWindow", u"COM15", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Amostragem:", None))
        self.comboAmostragem.setItemText(0, QCoreApplication.translate("MainWindow", u"1 s", None))
        self.comboAmostragem.setItemText(1, QCoreApplication.translate("MainWindow", u"2 s", None))
        self.comboAmostragem.setItemText(2, QCoreApplication.translate("MainWindow", u"3 s", None))
        self.comboAmostragem.setItemText(3, QCoreApplication.translate("MainWindow", u"4 s", None))
        self.comboAmostragem.setItemText(4, QCoreApplication.translate("MainWindow", u"5 s", None))
        self.comboAmostragem.setItemText(5, QCoreApplication.translate("MainWindow", u"6 s", None))
        self.comboAmostragem.setItemText(6, QCoreApplication.translate("MainWindow", u"7 s", None))
        self.comboAmostragem.setItemText(7, QCoreApplication.translate("MainWindow", u"8 s", None))
        self.comboAmostragem.setItemText(8, QCoreApplication.translate("MainWindow", u"9 s", None))
        self.comboAmostragem.setItemText(9, QCoreApplication.translate("MainWindow", u"10 s", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tipo Termopar:", None))
        self.comboTipoTermopar.setItemText(0, QCoreApplication.translate("MainWindow", u"B", None))
        self.comboTipoTermopar.setItemText(1, QCoreApplication.translate("MainWindow", u"E", None))
        self.comboTipoTermopar.setItemText(2, QCoreApplication.translate("MainWindow", u"J", None))
        self.comboTipoTermopar.setItemText(3, QCoreApplication.translate("MainWindow", u"K", None))
        self.comboTipoTermopar.setItemText(4, QCoreApplication.translate("MainWindow", u"N", None))
        self.comboTipoTermopar.setItemText(5, QCoreApplication.translate("MainWindow", u"R", None))
        self.comboTipoTermopar.setItemText(6, QCoreApplication.translate("MainWindow", u"S", None))
        self.comboTipoTermopar.setItemText(7, QCoreApplication.translate("MainWindow", u"T", None))

        self.comboTipoTermopar.setCurrentText(QCoreApplication.translate("MainWindow", u"B", None))
        self.grupoControle.setTitle(QCoreApplication.translate("MainWindow", u"Controle", None))
        self.spinCtrlManual.setSuffix(QCoreApplication.translate("MainWindow", u"%", None))
        self.valPower.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.checkCtrlAuto.setText(QCoreApplication.translate("MainWindow", u"Autom\u00e1tico", None))
        self.comboTermoparCtrl.setItemText(0, QCoreApplication.translate("MainWindow", u"Termopar 1", None))
        self.comboTermoparCtrl.setItemText(1, QCoreApplication.translate("MainWindow", u"Termopar 2", None))
        self.comboTermoparCtrl.setItemText(2, QCoreApplication.translate("MainWindow", u"Termopar 3", None))
        self.comboTermoparCtrl.setItemText(3, QCoreApplication.translate("MainWindow", u"Termopar 4", None))
        self.comboTermoparCtrl.setItemText(4, QCoreApplication.translate("MainWindow", u"Termopar 5", None))
        self.comboTermoparCtrl.setItemText(5, QCoreApplication.translate("MainWindow", u"Termopar 6", None))
        self.comboTermoparCtrl.setItemText(6, QCoreApplication.translate("MainWindow", u"Termopar 7", None))
        self.comboTermoparCtrl.setItemText(7, QCoreApplication.translate("MainWindow", u"Termopar 8", None))

        self.checkCtrlManual.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.spinSetPoint.setSuffix(QCoreApplication.translate("MainWindow", u" \u00b0C", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Kp:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Ki:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Kd:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Termopares", None))
        self.valT6.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.valT7.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.checkT7.setText(QCoreApplication.translate("MainWindow", u"Termopar 7", None))
        self.valT8.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.checkT8.setText(QCoreApplication.translate("MainWindow", u"Termopar 8", None))
        self.valT2.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.valT3.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.checkT4.setText(QCoreApplication.translate("MainWindow", u"Termopar 4", None))
        self.checkT3.setText(QCoreApplication.translate("MainWindow", u"Termopar 3", None))
        self.checkT1.setText(QCoreApplication.translate("MainWindow", u"Termopar 1", None))
        self.valT4.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.valT1.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.checkT2.setText(QCoreApplication.translate("MainWindow", u"Termopar 2", None))
        self.checkT5.setText(QCoreApplication.translate("MainWindow", u"Termopar 5", None))
        self.valT5.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.checkT6.setText(QCoreApplication.translate("MainWindow", u"Termopar 6", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Junta Fria", None))
        self.valRef.setText(QCoreApplication.translate("MainWindow", u"0.0 \u00b0C", None))
        self.bLimpar.setText(QCoreApplication.translate("MainWindow", u"Limpar Dados", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"0 s", None))
        self.bIniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar/Parar", None))
        self.bPageDown.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.spinJanela.setSuffix(QCoreApplication.translate("MainWindow", u" s", None))
        self.spinJanela.setPrefix("")
        self.bPageUp.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Arquivo", None))
    # retranslateUi

