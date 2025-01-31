#Vincent
import numpy as np

matrice = np.array([['|',".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","|"]for _ in range (20)])



# Fonction affichage


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg 

from pygame.locals import *
import pygame, sys
# Initialisation

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_WIDTH=400
WINDOW_HEIGHT=400
global SCREEN, CLOCK

pygame.init()
SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
CLOCK = pygame.time.Clock()
SCREEN.fill(BLACK)

font = pygame.font.Font(None, 30)
POINT=font.render(".",True,WHITE)
COULOIR=font.render("#",True,WHITE)
MUR_VERT=font.render("|",True,WHITE)
MUR_HOR=font.render("-",True,WHITE)
PORTE=font.render("+",True,WHITE)
ESCALIER=font.render("=",True,WHITE)
PERSO=font.render("@",True,WHITE)


font = pygame.font.Font(None, 30)  # Police par défaut, taille 74
POINT=font.render(".",True,WHITE)

### LA FONCTION AFFICHAGE ###

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for i in range (20):
        for j in range (20):
            if matrice[i][j]=='|':
                SCREEN.blit(MUR_VERT,(j*blockSize,i*blockSize))
            if matrice[i][j]=='.':
                SCREEN.blit(POINT,(j*blockSize,i*blockSize))
            if matrice[i][j]=='#':
                SCREEN.blit(COULOIR,(j*blockSize,i*blockSize))
            if matrice[i][j]=='+':
                SCREEN.blit(PORTE,(j*blockSize,i*blockSize))
            if matrice[i][j]=='-':
                SCREEN.blit(MUR_HOR,(j*blockSize,i*blockSize))






#La boucle de jeu principale
while True:
    drawGrid()
    sysFont = pygame.font.SysFont("None", 32)
    #rendered = sysFont.render('Hello World', 0, (255,100, 100))
    #SCREEN.blit(rendered, (WINDOW_HEIGHT, WINDOW_HEIGHT))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()

