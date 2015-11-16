# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:45:38 2015

@author: Raul
"""
import random

#Classe responvel por modelar tretraminos através de matrizes
class Peca():
    tipo=None
    rotacao = None#indica a rotação atual
    rotacaoMax=None#indica o número máximo de rotações suportadas
    maiorY=0#armazena o maior valor no eixo y para ser utilizado na colisão
    maiorX=0#''
    menorX=0#''
    #gera uma peca aleatoriamente
    def gerarPeca(self):    
        self.tipo = random.randint(1,7)
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
    
    #responsavel por encontrar os maiores valores na matriz da peça
    #é utilizado para delimitar colisões e o limite da tela
    def maxMin(self,matriz):
        self.menorX =0
        self.maiorX= 0
        self.maiorY=0
        
        for j,i in enumerate(matriz):
            if(self.menorX>matriz[j][0]):
                self.menorX=matriz[j][0]
                
        for j, i in enumerate(matriz):
            if(self.maiorX<matriz[j][0]):
                self.maiorX=matriz[j][0]
                
        for j, i in enumerate(matriz):
            if(self.maiorY<matriz[j][1]):
                self.maiorY=matriz[j][1]

        
        
    #gera a matriz que representa as peças e suas rotações    
    def getPeca(self):
        matriz = None
        #[]
        if(self.tipo==1):
            matriz = [[0,-1], #0
                      [0,0], #1
                      [1,0], #2 
                      [1,-1]] #3
            self.rotacaoMax=1
            
        #L                            
        elif(self.tipo==2):
            self.rotacaoMax=4
            if(self.rotacao==1):
                matriz = [[0,-1],
                          [0,0],
                          [0,1],
                          [1,1]]
            #L "deitado"              
            elif(self.rotacao==2):
                matriz = [[1,0],
                          [0,0],
                          [-1,0],
                          [-1,1]]
            # L "7"
            elif(self.rotacao==3):
                matriz = [[0,1],
                          [0,0],
                          [0,-1],
                          [-1,-1]]
            # L "7 deitado"
            else:
                matriz = [[1,0],
                          [0,0],
                          [-1,0],
                          [1,-1]]
                          
        #peça I              
        elif(self.tipo==3):
            self.rotacaoMax=2
            if(self.rotacao==1):
                matriz=[[0,-1],
                        [0,0],
                        [0,1],
                        [0,2]]
            # I "deitado"
            else:
                matriz=[[1,0],
                        [0,0],
                        [-1,0],
                        [-2,0]]
        
        #peça T
        elif(self.tipo==4):
            self.rotacaoMax=4
            if(self.rotacao==1):
                matriz=[[-1,0],
                        [0,0],
                        [1,0],
                        [0,1]]
            #T "de lado"
            elif(self.rotacao==2):
                matriz=[[0,-1],
                        [0,0],
                        [0,1],
                        [-1,0]]
            #T "invertido"
            elif(self.rotacao==3):
                matriz=[[1,0],
                        [0,0],
                        [-1,0],
                        [0,-1]]
            #T "de lado"
            else:
                matriz=[[0,1],
                        [0,0],
                        [0,-1],
                        [1,0]]
        
        #peça S
        elif(self.tipo==5):
            if(self.rotacao==1):
                self.rotacaoMax=2
                matriz=[[0,-1],
                        [0,0],
                        [-1,0],
                        [1,-1]]
            # S "rotacionado"
            else:
                matriz=[[1,0],
                        [0,0],
                        [0,-1],
                        [1,1]]
            
        #peça Z
        elif(self.tipo==6 ):
            self.rotacaoMax=2
            if(self.rotacao==1):
                matriz=[[0,-1],
                        [0,0],
                        [1,0],
                        [-1,-1]]
            #Z "rotacionado"
            else:
                matriz=[[1,0],
                        [0,0],
                        [0,1],
                        [1,-1]]
            
        #peça P
        elif(self.tipo==7):
            self.rotacaoMax=4
            if(self.rotacao==1):
                matriz = [[0,-1],
                          [0,0],
                          [0,1],
                          [1,-1]]
            # P "deitado"
            elif(self.rotacao==2):
                matriz = [[1,0],
                          [0,0],
                          [-1,0],
                          [1,1]]
            #P "L invertido"
            elif(self.rotacao==3):
                matriz = [[0,1],
                          [0,0],
                          [0,-1],
                          [-1,1]]
            else:
                matriz = [[1,0],
                          [0,0],
                          [-1,0],
                          [-1,-1]]
                          
        self.maxMin(matriz)
        
        return matriz
        
    
        
    
            
            
    

            
        
        
        
