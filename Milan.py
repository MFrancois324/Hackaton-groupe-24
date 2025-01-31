#Milan
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg 

H=10
W=10
pos=(0,0)

def check(pos):
    x,y=pos[0],pos[1]
    return x>=0 and x<WINDOW_HEIGHT and y>=0 and y<WINDOW_WIDTH

def pos_possible(pos,plateau):
    autorisé=['.','#','+','=']
    interdit=['|','-','@']
    x,y=pos[0],pos[1]
    
    if plateau[x][y] in autorisé:
        return True
    else :
        return False
    
# Fonction d'affichage 
def affiche(matrix): 
    for row in matrix:
        print("".join(row))  # Joint les éléments de la ligne en une seule chaîne

matrice = np.array([['|',".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","|"]for _ in range (20)])



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

# Créer une police
font = pygame.font.Font(None, 30)  # Police par défaut, taille 74
POINT=font.render(".",True,WHITE)
COULOIR=font.render("#",True,WHITE)
MUR_VERT=font.render("|",True,WHITE)
MUR_HOR=font.render("-",True,WHITE)
PORTE=font.render("+",True,WHITE)
ESCALIER=font.render("=",True,WHITE)
PERSO=font.render("@",True,WHITE)

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            #rect = pygame.Rect(x, y, blockSize, blockSize)
            #pygame.draw.rect(SCREEN, WHITE, rect, 1)
            if x==blockSize:
                SCREEN.blit(PERSO,(x,y))
            else:
                SCREEN.blit(COULOIR,(x,y))
            

#La boucle de jeu principale
while True:
    drawGrid()
    sysFont = pygame.font.SysFont("None", 32)
    #rendered = sysFont.render('Hello World', 0, WHITE)
    #SCREEN.blit(POINT,(10,10))
    #SCREEN.blit(rendered, (WINDOW_HEIGHT, WINDOW_HEIGHT))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()


