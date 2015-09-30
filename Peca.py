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
    tamQuadrado=20
    tipoPeca=None
    posX=3*(tamQuadrado+3)
    posY=0
    def __init__(self,telaPai,x,y):
        print(x)
        self.x=x
        self.y=y
        super(Peca, self).__init__(telaPai)
        self.setGeometry(0, 0, self.x, self.y)
        self.tipoPeca = random.randint(1,4)

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        qp.begin(self)
        self.drawRectangles(qp)
        qp.end()
        
    def drawRectangles(self,qp):#Desenha as peças
        print("draw")
     #   color = QtGui.QColor(0, 0, 0)
       # color.setNamedColor('#d4d4d4')
      #  qp.setPen(color)
        qp.setBrush(QtGui.QColor(255, 80, 0, 160))
        #peça []
        if(self.tipoPeca==1):
            qp.drawRect(self.posX, self.posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+23, self.posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX, self.posY+22, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+23, self.posY+22, self.tamQuadrado, self.tamQuadrado)
        #peça L   
        elif(self.tipoPeca==2):
            qp.drawRect(self.posX, self.posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+23, self.posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+46, self.posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX, self.posY+22, self.tamQuadrado, self.tamQuadrado)
        #peça I
        elif(self.tipoPeca==3):
            qp.drawRect(self.posX, self.posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX, self.posY+23, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX, self.posY+46, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX, self.posY+69, self.tamQuadrado, self.tamQuadrado)
        #peça T
        elif(self.tipoPeca==4):
            qp.drawRect(self.posX, self.posY,self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+23, self.posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+46, self.posY, self.tamQuadrado, self.tamQuadrado)
            qp.drawRect(self.posX+23, self.posY+23, self.tamQuadrado, self.tamQuadrado)
       #falta outras peças: S,Z, P
    
    
    def moverEsq(self):
        self.posX = self.posX -23
    
    def moverDir(self):
        self.posX=self.posX+23
    
    def cairPeca(self):
        self.posY=self.posY+23
            
        
        
        
