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
        self.setFixedSize(self.width(),self.height())
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
        self.IterBox.addItem("1000")
        self.IterBox.addItem("2000")
        self.IterBox.addItem("2500")
        self.IterBox.addItem("4000")
        self.IndBox.addItem("32")
        self.IndBox.addItem("40")
        self.IndBox.addItem("45")
        self.IndBox.addItem("50")
        self.put_image()

    def put_image(self):
        path = self.get_path_for_image()
        path = os.path.join(path, 'queen.jpg')
        print(path)
        width = self.image_label.frameGeometry().width() #X
        height = self.image_label.frameGeometry().height() #Y
        pixmap = QPixmap(path)
        pixmap = pixmap.scaled(width,height,QtCore.Qt.KeepAspectRatio)
        self.image_label.setPixmap(pixmap)

    def get_path_for_image(self):
        path = Path(os.getcwd())
        return path

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
        pg.init()
        pg.display.set_caption("Queens")
        screen = pg.display.set_mode((970, 970))
        size = round(970 / self.queens)
        screen.fill((255,255,255))
        self.draw_board(screen, size-1, board)
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                        sys.exit()
            pg.display.flip()

    def draw_board(self,screen, space_size, board):
        imagen = pg.image.load("dama.jpg")
        imagen = pg.transform.scale(imagen, (space_size,space_size))
        for fila,i in enumerate(range(0,970,space_size+1)):
           for columna,j in enumerate(range(0,970,space_size+1)):
               if fila < self.queens and columna < self.queens:
                   if board[fila] == columna:
                       pg.draw.rect(screen,(145,68,2),pg.Rect(j, i, space_size, space_size), 0)
                       screen.blit(imagen,(j,i))
                   else:
                       pg.draw.rect(screen,(234,186,144),pg.Rect(j, i, space_size,space_size), 0)
    



app = QApplication(sys.argv)
ex2 = Principal()
ex2.setWindowTitle("N Queens")
ex2.show()
sys.exit(app.exec_())
