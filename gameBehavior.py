from numpy import zeros, where, copy
from pecas import ControladorPecas


class EstadoJogo(object):

    def __init__(self, campo, indiceControlador,posicaoAtual,score):
        self.campo = campo
        self.indiceControlador = indiceControlador
        self.posicaoAtual = posicaoAtual
        self.score = score


class GameBehavior(object):

    def __init__(self):

        self.board = zeros((20, 10))
        self.score = 0
        self.posi_inicial = (1, 5)
        self.posi_atual = [self.posi_inicial[0], self.posi_inicial[1]]
        self.jogoAcabou = False
        self.peca_atual = None

    def iniciar(self, seed=None):
        self._controladorPeca = ControladorPecas(1000000, seed)
        self.__porNovaPeca()

    def __porNovaPeca(self):
        self.atualizarCampo()
        self.verificarJogoAcabou()
        if (self.jogoAcabou == False):
            self.peca_atual = self._controladorPeca.darPeca()
            self.__desenhar_peca(self.posi_inicial[0], self.posi_inicial[1], self.peca_atual)
            self.posi_atual[0] = self.posi_inicial[0]
            self.posi_atual[1] = self.posi_inicial[1]

    def __desenhar_peca(self, linha, coluna, peca):
        matriz_peca = peca.getPeca()
        for elementos in matriz_peca:
            self.board[linha + elementos[0]][coluna + elementos[1]] = peca.getTipoTrans()

    def __apagar_peca(self, linha, coluna, peca):
        matriz_peca = peca.getPeca()
        for elementos in matriz_peca:
            self.board[linha + elementos[0]][coluna + elementos[1]] = 0

    def verificar_posicao_valida(self, linha, coluna, peca):
        try:
            matriz_peca = peca.getPeca()
            for elementos in matriz_peca:
                if (self.board[linha + elementos[0]][coluna + elementos[1]] > 0):
                    return False
            return True
        except IndexError:
            return False

    def __moverPeca(self, l=0, c=0):
        self.__apagar_peca(self.posi_atual[0], self.posi_atual[1], self.peca_atual)
        self.__desenhar_peca(self.posi_atual[0] + l, self.posi_atual[1] + c, self.peca_atual)
        self.posi_atual[0] = self.posi_atual[0] + l
        self.posi_atual[1] = self.posi_atual[1] + c

    def moverParaBaixo(self):
        if (self.verificar_posicao_valida(self.posi_atual[0] + 1, self.posi_atual[1], self.peca_atual)):
            self.__moverPeca(1)
            return True
        else:
            return False

    def moverParaDireita(self):
        if (self.verificar_posicao_valida(self.posi_atual[0], self.posi_atual[1] + 1, self.peca_atual)):
            self.__moverPeca(c=1)
            return True
        return False

    def moverParaEsquerda(self):
        if (self.verificar_posicao_valida(self.posi_atual[0], self.posi_atual[1] - 1, self.peca_atual)):
            self.__moverPeca(c=-1)
            return True
        return False

    def dropPeca(self):
        while True:
            if (self.moverParaBaixo() == False):
                break

    def finalizarMovimento(self):
        self.fixarPeca()
        self.__porNovaPeca()

    def getLinhasFeitas(self):
        return where(self.board.all(axis=1))

    def removerLinhasFeitas(self):
        linhasFeitas = self.linhasFeitas
        for i in linhasFeitas:
            self.board[i, :] = 0
        self.score += len(linhasFeitas)

    def __descerCampo(self, linha):
        for l in range(linha, self.board.shape[0]):
            if (l != self.board.shape[0] - 1):
                self.board[l, :] = 0
            else:
                self.board[l] = self.board[l + 1]

    def atualizarCampo(self):
        self.linhasFeitas = self.getLinhasFeitas()[0]
        if (self.linhasFeitas.size > 0):
            self.removerLinhasFeitas()
            for i in self.linhasFeitas:
                self.__descerCampo(i)
            self.atualizarCampo()

    def verificarJogoAcabou(self):
        if (False in (self.board[0, :] <= 0)):
            self.jogoAcabou = True

    def fixarPeca(self):
        if (self.peca_atual != None):
            matriz_peca = self.peca_atual.getPeca()
            for elementos in matriz_peca:
                self.board[self.posi_atual[0] + elementos[0]][
                    self.posi_atual[1] + elementos[1]] = self.peca_atual.getTipoFixo()

    def salvarEstado(self):
        return EstadoJogo(copy(self.board), self._controladorPeca._peca_atual,self.posi_atual,self.score)

    def setEstado(self, estado):
        self.board = copy(estado.campo)
        self._controladorPeca.setIndiceAtual(estado.indiceControlador)
        self.peca_atual = self._controladorPeca.darPeca()
        self.posi_atual = estado.posicaoAtual
        self.score = estado.score
