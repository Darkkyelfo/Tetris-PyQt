from numpy import zeros

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
        if (self.verificar_posicao_valida(self.posi_atual + l, self.posi_atual[1] + c, self.peca_atual)):
            self.__apagar_peca(self.posi_atual[0], self.posi_atual[1], self.peca_atual)
            self.__desenhar_peca(self.posi_atual[0], self.posi_atual[1], self.peca_atual)
            self.posi_atual = (self.posi_atual + l, self.posi_atual[1] + c)
        else:
            self.__porNovaPeca()

    def moverParaBaixo(self):
        self.__moverPeca(1)

    def moverParaDireita(self):
        self.__moverPeca(c=-1)

    def moverParaEsquerda(self):
        self.__moverPeca(c=1)
