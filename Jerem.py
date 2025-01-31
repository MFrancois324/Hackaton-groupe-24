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
W=20
H=20
global SCREEN, CLOCK
blockSize = 20 #Set the size of the grid block
pos = (1,1)

BACKGROUND = np.array([['|',".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".",".","|"]for _ in range (20)])
BACKGROUND [0], BACKGROUND [19]= ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-'], ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
BACKGROUND [pos[0]][pos[1]]='@'
BACKGROUND [3][19]='='

PLATEAU = BACKGROUND.copy()



def move(plateau, event):
    # Déplace le joueur en fonction de l'événement clavier
    global pos
    x, y = pos
    print(event.key)
    if (event.key == pygame.K_LEFT and pos_possible((x-1,y), plateau)==True) :  # Flèche gauche
        y -= 1
    elif (event.key == pygame.K_RIGHT and pos_possible((x+1,y),plateau)== True):  # Flèche droite
        y += 1
    elif (event.key == pygame.K_UP and pos_possible((x,y-1), plateau)== True):  # Flèche haut
        x -= 1
    elif (event.key == pygame.K_DOWN and pos_possible((x,y+1), plateau)==True):  # Flèche bas
        x += 1
    plateau[pos[0]][pos[1]]=BACKGROUND[x][y]
    pos = (x,y)
    plateau[x][y]='@'



def check(pos):
    x,y=pos[0],pos[1]
    return x>=0 and x<W and y>=0 and y<H


def pos_possible(pos,plateau):
    autorisé=['.','#','+','=']
    interdit=['|','-','@']
    x,y=pos[0],pos[1]
    
    if check((x,y)) and (plateau[x][y] in autorisé):
        return True
    else :
        return False

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

### LA FONCTION AFFICHAGE ###

def drawGrid():
    for i in range (20):
        for j in range (20):
            if PLATEAU[i][j]=='|':
                SCREEN.blit(MUR_VERT,(j*blockSize,i*blockSize))
            if PLATEAU[i][j]=='.':
                SCREEN.blit(POINT,(j*blockSize,i*blockSize))
            if PLATEAU[i][j]=='#':
                SCREEN.blit(COULOIR,(j*blockSize,i*blockSize))
            if PLATEAU[i][j]=='+':
                SCREEN.blit(PORTE,(j*blockSize,i*blockSize))
            if PLATEAU[i][j]=='-':
                SCREEN.blit(MUR_HOR,(j*blockSize,i*blockSize))
            if PLATEAU[i][j]=='@':
                SCREEN.blit(PERSO,(j*blockSize,i*blockSize))
            if PLATEAU[i][j]=='=':
                SCREEN.blit(ESCALIER,(j*blockSize,i*blockSize))


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
        if event.type == KEYDOWN:
            move(PLATEAU,event)
        #print(PLATEAU)
        pygame.display.update()
    pygame.time.delay(100)

