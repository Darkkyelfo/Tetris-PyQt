# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:39:49 2015

@author: Raul
"""
#Essa classe é resposanvel pelo comportamento do jogo
#Nela que acontece a conexão com a GUI
#Também onde estão escritas as regras do jogo

from campoTetris import Ui_MainWindow
from PyQt4 import QtGui, QtCore
from DesenhoPeca import DesenhoPeca
from Peca import Peca


class GameBehavior(QtGui.QMainWindow,Ui_MainWindow):
    #atributos da classe
    desenhoPeca=None
    pecaAtual=None
    campo=[]
    
    def __init__(self,parent=None):
        super(GameBehavior, self).__init__(parent)
        self.setupUi(self)
        #cria tela onde vão ser desenhadas as peças
        self.desenhoPeca = DesenhoPeca(self.centralwidget,self.width(),self.height())
        #gera a primeira peca
        self.pecaAtual=Peca()
        self.pecaAtual.gerarPeca()            
        #desenha a peça na tela
        self.desenhoPeca.receberPeca(self.pecaAtual)
        self.widget_2=self.desenhoPeca
        self.show()
        
    #funçao que receve eventos do teclado
    def keyPressEvent(self, event):
        key = event.key()
        if(key == QtCore.Qt.Key_Right):#mover para a direira
            self.desenhoPeca.moverDir()
        if(key ==QtCore.Qt.Key_Left):#mover para a esquerda 
            self.desenhoPeca.moverEsq()
        if(key ==QtCore.Qt.Key_Down):
            self.desenhoPeca.descerPeca()
        if(key ==QtCore.Qt.Key_Up):#rotacionar peça ao apertar up
            self.pecaAtual.rotacionar()
        if(key ==QtCore.Qt.Key_Space):#faz a peça cair rápido
            self.desenhoPeca.soltarPeca()
        if(key==QtCore.Qt.Key_G):
            self.pecaAtual.gerarPeca()
            
        self.update()#Atualiza a GUI
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = GameBehavior()
    #av.show()
    sys.exit(app.exec_())
    