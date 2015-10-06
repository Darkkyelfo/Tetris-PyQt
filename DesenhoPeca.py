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
    x=None
    y=None
    novaPeca=True
    teste=False
    posicoes=[]
    posicoesY=[]
    tamQuadrado=20
    peca=None
    posX=3*(tamQuadrado+3)
    posY=22
    def __init__(self,telaPai,x,y):
        self.x=x
        self.y=y
        super(DesenhoPeca, self).__init__(telaPai)
        self.setGeometry(0, 0, self.x, self.y)
        
    #função que recebe o tipo de peca     
    def receberPeca(self,peca):
        self.peca=peca

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        if(self.teste):
            self.posicoes.append(self.posX)
            self.posicoesY.append(self.posY)
            print(self.posicoes)
            print(self.posicoesY)
            self.posX=3*(self.tamQuadrado+3)
            self.posY=22
            self.teste=False
        if(len(self.posicoes)>0):
            for i in range(0,len(self.posicoes)):
                self.drawRectangles(qp,self.posicoes[i],self.posicoesY[i],self.peca)
        self.drawRectangles(qp,self.posX,self.posY,self.peca)
        
    #função responsavel por desenhar as peças e preencher os quadradoes
    #no campo    
    def drawRectangles(self,qp,posX,posY,peca):#Desenha as peças
        #tabela de cores
        colorTable = [0x993300, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
                      
        if(self.novaPeca==True):
            self.cor = random.randint(0,4)
            self.novaPeca=False
            
        #Responsavel por pintar a peça    
        qp.setBrush(QtGui.QColor(colorTable[self.cor]))
        #pega a matriz da peça para desenha-la
        matriz = peca.getPeca()
        #desenha as peças    
        qp.drawRect(posX+(23*matriz[0][0]), posY+(22*matriz[0][1]),self.tamQuadrado, self.tamQuadrado)
        qp.drawRect(posX+(23*matriz[1][0]), posY+(22*matriz[1][1]), self.tamQuadrado, self.tamQuadrado)
        qp.drawRect(posX+(23*matriz[2][0]), posY+(22*matriz[2][1]), self.tamQuadrado, self.tamQuadrado)
        qp.drawRect(posX+(23*matriz[3][0]), posY+(22*matriz[3][1]), self.tamQuadrado, self.tamQuadrado)
            
    def moverEsq(self):
        print(self.posX)
        if(self.posX >0):#impede a peça de passar da tela
            self.posX = self.posX -23
    
    def moverDir(self):
        print(self.posX)
        if(self.posX+23<= self.x):#impede a peça de passar da tela
            self.posX=self.posX+23
    
    def cairPeca(self):
        self.posY=self.posY+22
        
    def subirPeca(self):
        self.posY=self.posY-22
            
        
        
        
