# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:36:13 2015

@author: Raul
"""

from campoTetris import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import time

class ConexaoCampo(QtGui.QMainWindow,Ui_MainWindow):
    posX=100
    posY=100
    def __init__(self,parent=None):
        super(ConexaoCampo, self).__init__(parent)
        self.setupUi(self)
        self.label.move(self.posX,self.posY)
    
    def mudarTexto(self):
        self.label.move(100,50)
        self.cont=self.cont+1
    
    def keyPressEvent(self, event):
        key = event.key()
        
        if(key == QtCore.Qt.Key_Left):
            self.posX=self.posX-5
            
        if(key == QtCore.Qt.Key_Right):
            self.posX=self.posX+5
            
        if(key == QtCore.Qt.Key_Down):
            self.posY=self.posY+5
            
        self.label.move(self.posX,self.posY)


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = ConexaoCampo()
    av.show()
    sys.exit(app.exec_())
