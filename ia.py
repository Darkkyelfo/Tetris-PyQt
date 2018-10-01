from numpy import random, where, abs


class Jogada(object):

    def __init__(self, rotacao, linha, coluna, valor=0):
        self.rotacao = rotacao
        self.linha = linha
        self.coluna = coluna
        self.valor = valor


class AvaliardorDeJogo(object):

    @staticmethod
    def alturaMaxima(gameBehavior):
        alturaMax = gameBehavior.board.shape[0]
        alturaDoCampo = where(gameBehavior.board.any(axis=1))[0][0]
        return alturaMax - alturaMax if alturaDoCampo.size == 0 else alturaDoCampo - 1

    @staticmethod
    def contarBuracos(gameBehavior):
        holes = 0
        for coluna in range(gameBehavior.board.shape[1]):
            diff = False
            for linha in range(gameBehavior.board.shape[0]):
                if gameBehavior.board[linha][coluna] != 0:
                    diff = True
                else:
                    if diff:
                        holes += 1
        return holes

    @staticmethod
    def contarBuracosConectados(gameBehavior):
        holes = 0
        for coluna in range(gameBehavior.board.shape[1]):
            diff = False
            for linha in range(gameBehavior.board.shape[0]):
                if gameBehavior.board[linha][coluna] != 0:
                    diff = True
                else:
                    if diff:
                        holes += 1
                        diff = False
        return holes

    @staticmethod
    def blocosSobreBuracos(gameBehavior):
        board = gameBehavior.board[1:-1, :]
        blocos = 0
        posicoes = where(board != 0)
        for i, linha in enumerate(posicoes[0]):
            coluna = posicoes[1][i]
            if (gameBehavior.board[linha + 2][coluna] == 0):
                blocos += 1
        return blocos

    @staticmethod
    def contarPocos(gameBehavior):
        board = gameBehavior.board[:17, 1:-1]
        return 0

    @staticmethod
    def nivelamento(gameBehavior):
        board = gameBehavior.board
        colunaEsquerda = board[:, 0]
        colunaDireita = board[:, -1]
        altEsquerda = 0
        altDireita = 0
        if (colunaEsquerda.any()):
            altEsquerda = where(colunaEsquerda != 0)[0][0]
        if (colunaDireita.any()):
            altDireita = where(colunaDireita != 0)[0][0]
        return abs(altDireita - altEsquerda)

class IA(object):

    def __init__(self, qtGenes=6, genes=None):
        self.qtGenes = qtGenes
        if (genes == None):
            self.gerarGenes()
        else:
            self.genes = genes

    def gerarGenes(self):
        self.genes = random.random(self.qtGenes)

    def setGameBehavior(self, gameBehavior):
        self.__gameBehavior = gameBehavior

    def jogar(self):
        from sys import maxsize
        board = self.__gameBehavior.board
        while self.__gameBehavior.moverParaEsquerda():
            pass
        saveJogo = self.__gameBehavior.salvarEstado()
        peca = self.__gameBehavior.peca_atual
        valorMax = -maxsize - 1
        jogadaEscolhida = None
        for i in range(1, peca.rotacaoMax+1):
            peca.setRotaco(i)
            while True:
                posicaoJogada = self.__gameBehavior.posi_atual
                saveJogo.posicaoAtual = posicaoJogada
                self.__gameBehavior.dropPeca()
                self.__gameBehavior.fixarPeca()
                self.__gameBehavior.atualizarCampo()
                valor = self.__avaliarJogada()
                if (self.__avaliarJogada() > valorMax):
                    jogadaEscolhida = Jogada(peca.rotacao, posicaoJogada[0], posicaoJogada[1], valor)
                self.__gameBehavior.setEstado(saveJogo)
                if (self.__gameBehavior.moverParaDireita() == False):
                    break

        return jogadaEscolhida

    def __avaliarJogada(self):
        valorDaJogada = 0
        valorDaJogada += self.genes[0] * self.__gameBehavior.qtLinhasFeitas
        valorDaJogada -= self.genes[1] * AvaliardorDeJogo.alturaMaxima(self.__gameBehavior)
        valorDaJogada -= self.genes[2] * AvaliardorDeJogo.blocosSobreBuracos(self.__gameBehavior)
        valorDaJogada -= self.genes[3] * AvaliardorDeJogo.contarBuracos(self.__gameBehavior)
        valorDaJogada -= self.genes[4] * AvaliardorDeJogo.contarPocos(self.__gameBehavior)
        valorDaJogada -= self.genes[5] * AvaliardorDeJogo.nivelamento(self.__gameBehavior)
        return valorDaJogada
