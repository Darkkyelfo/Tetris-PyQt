# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:45:38 2015

@author: Raul
"""
from numpy import array, random, append, empty


# Classe responvel por modelar tretraminos através de matrizes
class Peca(object):

    def __init__(self, tipo):
        self.setTipo(tipo)

    # Gera uma peca de um tipo escolhido
    def setTipo(self, tipo):
        self.tipo = tipo
        self.setRotaco(1)

    # Permite escolher a rotação desejada
    def setRotaco(self, rotacao):
        self.rotacao = rotacao

    def getTipoFixo(self):
        return self.tipo

    def getTipoTrans(self):
        return -self.tipo

    # responsavel por alterar a rotação da peça
    # rotacão 1 é a padrão
    def rotacionar(self):
        if (self.rotacao == self.rotacaoMax):
            self.rotacao = 0
        self.rotacao = self.rotacao + 1

    def getPeca(self):
        matriz_peca = None
        # []
        if (self.tipo == 1):
            matriz_peca = [[0, 0],  # 0
                           [0, 1],  # 1
                           [1, 0],  # 2
                           [1, 1]]  # 3
            self.rotacaoMax = 1

        # L
        elif (self.tipo == 2):
            self.rotacaoMax = 4
            if (self.rotacao == 1):
                matriz_peca = [[0, 0],
                               [-1, 0],
                               [1, 1],
                               [1, 0]]
            # L "deitado"
            elif (self.rotacao == 2):
                matriz_peca = [[0, 0],
                               [0, -1],
                               [0, 1],
                               [1, -1]]
            # L "7"
            elif (self.rotacao == 3):
                matriz_peca = [[0, 0],
                               [-1, -1],
                               [-1, 0],
                               [-1, 0]]
            # L "7 deitado"
            else:
                matriz_peca = [[0, 0],
                               [-1, 1],
                               [0, -1],
                               [0, 1]]

        # peça I
        elif (self.tipo == 3):
            self.rotacaoMax = 2
            if (self.rotacao == 1):
                matriz_peca = [[0, 0],
                               [-1, 0],
                               [1, 0],
                               [2, 0]]
            # I "deitado"
            else:
                matriz_peca = [[0, 0],
                               [0, -1],
                               [0, 1],
                               [0, 2]]

        # peça T
        elif (self.tipo == 4):
            self.rotacaoMax = 4
            if (self.rotacao == 1):
                matriz_peca = [[0, 0],
                               [0, -1],
                               [0, 1],
                               [1, 0]]
            # T "de lado"
            elif (self.rotacao == 2):
                matriz_peca = [[0, 0],
                               [0, -1],
                               [-1, 0],
                               [1, 0]]
            # T "invertido"
            elif (self.rotacao == 3):
                matriz_peca = [[0, 0],
                               [-1, 1],
                               [0, -1],
                               [0, 1]]
            # T "de lado"
            else:
                matriz_peca = [[0, 0],
                               [0, 1],
                               [-1, 0],
                               [1, 0]]

        # peça S
        elif (self.tipo == 5):
            if (self.rotacao == 1):
                self.rotacaoMax = 2
                matriz_peca = [[0, 0],
                               [-1, 0],
                               [0, 1],
                               [1, 1]]
            # S "rotacionado"
            else:
                matriz_peca = [[0, 0],
                               [1, -1],
                               [1, 0],
                               [0, 1]]

        # peça Z
        elif (self.tipo == 6):
            self.rotacaoMax = 2
            if (self.rotacao == 1):
                matriz_peca = [[0, 0],
                               [-1, 1],
                               [0, 1],
                               [1, 0]]
            # Z "rotacionado"
            else:
                matriz_peca = [[0, 0],
                               [0, -1],
                               [1, 0],
                               [1, 0]]

        # peça P
        elif (self.tipo == 7):
            self.rotacaoMax = 4
            if (self.rotacao == 1):
                matriz_peca = [[0, 0],
                               [0, -1],
                               [0, 1],
                               [-1, -1]]
            # P "deitado"
            elif (self.rotacao == 2):
                matriz_peca = [[0, 0],
                               [-1, 0],
                               [-1, 1],
                               [1, 0]]

            elif (self.rotacao == 3):
                matriz_peca = [[0, 0],
                               [0, 1],
                               [0, -1],
                               [1, 1]]
            # P "L invertido"
            else:
                matriz_peca = [[0, 0],
                               [-1, 0],
                               [1, -1],
                               [1, 0]]

        return array(matriz_peca)


class ControladorPecas(object):

    def __init__(self, quantidade, seed=None):
        self.seed = seed
        self.pecas = self._gerarPecas(quantidade)
        self._peca_atual = 0
        self.limite = self.pecas.size

    def darPeca(self):
        if (self._peca_atual > self.limite):
            append(self.pecas, self._gerarPecas(1000))
        peca_da_vez = self.pecas[self._peca_atual]
        self._peca_atual += 1
        return peca_da_vez

    def _gerarPecas(self, quantidade):
        if (self.seed != None):
            random.seed(self.seed)
            self.seed += 1
        pecas_tipos = random.randint(1, 8, size=quantidade)
        pecas = empty((quantidade), dtype=Peca)
        for i, tipo in enumerate(pecas_tipos):
            pecas[i] = Peca(tipo)
        return pecas

    def getIndiceAtual(self):
        return self._peca_atual

    def setIndiceAtual(self, indice):
        self._peca_atual = indice

    def setIndiceAnterior(self):
        self._peca_atual -= 1
