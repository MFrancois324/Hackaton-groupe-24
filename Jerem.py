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
WINDOW_HEIGHT=440
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
    if (event.key == pygame.K_LEFT and pos_possible((x,y-1), plateau)==True) :  # Flèche gauche
        y -= 1
    elif (event.key == pygame.K_RIGHT and pos_possible((x,y+1),plateau)== True):  # Flèche droite
        y += 1
    elif (event.key == pygame.K_UP and pos_possible((x-1,y), plateau)== True):  # Flèche haut
        x -= 1
    elif (event.key == pygame.K_DOWN and pos_possible((x+1,y), plateau)==True):  # Flèche bas
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


#Barre d'état
Or=0
Pv=0
Lvl=1
GOLD=(255,215,0)
AFFICHE_OR=font.render("Gold : ",True,GOLD)
AFFICHE_OR1=font.render(str(Or),True,GOLD)
AFFICHE_PV=font.render("PV : ",True,GOLD)
AFFICHE_PV1=font.render(str(Pv),True,GOLD)
AFFICHE_LEVEL=font.render("Level :",True,GOLD)
AFFICHE_LEVEL1=font.render(str(Lvl),True,GOLD)


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
    SCREEN.blit(AFFICHE_LEVEL,(0,21*blockSize))
    SCREEN.blit(AFFICHE_OR,(8*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_PV,(15*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_LEVEL1,(4*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_OR1,(12*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_PV1,(18*blockSize,21*blockSize))

#La boucle de jeu principale
while True:
    SCREEN.fill(BLACK)
    drawGrid()
    sysFont = pygame.font.SysFont("None", 32)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            move(PLATEAU,event)
        #print(PLATEAU)
        pygame.display.update()
    pygame.time.delay(100)

