# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:41:21 2015

@author: Raul
"""
import random

from ListaSincronizada import ListaSincronizada


class Agente():
    tetrisesFeitas = ListaSincronizada()
    genes = []
    qtGenes = 7
    desempenho = None  # armazena oquão eficiente é o agente

    # gera um agente aleatório
    def __init__(self):
        for i in range(0, self.qtGenes):
            self.genes.append(random.random())

    def avaliarJogada(self, campo):
        qualidade = 0
        # positivos
        qualidade = qualidade + (self.genes[0] * self.linhasFeitas(campo))
        # negativos
        qualidade = qualidade - (self.genes[2] * self.alturaMaxima(campo))
        qualidade = qualidade - (self.genes[4] * self.countSingleHoles(campo))
        qualidade = qualidade - (self.genes[4] * self.countConnectedHoles(campo))
        qualidade = qualidade - (self.genes[5] * self.blocosSobreBuracos(campo))
        qualidade = qualidade - (self.genes[6] * self.pocos(campo))
        qualidade = qualidade - (self.genes[3] * self.nivelamento(campo))
        return qualidade

    # Os trechos a seguir se são todos métodos de avaliação do campo
    # procurarLinhasFeitas
    # recebe o campo do tetris(uma matriz) como argumento
    def linhasFeitas(self, campo):
        cleared = 0
        columns = len(campo[0])
        y = 0
        while y < len(campo) - 1:
            ok = True
            x = 1
            while (x < columns - 1) and ok:
                if campo[y][x] == 0:
                    ok = False
                x += 1
                if ok:
                    cleared += 1
            y += 1
        return cleared

    # retorna altura maxima que o campo se encontra
    def alturaMaxima(self, campo):
        columns = columns = len(campo[0])
        y = 0
        while y < len(campo) - 1:
            x = 1
            while x < columns - 1:
                if campo[y][x] != 0:
                    return len(campo) - 1 - y
                x += 1
            y += 1
        return 0

    def countSingleHoles(self, board):
        holes = 0
        columns = len(board[0])
        j = 1
        while j < columns - 1:
            swap = False
            i = 0
            while i < len(board) - 1:
                if board[i][j] != 0:
                    swap = True
                else:
                    if swap:
                        holes += 1
                i += 1
            j += 1
        return holes

    def countConnectedHoles(self, board):
        holes = 0
        columns = len(board[0])
        j = 1
        while j < columns - 1:
            swap = False
            i = 0
            while i < len(board) - 1:
                if board[i][j] != 0:
                    swap = True
                else:
                    if swap:
                        holes += 1
                    swap = False
                i += 1
            j += 1
        return holes

    # verifica o nivelamento entre as colunas
    def blocosSobreBuracos(self, board):
        blocks = 0
        cols = len(board[0])
        c = 1
        while c < cols - 1:
            swap = False
            r = len(board) - 2
            while r >= 0:
                if board[r][c] == 0:
                    swap = True
                else:
                    if swap:
                        blocks += 1
                r -= 1
            c += 1
        return blocks

    def pocos(self, board):
        cols = len(board[0])
        wells = 0
        # da segunda até a  penultima coluna
        col = 2
        while col < cols - 2:
            row = 0
            while row < len(board) - 1:
                if (board[row][col - 1] > 0) and (board[row][col + 1] > 0) and (board[row][col] == 0):
                    wells += 1
                elif board[row][col] > 0:
                    break
                row += 1
            col += 1
        # primeira coluna
        row = 0
        while row < len(board) - 1:
            if (board[row][1] == 0) and (board[row][2] > 0):
                wells += 1
            elif board[row][1] > 0:
                break
            row += 1
        # ultima coluna
        row = 0
        while row < len(board) - 1:
            if (board[row][cols - 3] > 0) and (board[row][cols - 2] == 0):
                wells += 1
            elif board[row][cols - 2] > 0:
                break
            row += 1
        return wells

    def nivelamento(self, board):
        cols = len(board[0])
        heights = [0] * (cols - 2)
        x = 1
        while x < cols - 1:
            y = 0
            while y < len(board) - 1:
                if board[y][x] != 0:
                    heights[x - 1] = len(board) - 1 - y
                    break
                y += 1
            x += 1
        bmp = 0.0
        i = 0
        while i < cols - 3:
            diff = abs(heights[i] - heights[i + 1])
            bmp += diff
            i += 1
        return bmp
