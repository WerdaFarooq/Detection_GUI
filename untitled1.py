# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled1.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from detection import Ui_OtherWindow
from counting import Ui_OtherWindow1
from congestion import Ui_OtherWindow2
from speed import Ui_OtherWindow3
from video_player import VideoWindow

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow()
        self.ui.setupUi(self.window)
##        MainWindow.hide()
        self.window.show()

    def openVideoPlayer(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = VideoWindow()
        self.ui.setupUi(self.window)
##        MainWindow.hide()
        self.window.show()
        
    def openWindow1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow1()
        self.ui.setupUi(self.window)
##        MainWindow.hide()
        self.window.show()
        
    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow2()
        self.ui.setupUi(self.window)
##        MainWindow.hide()
        self.window.show()
        
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OtherWindow3()
        self.ui.setupUi(self.window)
##        MainWindow.hide()
        self.window.show()
        
    def close(self):
            QCoreApplication.instance().quit()
        

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(847, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open1.setGeometry(QtCore.QRect(310, 190, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open1.setFont(font)
        self.btn_open1.setStyleSheet("background-color: rgb(210, 249, 255);")
        self.btn_open1.setObjectName("btn_open1")
        
        self.btn_open1.clicked.connect(self.openWindow1)

        self.btn_open_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_3.setGeometry(QtCore.QRect(310, 310, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open_3.setFont(font)
        self.btn_open_3.setStyleSheet("background-color: rgb(210, 249, 255);")
        self.btn_open_3.setObjectName("btn_open_3")

        self.btn_open_3.clicked.connect(self.openWindow3)
        
        self.btn_open2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open2.setGeometry(QtCore.QRect(310, 250, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open2.setFont(font)
        self.btn_open2.setStyleSheet("background-color: rgb(210, 249, 255);\n"
"")
        self.btn_open2.setObjectName("btn_open2")

        self.btn_open2.clicked.connect(self.openWindow2)
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(310, 430, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(210, 249, 255);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.close)
        
        self.btn_open4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open4.setGeometry(QtCore.QRect(310, 370, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open4.setFont(font)
        self.btn_open4.setStyleSheet("background-color: rgb(210, 249, 255);")
        self.btn_open4.setObjectName("btn_open4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 40, 621, 61))
        self.textEdit.setObjectName("textEdit")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(310, 130, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btn_open.setFont(font)
        self.btn_open.setStyleSheet("background-color: rgb(210, 249, 255);")
        self.btn_open.setObjectName("btn_open")
        
        #self.btn_open.clicked.connect(self.openVideoPlayer)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 847, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFormat = QtWidgets.QAction(MainWindow)
        self.actionFormat.setObjectName("actionFormat")
        self.actionOpen_2 = QtWidgets.QAction(MainWindow)
        self.actionOpen_2.setObjectName("actionOpen_2")
        self.actionExit_2 = QtWidgets.QAction(MainWindow)
        self.actionExit_2.setObjectName("actionExit_2")
        self.actionEdit = QtWidgets.QAction(MainWindow)
        self.actionEdit.setObjectName("actionEdit")
        self.menuFile.addAction(self.actionOpen_2)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit_2)
        self.menuOption.addAction(self.actionFormat)
        self.menuOption.addSeparator()
        self.menuOption.addAction(self.actionEdit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_open1.setText(_translate("MainWindow", "2.VEHICLE COUNTING"))
        self.btn_open_3.setText(_translate("MainWindow", "4.SPEED ESTIMATION"))
        self.btn_open2.setText(_translate("MainWindow", "3.TRAFFIC CONGESTION"))
        self.pushButton_5.setText(_translate("MainWindow", "6.EXIT"))
        self.btn_open4.setText(_translate("MainWindow", "5.TRAFFIC VIOLATION"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#00007f;\">VIDEO SURVEILLIENCE BASED TRAFFIC MANAGEMENT SYSTEM</span></p></body></html>"))
        self.btn_open.setText(_translate("MainWindow", "1. DETECTIONS"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuOption.setTitle(_translate("MainWindow", "Option"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionFormat.setText(_translate("MainWindow", "Format"))
        self.actionOpen_2.setText(_translate("MainWindow", "Open"))
        self.actionExit_2.setText(_translate("MainWindow", "Exit"))
        self.actionEdit.setText(_translate("MainWindow", "Edit"))
        self.btn_open.clicked.connect(self.openVideoPlayer)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
