# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'congestion.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OtherWindow2(object):
    def setupUi(self, OtherWindow2):
        OtherWindow2.setObjectName("OtherWindow2")
        OtherWindow2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(OtherWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(170, 40, 461, 41))
        self.textEdit.setObjectName("textEdit")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(130, 160, 541, 331))
        self.frame.setStyleSheet("background-color: rgb(211, 211, 211);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(220, 90, 351, 41))
        self.textEdit_2.setObjectName("textEdit_2")
        OtherWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OtherWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuOption.setObjectName("menuOption")
        OtherWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OtherWindow2)
        self.statusbar.setObjectName("statusbar")
        OtherWindow2.setStatusBar(self.statusbar)
        self.actionSelect = QtWidgets.QAction(OtherWindow2)
        self.actionSelect.setObjectName("actionSelect")
        self.actionExit = QtWidgets.QAction(OtherWindow2)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSelect)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuOption.menuAction())

        self.retranslateUi(OtherWindow2)
        QtCore.QMetaObject.connectSlotsByName(OtherWindow2)

    def retranslateUi(self, OtherWindow2):
        _translate = QtCore.QCoreApplication.translate
        OtherWindow2.setWindowTitle(_translate("OtherWindow2", "MainWindow"))
        self.textEdit.setHtml(_translate("OtherWindow2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#00007f;\">TRAFFIC CONGESTION</span></p></body></html>"))
        self.textEdit_2.setHtml(_translate("OtherWindow2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#00007f;\">DENSITY:</span></p></body></html>"))
        self.menuFile.setTitle(_translate("OtherWindow2", "File"))
        self.menuOption.setTitle(_translate("OtherWindow2", "Option"))
        self.actionSelect.setText(_translate("OtherWindow2", "Select"))
        self.actionExit.setText(_translate("OtherWindow2", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OtherWindow2 = QtWidgets.QMainWindow()
    ui = Ui_OtherWindow2()
    ui.setupUi(OtherWindow2)
    OtherWindow2.show()
    sys.exit(app.exec_())
