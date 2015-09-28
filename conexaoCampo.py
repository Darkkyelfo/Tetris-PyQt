# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:36:13 2015

@author: Raul
"""

from campoTetris import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import blocos_rc
import random

class ConexaoCampo(QtGui.QMainWindow,Ui_MainWindow):
    posX=100
    posY=100
    boole=False
    cont=1
    linha = []
    pecas=[]
    def __init__(self,parent=None):
        super(ConexaoCampo, self).__init__(parent)
        self.setupUi(self)
        self.label.move(self.posX,self.posY)  
        self.label.setStyleSheet("image: url(:/blocos/Imagens/%s);"%(self.gerarPeca()))
        #self.pushButton.clicked.connect(self.criarLabel)
        
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
        if(key == QtCore.Qt.Key_Up):#rotaciona a peça
            if((self.peca=="1") or (self.peca=="2")):
                if(self.peca=="1"):
                    self.peca="2"
                    self.label.setStyleSheet("image: url(:/blocos/Imagens/%s);"%(self.peca))
                else:
                    self.peca="1"
                    self.label.setStyleSheet("image: url(:/blocos/Imagens/%s);"%(self.peca))
                    
                                
            
        self.label.move(self.posX,self.posY)
        
        print(self.posY)
        if(self.posY==400):
            self.criarLabel()
    #gera pecas randomicamente
    def gerarPeca(self):
        self.peca=str(random.choice(range(1,8)))
        return self.peca
        
    def criarLabel(self):
        self.pecas.append(self.posX)
        self.pecas.append(self.posY)
        self.pecas.append(self.peca)
        self.linha.append(0)
        index = self.linha.index(self.linha[len(self.linha)-1])
        print(index)
        pos=0
        self.setupUi(self)
        #gambiarra
        for i in self.linha:
            i=QtGui.QLabel(self.centralwidget)
            i.setGeometry(QtCore.QRect(self.pecas[pos],self.pecas[pos+1], 50, 50))
            i.setStyleSheet("image: url(:/blocos/Imagens/%s);"%(self.pecas[pos+2]))
            i.setObjectName("label_%s"%index)
            pos=pos+3
            
        self.label.setStyleSheet("image: url(:/blocos/Imagens/%s);"%(self.gerarPeca()))
        self.posX=100
        self.posY=100        
        self.label.move(self.posX,self.posY)

        



if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = ConexaoCampo()
    av.show()
    sys.exit(app.exec_())
