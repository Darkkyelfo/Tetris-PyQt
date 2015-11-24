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
    a.genes=[0.55364585,  0.16925342,  0.5622487,  0.7155643,  0.026904278, 0.18746862,  0.13597304  ]
    av=IA(a)#descomente pra deixar a IA jogar e comente "av=GameBehavior
    sys.exit(app.exec_())