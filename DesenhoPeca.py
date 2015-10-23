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
    cont=0
    x=None#armazena o tamanho da tela (229)
    y=None
    cor=None#armazena a cor da peca
    tamQuadrado=20
    peca=None#Armazena o tipo de peça. Recebe um objeto do tipo peça
    #cria uma matriz 22x10 que representa o campo
    campo=[[0,0,0,0,0,0,0,0,0,0] for i in range(22)]
    #guarda a posição inicial das peças
    posXinicial=4*(tamQuadrado+3)
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
    linhasFeitas =0
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
                
        self.limiteEsq=23*self.peca.menorX
        self.limiteDir = 23*self.peca.maiorX
        self.limiteY=22*(self.peca.maiorY+1)
        
    def desenharNovaPeca(self):
        self.posX=self.posXinicial
        if(self.peca.tipo!=4):#gambiarra para corrigir um erro. Depois explico :)
            self.posY=self.posYinicial-22
        else:
            self.posY=self.posYinicial-44
        self.cor = self.gerarCor()
        
        
    def gerarCor(self):
                      
        cor = random.randint(0,4)
        return cor 

    def paintEvent(self, e):
        qp = QtGui.QPainter(self)
        self.drawRectangles(qp,self.posX,self.posY,self.peca,self.cor)
        alterarMatriz=False#indica que alguma linha da matriz tem que ser "setada" para 0
        #esse trecho varre a matriz do campo e vai preenchendo os locais
        #onde a peças 
        for linha,i in enumerate(self.campo):
            for coluna,j in enumerate(i):
                if(j!=0):#Se é diferente de 0 indica que há uma peça nesse indice
                    self.desenharQuadrado(qp,self.colunaToPos(coluna),self.linhaToPos(linha),j[1])
                if(0 not in i):#caso forme uma linha ela será apagada
                    alterarMatriz=True
            if(alterarMatriz):
                alterarMatriz=False
                self.descerLinhas(linha)
        
        
    #função responsavel por desenhar as peças e preencher os quadradoes
    #no campo. Dsenha peças completas    
    def drawRectangles(self,qp,posX,posY,peca,cor):#Desenha as peças
        #tabela de cores
        colorTable = [0x993300, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
            
        #Responsavel por pintar a peça    
        qp.setBrush(QtGui.QColor(colorTable[cor]))
        #pega a matriz da peça para desenha-la
        matriz = peca.getPeca()
        #desenha as peças    
        for i in range(0,4):
            qp.drawRect(posX+(23*matriz[i][0]), posY+(22*matriz[i][1]),self.tamQuadrado, self.tamQuadrado)
        
        self.limitarCampo()
    
    #desenha apenas um quadrado
    def desenharQuadrado(self,qp,posX,posY,cor):
        #tabela de cores
        colorTable = [0x993300, 0xCC6666, 0x66CC66, 0x6666CC,
                      0xCCCC66, 0xCC66CC, 0x66CCCC, 0xDAAA00]
        #Responsavel por pintar a peça    
        qp.setBrush(QtGui.QColor(colorTable[cor]))
        #desenha apenas um quadrado
        qp.drawRect(posX,posY,self.tamQuadrado, self.tamQuadrado)
            

    def moverEsq(self):
        podeMover=True
        if(self.posX+self.limiteEsq>0):#impede a peça de passar da tela
            matriz=self.peca.getPeca()
            #verifica se do lado esquerdo da peça existe outra peça
            #Só permite que a peça se mova pra esquerda caso não tenha peça.
            #simula um colisor esquerdo para peça
            for i in range(0,4):
                if(self.campo[self.posYtoIndex(self.posY+(22*matriz[i][1]))][self.posXtoIndex(self.posX+(23*matriz[i][0]))-1]!=0):
                    podeMover=False
            if(podeMover):
                self.posX = self.posX -23
    
    def moverDir(self):
        podeMover=True
        if(self.posX+self.limiteDir+23<self.x):#impede a peça de passar da tela
            matriz=self.peca.getPeca()
            for i in range(0,4):
                if(self.campo[self.posYtoIndex(self.posY+(22*matriz[i][1]))][self.posXtoIndex(self.posX+(23*matriz[i][0]))+1]!=0):
                    podeMover=False
            if(podeMover):
                self.posX=self.posX+23
    
    def descerPeca(self):
        if(self.posY+self.limiteY<self.y):
            self.posY=self.posY+22
        else:
            self.tocouY=True
            
    def soltarPeca(self):#ainda não está funcional
        while(self.posY+self.limiteY<self.y and self.campo[self.posYtoIndex(self.posY+(22*self.peca.maiorY))+1][self.posXtoIndex(self.posX)]==0):
            self.posY=self.posY+22 
        
    def posXtoIndex(self,posX):
        return posX/23 
    
    def posYtoIndex(self,posY):
        return posY/22 
    
    #responsavel por marcar na matriz os locais onde há peças
    #converte a posição(x,y) em índices da matriz do campo 
    def postoIndex(self,posX,posY,cor):
        indexX=self.posXtoIndex(posX)
        indexY=self.posYtoIndex(posY)
        if(self.campo[indexY][indexX]==0):
            self.campo[indexY][indexX]=[1,cor]
    
    #converte o indice da linha para as coordenadas na GUI
    def colunaToPos(self,coluna):
        return 23*(coluna)
    #converte o indice da coluna para as coordenadas na GUI   
    def linhaToPos(self,linha):
        return 22*(linha)
    
    #responsavel por apagar a linha criada 
    #e pelo efeito descer as linhas acima
    def descerLinhas(self,indiceLinha):
        #self.cont+=1
       # print("entrei %s"%self.cont)
        for i in range(indiceLinha,0,-1):
            self.campo[i]=self.campo[i-1]
            if(i==1):
                self.campo[i-1]=[0,0,0,0,0,0,0,0,0,0]
        self.linhasFeitas+=1

    def imprimirCampo(self):
        for i in self.campo:
            for j in i:
                if(j!=0):
                    j=1
                print(j),
            print("\n")
      

            
        
        
        
