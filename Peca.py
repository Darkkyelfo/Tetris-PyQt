# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:45:38 2015

@author: Raul
"""
import sys
import random

#Classe responvel por modelar tretraminos através de matrizes
class Peca():
    tipo=None
    rotacao = None
    rotacaoMax=None
    #gera uma peca aleatoriamente
    def gerarPeca(self):    
        self.tipo = random.randint(1,4)
        self.rotacao=1
        
    #Gera uma peca de um tipo escolhido
    def setTipo(self,tipo):
        self.tipo=tipo
    
    #Permite escolher a rotação desejada
    def setRotaco(self,rotacao): 
        self.rotacao=rotacao
        
    #responsavel por alterar a rotação da peça
    #rotacão 1 é a padrão
    def rotacionar(self):
        if(self.rotacao==self.rotacaoMax):
            self.rotacao=0
        self.rotacao=self.rotacao+1
        
    #gera a matriz que representa as peças e suas rotações    
    def getPeca(self):
        matriz = None
        #[]
        if(self.tipo==1):
            matriz = [[0,0], #0
                      [1,0], #1
                      [0,1], #2 
                      [1,1]] #3
            self.rotacaoMax=1
                      
        #L              
        elif(self.tipo==2 and self.rotacao==1):
            matriz = [[0,-1],
                      [0,0],
                      [0,1],
                      [1,1]]
            self.rotacaoMax=4
        #L "deitado"              
        elif(self.tipo==2 and self.rotacao==2):
            matriz = [[1,0],
                      [0,0],
                      [-1,0],
                      [-1,1]]
            self.rotacaoMax=4
        # L "7"
        elif(self.tipo==2 and self.rotacao==3):
            matriz = [[0,1],
                      [0,0],
                      [0,-1],
                      [-1,-1]]
            self.rotacaoMax=4
                      
        # L "7 deitado"
        elif(self.tipo==2 and self.rotacao==4):
            matriz = [[1,0],
                      [0,0],
                      [-1,0],
                      [1,-1]]
            self.rotacaoMax=4
                      
        #peça I              
        elif(self.tipo==3 and self.rotacao==1):
            matriz=[[0,-1],
                    [0,0],
                    [0,1],
                    [0,2]]
            self.rotacaoMax=2
        # I "deitado"
        elif(self.tipo==3 and self.rotacao==2):
            matriz=[[1,0],
                    [0,0],
                    [-1,0],
                    [-2,0]]
            self.rotacaoMax=2
        
        #peça T
        elif(self.tipo==4 and self.rotacao==1):
            matriz=[[-1,0],
                    [0,0],
                    [1,0],
                    [0,1]]
            self.rotacaoMax=4
        #T "de lado"
        elif(self.tipo==4 and self.rotacao==2):
            matriz=[[0,-1],
                    [0,0],
                    [0,1],
                    [-1,0]]
            self.rotacaoMax=4
        #T "invertido"
        elif(self.tipo==4 and self.rotacao==3):
            matriz=[[1,0],
                    [0,0],
                    [-1,0],
                    [0,-1]]
            self.rotacaoMax=4
        #T "de lado"
        elif(self.tipo==4 and self.rotacao==4):
            matriz=[[0,1],
                    [0,0],
                    [0,-1],
                    [1,0]]
            self.rotacaoMax=4
        
        #peça S
        elif(self.tipo==5 and self.rotacao==1):
            matriz=[[0,-1],
                    [0,0],
                    [-1,0],
                    [1,-1]]
            self.rotacaoMax=2
        # S "rotacionado"
        elif(self.tipo==5 and self.rotacao==2):
            matriz=[[1,0],
                    [0,0],
                    [0,-1],
                    [1,1]]
            self.rotacaoMax=2
            
        #peça Z
        elif(self.tipo==6 and self.rotacao==1):
            matriz=[[0,-1],
                    [0,0],
                    [1,0],
                    [-1,-1]]
            self.rotacaoMax=2
        #Z "rotacionado"
        elif(self.tipo==6 and self.rotacao==2):
            matriz=[[1,0],
                    [0,0],
                    [0,1],
                    [1,-1]]
            self.rotacaoMax=2            
            
        #peça P
        elif(self.tipo==7 and self.rotacao==1):
            matriz = [[0,-1],
                      [0,0],
                      [0,1],
                      [1,-1]]
            self.rotacaoMax=4
        # P "deitado"
        elif(self.tipo==7 and self.rotacao==2):
            matriz = [[1,0],
                      [0,0],
                      [-1,0],
                      [1,1]]
            self.rotacaoMax=4
        #P "L invertido"
        elif(self.tipo==7 and self.rotacao==3):
            matriz = [[0,1],
                      [0,0],
                      [0,-1],
                      [-1,1]]
            self.rotacaoMax=4
        elif(self.tipo==7 and self.rotacao==4):
            matriz = [[1,0],
                      [0,0],
                      [-1,0],
                      [-1,-1]]
            self.rotacaoMax=4
        
                    
        return matriz
            
            
    

            
        
        
        
