# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:45:38 2015

@author: Raul
"""
import sys
from PyQt4 import QtGui, QtCore
import random

#Classe responvel por desenhar os tetraminos na GUI
#essa classe é um widget que irá substituir o widget_2 da
#da tela do campo. Foi feita assim,pois, ao chamar o método paintEvent
#direto na tela campo(GameBehavior) as peças ficam por atras do styleSheet. 
class DesenhoPeca(QtGui.QWidget):
    
    x=None#armazena o tamanho da tela (229)
    y=None
    cor=None#armazena a cor da peca
    posicoes=[]
    posicoesY=[]
    #cria uma matriz 20x10 que representa o campo
    campo=[[0,0,0,0,0,0,0,0,0,0] for i in range(20)]
    tamQuadrado=20
    peca=None#Armazena o tipo de peça. Recebe um objeto do tipo peça
    
    #guarda a posição inicial das peças
    posXinicial=3*(tamQuadrado+3)
    posYinicial = 22
    #guarda a posição atual das peças
    posX=posXinicial
    posY=posYinicial
    #delimita o tamanho do campo para a peça não 
    #passar pela borda
    limiteEsq=None
    limiteDir=None
    limiteY=None
    tocouY=False#flag para indicar se a peça tocu o limite inferior
    
    def __init__(self,telaPai,x,y):
        self.x=x
        self.y=y
        super(DesenhoPeca, self).__init__(telaPai)
        self.setGeometry(0, 0, self.x, self.y)
        self.cor=self.gerarCor()
        
    #função que recebe o tipo de peca     
    def receberPeca(self,peca):
        self.peca=peca
    
    def limitarCampo(self):
        #esse trecho encontra o elemento de maior valor nas linhas da matriz
        #Serve para delimitar o movimento das peças
        minimo =0
        maximo= 0
        maxy=0
        
        for j,i in enumerate(self.peca.getPeca()):
            if(minimo>self.peca.getPeca()[j][0]):
                minimo=self.peca.getPeca()[j][0]
                
        for j, i in enumerate(self.peca.getPeca()):
            if(maximo<self.peca.getPeca()[j][0]):
                maximo=self.peca.getPeca()[j][0]
                
        for j, i in enumerate(self.peca.getPeca()):
            if(maxy<self.peca.getPeca()[j][1]):
                maxy=self.peca.getPeca()[j][1]
                
        self.limiteEsq=23*minimo
        self.limiteDir = 23*maximo
        self.limiteY=22*(maxy+1)
        
    def desenharNovaPeca(self):
        self.posX=self.posXinicial
        self.posY=self.posYinicial
        self.cor = self.gerarCor()
        
        
    def gerarCor(self):
                      
        cor = random.randint(0,4)
        return cor 

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        #Esse trecho é responsavel por pintar os trechos onde há peças
        if(len(self.posicoes)>0):
            for i in range(0,len(self.posicoes)):
                self.drawRectangles(qp,self.posicoes[i],self.posicoesY[i],self.peca,self.gerarCor())
        self.drawRectangles(qp,self.posX,self.posY,self.peca,self.cor)
        
    #função responsavel por desenhar as peças e preencher os quadradoes
    #no campo    
    def drawRectangles(self,qp,posX,posY,peca,cor):#Desenha as peças
        #tabela de cores
        colorTable = [0x993300, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
            
        #Responsavel por pintar a peça    
        qp.setBrush(QtGui.QColor(colorTable[cor]))
        #pega a matriz da peça para desenha-la
        matriz = peca.getPeca()
        #desenha as peças    
        qp.drawRect(posX+(23*matriz[0][0]), posY+(22*matriz[0][1]),self.tamQuadrado, self.tamQuadrado)
        qp.drawRect(posX+(23*matriz[1][0]), posY+(22*matriz[1][1]), self.tamQuadrado, self.tamQuadrado)
        qp.drawRect(posX+(23*matriz[2][0]), posY+(22*matriz[2][1]), self.tamQuadrado, self.tamQuadrado)
        qp.drawRect(posX+(23*matriz[3][0]), posY+(22*matriz[3][1]), self.tamQuadrado, self.tamQuadrado)
        
        
        self.limitarCampo()

    def moverEsq(self):
        if(self.posX+self.limiteEsq>0):#impede a peça de passar da tela
            self.posX = self.posX -23
    
    def moverDir(self):
        if(self.posX+self.limiteDir+23<self.x):#impede a peça de passar da tela
            self.posX=self.posX+23
    
    def descerPeca(self):
        if(self.posY+self.limiteY<self.y):
            self.posY=self.posY+22
        else:
            self.tocouY=True
            
    def soltarPeca(self):
        while(self.posY+self.limiteY<self.y):
            self.posY=self.posY+22 
        
    def subirPeca(self):
        self.posY=self.posY-22
            
        
        
        