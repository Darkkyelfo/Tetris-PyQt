from gameBehavior import GameBehavior

class Tetris(object):
    def __init__(self):
        self.gameBehavior = GameBehavior()

    def getScore(self):
        return self.gameBehavior.score
