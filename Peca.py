# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:45:38 2015

@author: Raul
"""
import sys
from PyQt4 import QtGui, QtCore
import random

#Classe responvel por modelar os Tetraminos, tanto virtualmente quanto 
#na interface GUI
class Peca(QtGui.QWidget):
    x=None
    y=None
    novaPeca=True
    teste=False
    posicoes=[]
    posicoesY=[]
    tamQuadrado=20
    tipoPeca=None
    posX=3*(tamQuadrado+3)
    posY=22
    def __init__(self,telaPai,x,y):
        self.x=x
        self.y=y
        super(Peca, self).__init__(telaPai)
        self.setGeometry(0, 0, self.x, self.y)
        self.gerarPeca()
         
    def gerarPeca(self):
        self.tipoPeca=random.randint(1,4)

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
            self.gerarPeca()
        if(len(self.posicoes)>0):
            for i in range(0,len(self.posicoes)):
                self.drawRectangles(qp,self.posicoes[i],self.posicoesY[i])
      #  qp.begin(self)
        self.drawRectangles(qp,self.posX,self.posY)
      #  qp.end()
        
       

        
    def drawRectangles(self,qp,posX,posY):#Desenha as peças
        colorTable = [0x000000, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        if(self.novaPeca==True):
            self.cor = random.randint(0,4)
            self.novaPeca=False
            
        qp.setBrush(QtGui.QColor(colorTable[self.cor]))
        #peça []
        if(self.tipoPeca==1):
            qp.drawRect(posX, posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+23, posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX, posY+22, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+23, posY+22, self.tamQuadrado, self.tamQuadrado)
        #peça L   
        elif(self.tipoPeca==2):
            qp.drawRect(posX, posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+23, posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+46, posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX, posY+22, self.tamQuadrado, self.tamQuadrado)
        #peça I
        elif(self.tipoPeca==3):
            qp.drawRect(posX, posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX, posY+22, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX, posY+44, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX, posY+66, self.tamQuadrado, self.tamQuadrado)
        #peça T
        elif(self.tipoPeca==4):
            qp.drawRect(posX, posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+23, posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+46, posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(posX+23, posY+23, self.tamQuadrado, self.tamQuadrado)
       #falta outras peças: S,Z, P
    
    
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
            
        
        
        
