import Board as bd
import pygame
from pygame.locals import*

#constants
WIDTH  = 400
HEIGHT = 800

#init pygame and set up window
pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Master Mind")

#init board
board = bd.Board(4, 10)

#main loop
run = True
while run:

    #check for events
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    
    #draw
    board.draw(window)
    pygame.display.update()

#quit pygame
pygame.quit()
