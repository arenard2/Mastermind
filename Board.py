import pygame
from pygame.locals import *

#colors
WHITE  = (255, 255, 255)
BLACK  = (0, 0, 0)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (160, 32, 240)

#board size
SQUARE_SIZE = 40

class Board:
    def __init__(self, size_x, size_y):
        self.x = size_x
        self.y = size_y
        self.board = self.setUpBoard()
    
    def setUpBoard(self):
        board = []
        for i in range(self.y):
            xboard = []
            for j in range(self.x):
                xboard.append(WHITE)
            board.append(xboard)
        return board
    
    def draw(self, window):
        x = 10
        y = 10
        for colors in self.board:
            for color in colors:
                rect = pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(window, color, rect)
                x += SQUARE_SIZE + 10
            y += SQUARE_SIZE + 10
            x = 10
