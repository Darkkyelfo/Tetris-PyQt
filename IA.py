# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:40:41 2015

@author: Raul
"""
import operator
from PyQt4 import QtGui, QtCore
from GameBehavior import GameBehavior
from Movimento import Movimento
from Agente import Agente
from tocarMusica import tocarMusica

class IA(GameBehavior):
    agente=None
    
    def __init__(self,agente):
        self.agente=agente
        self.velocidadeQueda=1000#determina a velocidade da jogada da IA(dado em milésimos)
        super(IA,self).__init__(None)
    #funçao que recebe eventos do teclado
    #fica desativada quando o Agente joga
    def keyPressEvent(self, event):
        b=False
        
    def receberAgente(self,agente):
        self.agente=agente
    #detecta se a peça colidiu com outra peça ou se chegou ao fim do campo
    def detectarColisao(self,posX,posY):
        for i in range(4):#Verifica se a peça não está "atravessando" o campo pelas laterais
            colidiu=False
            x=self.desenhoPeca.posXtoIndex(posX+(23*self.pecaAtual.getPeca()[i][0]))
            if(x<0 or x>len(self.desenhoPeca.campo[0])-1):#se estiver, não há colisão
                return False
        for i in range(4):#verifica se a a peça colidiu com alguma outra peça no campo ou se cheou ao fim dele
            if(super(IA, self).detectarColisao(posX+(23*self.pecaAtual.getPeca()[i][0]),posY+(22*self.pecaAtual.getPeca()[i][1]))):
                colidiu=True
        return colidiu
    #função responsável por determinar se o movimento é válido ou não
    #mesmo quando se detecta a colisão é nescessário verificas se ao
    # redor da peça está livre. A função faz isso
    def movimentoEhPossivel(self,posX,posY):
        ehPossivel=False
        if(self.detectarColisao(posX,posY)):#Se houve colisão
            matriz=self.pecaAtual.getPeca()
            ehPossivel = True
            for i in range(4):#verifica se todas a posições que a peça vai ocupar estão vagas
                linha = self.desenhoPeca.posYtoIndex(posY+(22*matriz[i][1]))
                coluna = self.desenhoPeca.posXtoIndex(posX+(23*matriz[i][0]))
                try:
                    if(self.desenhoPeca.campo[linha][coluna]!=0):
                        return False
                except IndexError:
                    return False
        return ehPossivel
                
    #Encontra todos os movimentos possíveis 
    def encontrarMovimentos(self):
        movimentosPossiveis=[]#lista com os movimentos possiveis(contem a posição e o tipo da peça)
        for u in range(self.pecaAtual.rotacaoMax):
            for j in range(len(self.desenhoPeca.campo[0])):#percorre o campo coluna por coluna(de cima pra baixo)
                for i in range (len(self.desenhoPeca.campo)):
                    #converte os indices da matriz para posições da GUI
                    posX=self.desenhoPeca.colunaToPos(j)
                    posY=self.desenhoPeca.linhaToPos(i)
                    if(self.movimentoEhPossivel(posX,posY)):
                        movimentosPossiveis.append(Movimento(posX,posY,self.pecaAtual.tipo,self.pecaAtual.rotacao))
            self.pecaAtual.rotacionar()
        return movimentosPossiveis
        
    #Avalia qual é o melhor movimento                    
    def avaliarMelhorJogada(self):
        movPossiveis=self.encontrarMovimentos()
        for i in movPossiveis:
            self.pecaAtual.setRotaco(i.rotacao)
            matriz=self.pecaAtual.getPeca()
            for r in range(4):
                self.desenhoPeca.postoIndex(i.posX+(23*matriz[r][0]),i.posY+(22*matriz[r][1]),i.tipoPeca)
            i.qualidade=self.agente.avaliarJogada(self.desenhoPeca.campo)
            for k in range(4):
                self.desfazerMovimento(i.posX+(23*matriz[k][0]),i.posY+(22*matriz[k][1]))
        #trecho responsável pela jogada da IA
        #determina onde o Agente irá jogar
        movPossiveis.sort(key=operator.attrgetter("qualidade"),reverse=True)
        self.pecaAtual.setRotaco(movPossiveis[0].rotacao)
        matriz=self.pecaAtual.getPeca()
        for j in range(4):
            self.desenhoPeca.postoIndex(movPossiveis[0].posX+(23*matriz[j][0]),movPossiveis[0].posY+(22*matriz[j][1]),movPossiveis[0].tipoPeca)

    def desfazerMovimento(self,posX,posY):
        linha = self.desenhoPeca.posYtoIndex(posY)
        coluna = self.desenhoPeca.posXtoIndex(posX)
        self.desenhoPeca.campo[linha][coluna]=0
    
    def iniciarIA(self):
        self.avaliarMelhorJogada()
     
    def time(self):
        self.iniciarIA()
        self.score.display(self.desenhoPeca.linhasFeitas)
        self.criarNovaPeca()
        self.update()
        if(len(self.desenhoPeca.campo[0])>self.desenhoPeca.campo[0].count(0)):#finaliza a partida
            self.timer.stop()