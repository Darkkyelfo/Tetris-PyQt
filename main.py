# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 19:54:14 2015

@author: Raul
"""
from GameBehavior import GameBehavior
from IA import IA
from Agente import Agente
from PyQt4 import QtGui, QtCore
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
   # av = GameBehavior()# descomente se quiser jogar o tetris e comente "av=IA(a)"
    a=Agente()
    av=IA(a)#descomente pra deixar a IA jogar e comente "av=GameBehavior
    sys.exit(app.exec_())