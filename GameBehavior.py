# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 12:39:49 2015

@author: Raul
"""
#Essa classe é resposanvel pelo comportamento do jogo
#Nela que acontece a conexão com a GUI
#Também onde estão escritas as regras do jogo

from campoTetris import Ui_MainWindow
from PyQt4 import QtGui, QtCore
import blocos_rc
from Peca import Peca


class GameBehavior(QtGui.QMainWindow,Ui_MainWindow):
    pecaAtual=None
    def __init__(self,parent=None):
        super(GameBehavior, self).__init__(parent)
        self.setupUi(self)
        self.pecaAtual = Peca(self.centralwidget,self.width(),self.height())
        self.widget_2=self.pecaAtual
        self.show()
        
    #funçao que receve eventos do teclado
    def keyPressEvent(self, event):
        key = event.key()
        if(key == QtCore.Qt.Key_Right):
            self.pecaAtual.moverDir()
        if(key ==QtCore.Qt.Key_Left):
            self.pecaAtual.moverEsq()
        if(key ==QtCore.Qt.Key_Down):
            self.pecaAtual.cairPeca()
        if(key ==QtCore.Qt.Key_Up):
            self.pecaAtual.subirPeca()
            
        self.update()#Atualiza a GUI
        



    



       

    

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = GameBehavior()
    #av.show()
    sys.exit(app.exec_())
    