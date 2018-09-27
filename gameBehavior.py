from numpy import zeros, where

from pecas import ControladorPecas


class GameBehavior(object):

    def __init__(self):
        self._controladorPeca = ControladorPecas(1000000)
        self.board = zeros((20, 10))
        self.score = 0
        self.posi_inicial = (1, 5)
        self.posi_atual = self.posi_inicial

    def __porNovaPeca(self):
        self.peca_atual = self._controladorPeca.darPeca()
        self.__desenhar_peca(self.posi_inicial[0], self.posi_inicial[1], self.peca_atual)

    def __desenhar_peca(self, linha, coluna, peca):
        if (self.verificar_posicao_valida(linha, coluna, peca)):
            matriz_peca = peca.getPeca()
            for elementos in matriz_peca:
                self.board[linha + elementos[0]][coluna + elementos[1]] = peca.tipo

    def __apagar_peca(self, linha, coluna, peca):
        matriz_peca = peca.getPeca()
        for elementos in matriz_peca:
            self.board[linha + elementos[0]][coluna + elementos[1]] = 0

    def verificar_posicao_valida(self, linha, coluna, peca):
        try:
            matriz_peca = peca.getPeca()
            for elementos in matriz_peca:
                if (self.board[linha + elementos[0]][coluna + elementos[1]] != 0):
                    return False
            return True
        except IndexError:
            return False

    def __moverPeca(self, l=0, c=0):
        self.__apagar_peca(self.posi_atual[0], self.posi_atual[1], self.peca_atual)
        self.__desenhar_peca(self.posi_atual[0] + l, self.posi_atual[1] + c, self.peca_atual)
        self.posi_atual = (self.posi_atual[0] + l, self.posi_atual[1] + c)

    def moverParaBaixo(self):
        if (self.verificar_posicao_valida(self.posi_atual + 1, self.posi_atual[1], self.peca_atual)):
            self.__moverPeca(1)
        else:
            self.__porNovaPeca()

    def moverParaDireita(self):
        if (self.verificar_posicao_valida(self.posi_atual, self.posi_atual[1] - 1, self.peca_atual)):
            self.__moverPeca(c=-1)

    def moverParaEsquerda(self):
        if (self.verificar_posicao_valida(self.posi_atual, self.posi_atual[1] + 1, self.peca_atual)):
            self.__moverPeca(c=1)

    def dropPeca(self):
        while self.verificar_posicao_valida(self.posi_atual + 1, self.posi_atual[1], self.peca_atual):
            self.__moverPeca(1)
        self.__porNovaPeca()

    def getLinhasFeitas(self):
        return where(self.board.any(axis=1) == False)

    def removerLinhasFeitas(self):
        linhasFeitas = self.getLinhasFeitas()
        for i in linhasFeitas:
            self.board[i, :] = 0

    def __descerCampo(self, linha):
        for l in range(linha, self.board.shape[0]):
            if (l != self.board.shape[0] - 1):
                self.board[l, :] = 0
            else:
                self.board[l] = self.board[l + 1]

    def atualizarCampo(self):
        self.removerLinhasFeitas()
        for i in self.getLinhasFeitas():
            self.__descerCampo(i)