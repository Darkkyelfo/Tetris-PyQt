# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:17:01 2015

@author: Raul
"""
import threading

class ListaSincronizada():
    lista=None
    listaLock=None
    
    def __init__(self):
        self.lista=[]
        self.listaLock= threading.Lock()
    
    def add(self,elemento):
        self.listaLock.acquire()
        self.lista.append(elemento)
        self.listaLock.release()
        
    def apagarLista(self):
        self.lista=[]
    
    def remove(self,elemento):
        self.listaLock.acquire()
        self.lista.remove(elemento)
        self.listaLock.release()
    
    
    