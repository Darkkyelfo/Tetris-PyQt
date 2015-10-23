# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'campoTetris.ui'
#
# Created: Fri Oct 23 19:46:14 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(338, 483)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = QtGui.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 229, 483))
        self.widget.setStyleSheet(_fromUtf8("background-image: url(:/GRid/Imagens/1-3grid.png);"))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = QtGui.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 229, 483))
        self.widget_2.setStyleSheet(_fromUtf8(""))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.score = QtGui.QLCDNumber(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(230, 40, 101, 41))
        self.score.setObjectName(_fromUtf8("score"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 10, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "PyQtTetris", None))
        self.label.setText(_translate("MainWindow", "SCORE", None))

import blocos_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

