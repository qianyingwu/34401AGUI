# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Fri May 20 16:52:19 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 792)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.groupBox_5 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_8 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lastMeasurement = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastMeasurement.sizePolicy().hasHeightForWidth())
        self.lastMeasurement.setSizePolicy(sizePolicy)
        self.lastMeasurement.setMaximumSize(QtCore.QSize(312, 29))
        self.lastMeasurement.setReadOnly(True)
        self.lastMeasurement.setObjectName("lastMeasurement")
        self.verticalLayout.addWidget(self.lastMeasurement)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lastMeasureMode = QtGui.QLineEdit(self.groupBox_5)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lastMeasureMode.sizePolicy().hasHeightForWidth())
        self.lastMeasureMode.setSizePolicy(sizePolicy)
        self.lastMeasureMode.setMaximumSize(QtCore.QSize(312, 16777215))
        self.lastMeasureMode.setReadOnly(True)
        self.lastMeasureMode.setObjectName("lastMeasureMode")
        self.horizontalLayout_2.addWidget(self.lastMeasureMode)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.groupBox_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout_8.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem)
        self.groupBox_6 = QtGui.QGroupBox(self.centralWidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_9 = QtGui.QGridLayout(self.groupBox_6)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label = QtGui.QLabel(self.groupBox_6)
        self.label.setObjectName("label")
        self.horizontalLayout_14.addWidget(self.label)
        self.quickMeasureMode = QtGui.QComboBox(self.groupBox_6)
        self.quickMeasureMode.setObjectName("quickMeasureMode")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.quickMeasureMode.addItem("")
        self.horizontalLayout_14.addWidget(self.quickMeasureMode)
        self.verticalLayout_10.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_11 = QtGui.QLabel(self.groupBox_6)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_15.addWidget(self.label_11)
        self.quickResOverload = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickResOverload.sizePolicy().hasHeightForWidth())
        self.quickResOverload.setSizePolicy(sizePolicy)
        self.quickResOverload.setMaximumSize(QtCore.QSize(60, 16777215))
        self.quickResOverload.setObjectName("quickResOverload")
        self.horizontalLayout_15.addWidget(self.quickResOverload)
        self.quickResLowerLimit = QtGui.QLineEdit(self.groupBox_6)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quickResLowerLimit.sizePolicy().hasHeightForWidth())
        self.quickResLowerLimit.setSizePolicy(sizePolicy)
        self.quickResLowerLimit.setMaximumSize(QtCore.QSize(80, 16777215))
        self.quickResLowerLimit.setObjectName("quickResLowerLimit")
        self.horizontalLayout_15.addWidget(self.quickResLowerLimit)
        self.quickResHelp = QtGui.QToolButton(self.groupBox_6)
        self.quickResHelp.setObjectName("quickResHelp")
        self.horizontalLayout_15.addWidget(self.quickResHelp)
        self.verticalLayout_10.addLayout(self.horizontalLayout_15)
        self.gridLayout_9.addLayout(self.verticalLayout_10, 0, 0, 1, 1)
        self.quickTakeMeasurement = QtGui.QPushButton(self.groupBox_6)
        self.quickTakeMeasurement.setObjectName("quickTakeMeasurement")
        self.gridLayout_9.addWidget(self.quickTakeMeasurement, 1, 0, 1, 1)
        self.verticalLayout_9.addWidget(self.groupBox_6)
        self.horizontalLayout.addLayout(self.verticalLayout_9)
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_5 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.beepEnable = QtGui.QCheckBox(self.groupBox_3)
        self.beepEnable.setChecked(True)
        self.beepEnable.setObjectName("beepEnable")
        self.gridLayout_5.addWidget(self.beepEnable, 2, 0, 1, 1)
        self.displayEnable = QtGui.QCheckBox(self.groupBox_3)
        self.displayEnable.setChecked(True)
        self.displayEnable.setObjectName("displayEnable")
        self.gridLayout_5.addWidget(self.displayEnable, 1, 0, 1, 1)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.systReset = QtGui.QPushButton(self.groupBox_3)
        self.systReset.setObjectName("systReset")
        self.horizontalLayout_11.addWidget(self.systReset)
        self.verticalLayout_6.addLayout(self.horizontalLayout_11)
        self.gridLayout_5.addLayout(self.verticalLayout_6, 3, 0, 1, 1)
        self.viewErrors = QtGui.QPushButton(self.groupBox_3)
        self.viewErrors.setObjectName("viewErrors")
        self.gridLayout_5.addWidget(self.viewErrors, 4, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 4, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.serialDevice = QtGui.QComboBox(self.groupBox)
        self.serialDevice.setEditable(True)
        self.serialDevice.setObjectName("serialDevice")
        self.horizontalLayout_5.addWidget(self.serialDevice)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.serialBaudRate = QtGui.QComboBox(self.groupBox)
        self.serialBaudRate.setObjectName("serialBaudRate")
        self.serialBaudRate.addItem("")
        self.serialBaudRate.addItem("")
        self.serialBaudRate.addItem("")
        self.serialBaudRate.addItem("")
        self.serialBaudRate.addItem("")
        self.serialBaudRate.addItem("")
        self.horizontalLayout_6.addWidget(self.serialBaudRate)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.serialParity = QtGui.QComboBox(self.groupBox)
        self.serialParity.setObjectName("serialParity")
        self.serialParity.addItem("")
        self.serialParity.addItem("")
        self.serialParity.addItem("")
        self.horizontalLayout_8.addWidget(self.serialParity)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.connectToDevice = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectToDevice.sizePolicy().hasHeightForWidth())
        self.connectToDevice.setSizePolicy(sizePolicy)
        self.connectToDevice.setObjectName("connectToDevice")
        self.gridLayout_3.addWidget(self.connectToDevice, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_6 = QtGui.QGridLayout(self.tab_4)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_4 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_8 = QtGui.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_18.addWidget(self.label_13)
        self.logTrigSource = QtGui.QComboBox(self.groupBox_4)
        self.logTrigSource.setObjectName("logTrigSource")
        self.logTrigSource.addItem("")
        self.logTrigSource.addItem("")
        self.horizontalLayout_18.addWidget(self.logTrigSource)
        self.verticalLayout_8.addLayout(self.horizontalLayout_18)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_11 = QtGui.QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_12 = QtGui.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_9 = QtGui.QLabel(self.groupBox_8)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_12.addWidget(self.label_9)
        spacerItem2 = QtGui.QSpacerItem(43, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem2)
        self.logAutoInterval = QtGui.QSpinBox(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logAutoInterval.sizePolicy().hasHeightForWidth())
        self.logAutoInterval.setSizePolicy(sizePolicy)
        self.logAutoInterval.setMaximum(100000)
        self.logAutoInterval.setObjectName("logAutoInterval")
        self.horizontalLayout_12.addWidget(self.logAutoInterval)
        self.gridLayout_11.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_14 = QtGui.QLabel(self.groupBox_8)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_19.addWidget(self.label_14)
        spacerItem3 = QtGui.QSpacerItem(39, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem3)
        self.logAutoSamplesMax = QtGui.QSpinBox(self.groupBox_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logAutoSamplesMax.sizePolicy().hasHeightForWidth())
        self.logAutoSamplesMax.setSizePolicy(sizePolicy)
        self.logAutoSamplesMax.setMaximum(9999999)
        self.logAutoSamplesMax.setObjectName("logAutoSamplesMax")
        self.horizontalLayout_19.addWidget(self.logAutoSamplesMax)
        self.logAutoSamplesLimit = QtGui.QCheckBox(self.groupBox_8)
        self.logAutoSamplesLimit.setChecked(True)
        self.logAutoSamplesLimit.setObjectName("logAutoSamplesLimit")
        self.horizontalLayout_19.addWidget(self.logAutoSamplesLimit)
        self.gridLayout_11.addLayout(self.horizontalLayout_19, 1, 0, 1, 1)
        self.verticalLayout_8.addWidget(self.groupBox_8)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.logTriggerSampleCount = QtGui.QSpinBox(self.groupBox_4)
        self.logTriggerSampleCount.setMinimum(1)
        self.logTriggerSampleCount.setMaximum(50000)
        self.logTriggerSampleCount.setObjectName("logTriggerSampleCount")
        self.horizontalLayout_13.addWidget(self.logTriggerSampleCount)
        self.verticalLayout_8.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_17.addWidget(self.label_12)
        self.logTriggerSampleDelay = QtGui.QSpinBox(self.groupBox_4)
        self.logTriggerSampleDelay.setMaximum(3600)
        self.logTriggerSampleDelay.setObjectName("logTriggerSampleDelay")
        self.horizontalLayout_17.addWidget(self.logTriggerSampleDelay)
        self.verticalLayout_8.addLayout(self.horizontalLayout_17)
        self.gridLayout_7.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_4)
        self.groupBox_7 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_10 = QtGui.QGridLayout(self.groupBox_7)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_11 = QtGui.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_15 = QtGui.QLabel(self.groupBox_7)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_20.addWidget(self.label_15)
        self.logMeasureMode = QtGui.QComboBox(self.groupBox_7)
        self.logMeasureMode.setObjectName("logMeasureMode")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.logMeasureMode.addItem("")
        self.horizontalLayout_20.addWidget(self.logMeasureMode)
        self.verticalLayout_11.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtGui.QLabel(self.groupBox_7)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        spacerItem4 = QtGui.QSpacerItem(112, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.logResOverload = QtGui.QLineEdit(self.groupBox_7)
        self.logResOverload.setObjectName("logResOverload")
        self.horizontalLayout_10.addWidget(self.logResOverload)
        self.logResLowerLimit = QtGui.QLineEdit(self.groupBox_7)
        self.logResLowerLimit.setObjectName("logResLowerLimit")
        self.horizontalLayout_10.addWidget(self.logResLowerLimit)
        self.logResHelp = QtGui.QToolButton(self.groupBox_7)
        self.logResHelp.setObjectName("logResHelp")
        self.horizontalLayout_10.addWidget(self.logResHelp)
        self.verticalLayout_11.addLayout(self.horizontalLayout_10)
        self.gridLayout_10.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_7)
        self.groupBox_2 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_21.addWidget(self.label_16)
        self.logFilePath = QtGui.QLineEdit(self.groupBox_2)
        self.logFilePath.setObjectName("logFilePath")
        self.horizontalLayout_21.addWidget(self.logFilePath)
        self.logFileBrowse = QtGui.QPushButton(self.groupBox_2)
        self.logFileBrowse.setObjectName("logFileBrowse")
        self.horizontalLayout_21.addWidget(self.logFileBrowse)
        self.verticalLayout_5.addLayout(self.horizontalLayout_21)
        self.logAppend = QtGui.QRadioButton(self.groupBox_2)
        self.logAppend.setChecked(True)
        self.logAppend.setObjectName("logAppend")
        self.verticalLayout_5.addWidget(self.logAppend)
        self.logReplace = QtGui.QRadioButton(self.groupBox_2)
        self.logReplace.setObjectName("logReplace")
        self.verticalLayout_5.addWidget(self.logReplace)
        self.gridLayout_4.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.logStart = QtGui.QPushButton(self.tab_4)
        self.logStart.setObjectName("logStart")
        self.verticalLayout_7.addWidget(self.logStart)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dataNotes = QtGui.QLineEdit(self.tab_4)
        self.dataNotes.setObjectName("dataNotes")
        self.horizontalLayout_3.addWidget(self.dataNotes)
        self.loggingStop = QtGui.QPushButton(self.tab_4)
        self.loggingStop.setObjectName("loggingStop")
        self.horizontalLayout_3.addWidget(self.loggingStop)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.gridLayout_6.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1056, 23))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("MainWindow", "Last Measurement", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Mesuring", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_6.setTitle(QtGui.QApplication.translate("MainWindow", "Quick Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(0, QtGui.QApplication.translate("MainWindow", "DC Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(1, QtGui.QApplication.translate("MainWindow", "DC Current", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(2, QtGui.QApplication.translate("MainWindow", "AC Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(3, QtGui.QApplication.translate("MainWindow", "AC Current", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(4, QtGui.QApplication.translate("MainWindow", "Resistance", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(5, QtGui.QApplication.translate("MainWindow", "4 Wire Resistance", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(6, QtGui.QApplication.translate("MainWindow", "Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(7, QtGui.QApplication.translate("MainWindow", "Period", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(8, QtGui.QApplication.translate("MainWindow", "Continuity", None, QtGui.QApplication.UnicodeUTF8))
        self.quickMeasureMode.setItemText(9, QtGui.QApplication.translate("MainWindow", "Diode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.quickResOverload.setText(QtGui.QApplication.translate("MainWindow", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.quickResLowerLimit.setText(QtGui.QApplication.translate("MainWindow", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.quickResHelp.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.quickTakeMeasurement.setText(QtGui.QApplication.translate("MainWindow", "Take Measurement", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("MainWindow", "System Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.beepEnable.setText(QtGui.QApplication.translate("MainWindow", "Beep On", None, QtGui.QApplication.UnicodeUTF8))
        self.displayEnable.setText(QtGui.QApplication.translate("MainWindow", "Display On", None, QtGui.QApplication.UnicodeUTF8))
        self.systReset.setText(QtGui.QApplication.translate("MainWindow", "Reset", None, QtGui.QApplication.UnicodeUTF8))
        self.viewErrors.setText(QtGui.QApplication.translate("MainWindow", "View Errors...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Serial Interface", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Serial Device", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Baud Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.serialBaudRate.setItemText(0, QtGui.QApplication.translate("MainWindow", "9600", None, QtGui.QApplication.UnicodeUTF8))
        self.serialBaudRate.setItemText(1, QtGui.QApplication.translate("MainWindow", "4800", None, QtGui.QApplication.UnicodeUTF8))
        self.serialBaudRate.setItemText(2, QtGui.QApplication.translate("MainWindow", "2400", None, QtGui.QApplication.UnicodeUTF8))
        self.serialBaudRate.setItemText(3, QtGui.QApplication.translate("MainWindow", "1200", None, QtGui.QApplication.UnicodeUTF8))
        self.serialBaudRate.setItemText(4, QtGui.QApplication.translate("MainWindow", "600", None, QtGui.QApplication.UnicodeUTF8))
        self.serialBaudRate.setItemText(5, QtGui.QApplication.translate("MainWindow", "300", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Parity", None, QtGui.QApplication.UnicodeUTF8))
        self.serialParity.setItemText(0, QtGui.QApplication.translate("MainWindow", "Even", None, QtGui.QApplication.UnicodeUTF8))
        self.serialParity.setItemText(1, QtGui.QApplication.translate("MainWindow", "Odd", None, QtGui.QApplication.UnicodeUTF8))
        self.serialParity.setItemText(2, QtGui.QApplication.translate("MainWindow", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.connectToDevice.setText(QtGui.QApplication.translate("MainWindow", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("MainWindow", "Logging Setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "Tigger Source", None, QtGui.QApplication.UnicodeUTF8))
        self.logTrigSource.setItemText(0, QtGui.QApplication.translate("MainWindow", "Automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.logTrigSource.setItemText(1, QtGui.QApplication.translate("MainWindow", "Manual", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_8.setTitle(QtGui.QApplication.translate("MainWindow", "Automatic", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Auto Trigger Interval (seconds)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Auto Trigger Samples", None, QtGui.QApplication.UnicodeUTF8))
        self.logAutoSamplesLimit.setText(QtGui.QApplication.translate("MainWindow", "No Limit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Samples Per Trigger", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "Sample Delay ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_7.setTitle(QtGui.QApplication.translate("MainWindow", "Measurement Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(0, QtGui.QApplication.translate("MainWindow", "DC Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(1, QtGui.QApplication.translate("MainWindow", "DC Current", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(2, QtGui.QApplication.translate("MainWindow", "AC Voltage", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(3, QtGui.QApplication.translate("MainWindow", "AC Current", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(4, QtGui.QApplication.translate("MainWindow", "Resistance", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(5, QtGui.QApplication.translate("MainWindow", "4 Wire Resistance", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(6, QtGui.QApplication.translate("MainWindow", "Frequency", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(7, QtGui.QApplication.translate("MainWindow", "Period", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(8, QtGui.QApplication.translate("MainWindow", "Continuity", None, QtGui.QApplication.UnicodeUTF8))
        self.logMeasureMode.setItemText(9, QtGui.QApplication.translate("MainWindow", "Diode", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Resolution", None, QtGui.QApplication.UnicodeUTF8))
        self.logResOverload.setText(QtGui.QApplication.translate("MainWindow", "15", None, QtGui.QApplication.UnicodeUTF8))
        self.logResLowerLimit.setText(QtGui.QApplication.translate("MainWindow", "0.1", None, QtGui.QApplication.UnicodeUTF8))
        self.logResHelp.setText(QtGui.QApplication.translate("MainWindow", "?", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("MainWindow", "File Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Log to file", None, QtGui.QApplication.UnicodeUTF8))
        self.logFileBrowse.setText(QtGui.QApplication.translate("MainWindow", "Browse...", None, QtGui.QApplication.UnicodeUTF8))
        self.logAppend.setText(QtGui.QApplication.translate("MainWindow", "Append", None, QtGui.QApplication.UnicodeUTF8))
        self.logReplace.setText(QtGui.QApplication.translate("MainWindow", "Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.logStart.setText(QtGui.QApplication.translate("MainWindow", "Start Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Notes", None, QtGui.QApplication.UnicodeUTF8))
        self.loggingStop.setText(QtGui.QApplication.translate("MainWindow", "Stop Logging", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Logging", None, QtGui.QApplication.UnicodeUTF8))

