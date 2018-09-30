from numpy import random
class Jogada(object):

    def __init__(self, rotacao, linha, coluna):
        self.rotacao = rotacao
        self.linha = linha
        self.coluna = coluna

class avaliardorDeCampo(object):
    pass

class avaliadorDeIa(object):
    pass

class IA(object):

    def __init__(self,qtGenes = 6,genes = None):
        self.qtGenes = qtGenes
        if(genes==None):
            self.gerarGenes()
        self.genes = genes

    def gerarGenes(self):
        self.genes = random.random(self.qtGenes)

    def __escolherJogada(self):
        pass

    def jogar(self):
        pass




