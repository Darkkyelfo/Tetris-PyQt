from numpy import zeros

from pecas import ControladorPecas


class GameBehavior(object):

    def __init__(self):
        self._controladorPeca = ControladorPecas(1000000)
        self.board = zeros((22, 10))
        self.score = 0




