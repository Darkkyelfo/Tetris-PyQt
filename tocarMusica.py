import sys
sys.path.append("musica")

import pygame.mixer
def tocarMusica(tocar):
    if(tocar):
        pygame.mixer.init()
        pygame.mixer.music.load(open("musica/Original Tetris theme (Tetris Soundtrack).mp3","rb"))
        pygame.mixer.music.play(-1)


