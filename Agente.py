# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:41:21 2015

@author: Raul
"""
import random
from ListaSincronizada import ListaSincronizada
class Agente():
    tetrisesFeitas = ListaSincronizada() 
    genes=[]   
    qtGenes=7
    desempenho=None #armazena oquão eficiente é o agente
    
    #gera um agente aleatório 
    def __init__(self):
        for i in range(0,self.qtGenes):
            self.genes.append(random.random())
   
    def avaliarJogada(self,campo):
        qualidade=0
        #positivos
        qualidade =qualidade +(self.genes[0] * self.linhasFeitas(campo)) 
        qualidade = qualidade +(self.genes[1]*self.numTetrizes(campo))
        #negativos
        qualidade =qualidade -(self.genes[2] * self.alturaMaxima(campo))
        qualidade =qualidade - (self.genes[3]*self.nivelamento(campo))
        qualidade = qualidade -(self.genes[4] * self.numBuracos(campo))
        qualidade = qualidade -(self.genes[5]*self.blocosSobreBuracos(campo))
        qualidade = qualidade =(self.genes[6]*self.pocos(campo))
        return qualidade
    
    def compararAgente(self,agente):
        ehMelhor=False
        if(self.desempenho>agente.desempenho):
            ehMelhor=True
        return ehMelhor
    
    def clonarAgente(self):
        agente = Agente()
        for indice, i in enumerate(self.genes):
            agente[indice]=i
        return agente
        
    #Os trechos a seguir se são todos métodos de avaliação do campo    
    
    #procurarLinhasFeitas
    #recebe o campo do tetris(uma matriz) como argumento
    def linhasFeitas(self,campo):
        numLinhas=0
        for linha in campo:
            if not 0 in linha:
                numLinhas+=1
        return numLinhas
            
    #retorna altura maxima que o campo se encontra
    def alturaMaxima(self,campo):    
        alturaMax=0
        for i in range(len(campo)-1,-1,-1):#percorre de baixo pra cima
        #todos os elementos da lista sao iguais a 0? se for falso incremento o contador
            if all(campo[j]==0 for j in campo[i])==False:
                alturaMax+=1;
        return alturaMax
    
    #conta a quantidade de buracos existentes no campo
    def numBuracos(self,campo):
        buracos=0
        for linha in campo:
            ehZero=False
            for j in linha:
                if(j==0):
                    ehZero=True
                else:
                    if(ehZero):
                        buracos+=1
                        ehZero=False
        return buracos
    
    #Conta o número de tetrizes formadas
    def numTetrizes(self,campo):
        tetrizes=0
        for i in range(0,len(campo),4):
            ok=True
            for j in range(0,len(campo[i])):
                for y in range(i,-1,-1):
                    if(campo[y][j]==0):
                        ok=False
            if(ok):
                tetrizes+=1
        return tetrizes
                
    #verifica o nivelamento entre as colunas
    def nivelamento(self,campo):
        alturas=[]
        for j in range(0,len(campo[0])):
            for i in range(0,len(campo)):
                if(campo[i][j]!=0):
                    alturas.append(j)
                    break
        nivel=0
        for i in range(len(alturas)-1):
            diferenca =   abs(alturas[i]-alturas[i+1])
            nivel+=diferenca
        return nivel

    def blocosSobreBuracos(self,campo):
        blocos=0
        for j in range(0,len(campo[0])):
            diferenteZero=False
            for i in range(0,len(campo)):
               if(campo[i][j]!=0):
                   diferenteZero=True
               else:
                   if(diferenteZero):
                       diferenteZero=False
                       blocos+=1
        return blocos
                       
    def pocos(self,campo):
        pocos=0
        #percorre a primeira coluna do campo
        for i in range(len(campo)-1,-1,-1):
            cont=0 
            if((campo[i][0]==0 and campo[i][1]!=1)):
                cont+=1
            else:
                cont=0
            if(cont==4):
                pocos+=1
        #percorre a última coluna
        for i in range(len(campo)-1,-1,-1):
            cont=0
            if((campo[i][len(campo[0])-2]==1 and campo[i][len(campo[0])-1]!=0)):
                cont+=1 
            else:
                cont=0
            if(cont==4):
                pocos+=1
      #percorre o meio do campo          
        for j in range(1,len(campo[0])-1):
            cont=0
            for i in range(len(campo)-1,-1,-1):
                if(campo[i][j-1]==1 and campo[i][j]==0 and campo[i][j+1]==1):
                    cont=0
                else:
                    cont=0
                if(cont==4):
                    pocos+=1
        return pocos
            
                  
                
                    
                    
                
        

        
        
            
               
        
    
        
    
            
            