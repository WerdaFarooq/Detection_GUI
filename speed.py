# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'speed.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow3(object):
    def setupUi(self, OtherWindow3):
        OtherWindow3.setObjectName("OtherWindow3")
        OtherWindow3.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OtherWindow3)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(133, 40, 511, 41))
        self.textEdit.setObjectName("textEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(99, 139, 591, 371))
        self.frame.setStyleSheet("background-color: rgb(206, 206, 206);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        OtherWindow3.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow3)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        OtherWindow3.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow3)
        self.statusbar.setObjectName("statusbar")
        OtherWindow3.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(OtherWindow3)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(OtherWindow3)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(OtherWindow3)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow3)

    def retranslateUi(self, OtherWindow3):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow3.setWindowTitle(_translate("OtherWindow3", "MainWindow"))
        self.textEdit.setHtml(_translate("OtherWindow3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#00007f;\">SPEED ESTIMATION</span></p></body></html>"))
        self.menuFile.setTitle(_translate("OtherWindow3", "File"))
        self.menuOption.setTitle(_translate("OtherWindow3", "Option"))
        self.actionOpen.setText(_translate("OtherWindow3", "Open"))
        self.actionExit.setText(_translate("OtherWindow3", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow3 = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow3()
    ui.setupUi(OtherWindow3)
    OtherWindow3.show()
    sys.exit(app.exec_())
