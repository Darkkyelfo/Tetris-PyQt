# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 18:33:18 2015

@author: Raul
"""

class Movimento():
    qualidade=0
    posX=None
    posY=None
    tipoPeca=None
    rotacao=None
    def __init__(self,posX,posY,tipoPeca,rotacao):
        self.posX=posX
        self.posY=posY
        self.tipoPeca=tipoPeca
        self.rotacao=rotacao