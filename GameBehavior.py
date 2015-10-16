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
    velocidadeQueda=300#tempo que leva para a peça se mover(dado em milésimos)
    
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
        
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.time)
        timer.start(self.velocidadeQueda)#inicia a função time
        
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
            self.pecaAtual.tipo=2
            
        self.update()#Atualiza a GUI
    
    #Responsavel por fazer a peça cair a cada 1s
    def time(self):
        self.desenhoPeca.descerPeca()
        posX=self.desenhoPeca.posX
        posY =self.desenhoPeca.posY
        matriz=self.pecaAtual.getPeca()
        cor = self.desenhoPeca.cor
        #caso a peça toque o limite do campo
        #gera uma nova peca
        if(self.desenhoPeca.tocouY):
            #preenche os quadrados do campo
            for i in range(0,4):
                self.postoIndex(posX+(23*matriz[i][0]),posY+(22*matriz[i][1]),cor)
            self.criarNovaPeca()
        else:#thecho responsavel por dectecar a colisão entre peças

            for i in range(0,4):#verifica se algum dos quadrados que compoem a peça colidiu
                if(self.detectarColisao(posX+(23*matriz[i][0]),posY+(22*matriz[i][1]))):
                    for i in range(0,4):#preenche os quadrados do campo
                        self.postoIndex(posX+(23*matriz[i][0]),posY+(22*matriz[i][1]),cor)
                    self.criarNovaPeca()
                    break
        self.update()
    
    #cria uma nova peça
    def criarNovaPeca(self):
        self.pecaAtual=Peca()
        self.pecaAtual.gerarPeca()
        self.desenhoPeca.receberPeca(self.pecaAtual)
        self.desenhoPeca.desenharNovaPeca()
        self.desenhoPeca.tocouY=False
        
    #responsavel por marcar na matriz os locais onde há peças
    #converte a posição(x,y) em índices da matriz do campo 
    def postoIndex(self,posX,posY,cor):
        indexX=self.posXtoIndex(posX)
        indexY=self.posYtoIndex(posY)
        if(self.desenhoPeca.campo[indexY][indexX]==0):
            self.desenhoPeca.campo[indexY][indexX]=[posX,posY,cor]
            
    def posXtoIndex(self,posX):
        return posX/23 -1
    
    def posYtoIndex(self,posY):
        return posY/22 -1 
    
    #indica se a peça colidiu com outra peça no eixo y.    
    def detectarColisao(self,posX,posY):
        temColisao = False
        try:
            if(self.desenhoPeca.campo[self.posYtoIndex(posY)+1][self.posXtoIndex(posX)]!=0):
                temColisao = True
        except(IndexError):
            temColisao = False
        return temColisao
        
            
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = GameBehavior()
    sys.exit(app.exec_())
    