# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:54:14 2015

@author: Raul
"""
from GameBehavior import GameBehavior
from PyQt4 import QtGui, QtCore
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = GameBehavior()
    sys.exit(app.exec_())