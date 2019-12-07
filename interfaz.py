from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
from DE import *
from queens import Queen
import os
import re
import sys
from pathlib import Path
import pygame as pg

class Principal(QMainWindow):

    def __init__(self):
        super(Principal, self).__init__()
        loadUi('interfaz.ui',self)
        self.queens = 20
        self.iterations = 0
        self.individuos = 0
        self.StartButton.clicked.connect(self.draw_map)
        self.initialize_all()

    def initialize_all(self):
        self.QueenBox.addItem("05")
        self.QueenBox.addItem("08")
        self.QueenBox.addItem("10")
        self.QueenBox.addItem("12")
        self.QueenBox.addItem("20")
        self.QueenBox.addItem("32")
        self.QueenBox.addItem("40")
        self.QueenBox.addItem("50")
        self.IterBox.addItem("01000")
        self.IterBox.addItem("02000")
        self.IterBox.addItem("04000")
        self.IndBox.addItem("32")
        self.IndBox.addItem("50")
        self.IndBox.addItem("70")

    def draw_map(self):
        self.StartButton.hide()
        self.queens = int(self.QueenBox.currentText())
        #self.queens = 25
        self.iterations = int(self.IterBox.currentText())
        self.individuos = int(self.IndBox.currentText())
        q = Queen(self.queens)
        algoritmo = DE(self.individuos,self.iterations,self.queens,q)
        best = algoritmo.run()
        position = best[0]
        fitness = best[1]
        #position = [7, 17, 4, 11, 15, 19, 9, 16, 5, 3, 10, 0, 18, 14, 2, 13, 1, 12, 8, 6] 20 REINAS!!
        self.draw_queens(position)

    def draw_queens(self, board):
        self.close()
        if self.queens >= 32:
            size = 11
        else:
            size = 71
        t_size = size * self.queens
        pg.init()
        screen = pg.display.set_mode((t_size, t_size))
        screen.fill((255,255,255))
        self.draw_board(screen, size-1, board)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                        sys.exit()
            pg.display.flip()

    def draw_board(self,screen, space_size, board):
        for fila,i in enumerate(range(0,900,space_size + 1)):
           for columna,j in enumerate(range(0,900,space_size + 1)):
               if fila < self.queens and columna < self.queens:
                   if board[fila] == columna:
                       pg.draw.rect(screen,(145,68,2),pg.Rect(j, i, space_size, space_size), 0)
                   else:
                       pg.draw.rect(screen,(234,186,144),pg.Rect(j, i, space_size,space_size), 0)

app = QApplication(sys.argv)
ex2 = Principal()
ex2.setWindowTitle("N Queens")
ex2.show()
sys.exit(app.exec_())
