from gameBehavior import GameBehavior
from ia import Jogada


class Tetris(object):

    def __init__(self):
        self.gameBehavior = GameBehavior()

    def getScore(self):
        return self.gameBehavior.score

    def getTabuleiro(self):
        return self.gameBehavior.board

    def getPeca(self):
        return self.gameBehavior.peca_atual

    def setRotacaoPeca(self, rotacao):
        self.gameBehavior.peca_atual.setRotaco(rotacao)

    def getRotacaoPeca(self):
        return self.gameBehavior.peca_atual.rotacao

    def getLinhaAtual(self):
        return self.gameBehavior.posi_atual[0]

    def getColunaAtual(self):
        return self.gameBehavior.posi_atual[1]

    def jogoAcabou(self):
        return self.gameBehavior.jogoAcabou

    def moverEsquerda(self):
        self.gameBehavior.moverParaEsquerda()

    def moverDireita(self):
        self.gameBehavior.moverParaDireita()

    def drop(self):
        self.gameBehavior.dropPeca()

    def imprimirTabuleiro(self):
        print(self.getTabuleiro())
        print("__________________________________\n")

    def exibirGUI(self):
        pass


class TetrisIA(Tetris):

    def __init__(self, IA):
        super().__init__()
        self.IA = IA

    def iniciarJogo(self, imprimir=False, GUI=False):
        while self.jogoAcabou() != True:
            self.realizarJogada(imprimir)

    def realizarJogada(self,imprimir):
        jogada = Jogada(1, 19, 4)
        while True:
            if (imprimir):
                self.imprimirTabuleiro()
            movimentoAcabou = self.__jogadadParaMovimento(jogada)
            if (movimentoAcabou):
                break

    def __jogadadParaMovimento(self, jogada):
        c = self.getColunaAtual()
        if (self.getRotacaoPeca() != jogada.rotacao):
            self.setRotacaoPeca(jogada.rotacao)
            return False

        if (jogada.coluna < self.getColunaAtual()):
            self.moverEsquerda()
            return False

        elif (jogada.coluna > self.getColunaAtual()):
            self.moverDireita()
            return False

        else:
            self.drop()
            return True
