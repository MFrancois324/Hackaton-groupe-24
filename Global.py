import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg 
import random as rd

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
MONEY=font.render("*",True,WHITE)

#Barre d'état
Or=0
Pv=0
Lvl=1
GOLD=(255,215,0)
AFFICHE_OR=font.render("Gold : ",True,GOLD)
AFFICHE_PV=font.render("PV : ",True,GOLD)
AFFICHE_LEVEL=font.render("Level :",True,GOLD)



### LA FONCTION AFFICHAGE ###
def etage_1(): 
    matrice = np.zeros ((20,20),dtype=str)
    matrice[0] = ['-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-']
    matrice[1] = ['|','.','.','.','+','#','#','#','#','#','+','.','.','.','.','.','|','','','|']
    matrice[2] = ['|','.','.','.','|','','','','','','|','.','.','.','.','.','|','-','-','|']
    matrice[3] = ['|','.','.','.','|','','','','','','|','.','.','.','.','.','.','.','.','|']
    matrice[4] = ['|','.','.','.','|','','','','','','|','-','-','-','-','+','-','-','-','|']
    matrice[5] = ['|','.','.','.','+','#','#','','','','','','','','','#','','','','|']
    matrice[6] = ['|','-','+','-','-','','#','','|','-','-','-','-','','','#','','','','|']
    matrice[7] = ['|','','#','','','','#','','|','.','.','.','.','|','','#','','','','|']
    matrice[8] = ['|','','#','','','','#','#','+','.','.','.','.','|','-','+','-','-','-','|']
    matrice[9] = ['|','','#','','','','','','|','-','-','-','-','|','|','.','.','.','.','|']

    matrice_bas= np.array([["|","-","+","-","-","-","-","-","|","","","","","","|",".",".",".",".","|"],
        ["|",".",".",".",".",".",".",".","|","","","","","","|",".",".",".",".","|"] ,
        ["|",".",".",".",".",".",".",".","+","#","#","#","#","","|",".",".","=",".","|"],
        ["|",".",".",".",".",".",".",".","|","","","","#","","|",".",".",".",".","|"],
        ["|","-","-","+","-","|","=",".","|","","","","#","#","+",".",".",".",".","|"],
        ["|","","","#","","|",".",".","|","","","","","","|",".",".",".",".","|"],
        ["|","","","#","","|","-","-","-","","","","","","|","-","-","+","-","|"],
        ["|","-","-","+","-","-","-","-","-","-","-","-","-","-","|","","#","#","","|"],
        ["|",".",".",".",".",".",".",".",".",".",".",".",".",".","+","#","#","","","|"],
    ["|","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","-","|"]])



    return np.vstack((matrice[:10],matrice_bas))

def etage_2():
    matrice = np.transpose(etage_1())
    return matrice

def generate_gold(matrice):
    """
    Remplace aléatoirement 10% des points dans la matrice par de l'or ('*').
    Les points sont initialement des '.'.
    """
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):
            if matrice[i][j] == '.':  # Si c'est un point
                if rd.random() < 0.1:  # 10% de chance de devenir de l'or
                    matrice[i][j] = '*'  # Remplacer le point par de l'or
    return matrice


BACKGROUND = etage_1()
PLATEAU = BACKGROUND.copy()
PLATEAU[pos[0]][pos[1]]='@'
generate_gold(PLATEAU)

def drawGrid():
    AFFICHE_OR1=font.render(str(Or),True,GOLD)
    AFFICHE_PV1=font.render(str(Pv),True,GOLD)
    AFFICHE_LEVEL1=font.render(str(Lvl),True,GOLD)
    blockSize = 20 #Set the size of the grid block
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
            if PLATEAU[i][j]=='*':
                SCREEN.blit(MONEY,(j*blockSize,i*blockSize))
    SCREEN.blit(AFFICHE_LEVEL,(0,21*blockSize))
    SCREEN.blit(AFFICHE_OR,(8*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_PV,(15*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_LEVEL1,(4*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_OR1,(12*blockSize,21*blockSize))
    SCREEN.blit(AFFICHE_PV1,(18*blockSize,21*blockSize))

def move(plateau, event):
    # Déplace le joueur en fonction de l'événement clavier
    global pos
    global Lvl
    global Or
    x, y = pos
    if (event.key == pygame.K_LEFT and pos_possible((x,y-1), plateau)==True) :  # Flèche gauche
        y -= 1
    elif (event.key == pygame.K_RIGHT and pos_possible((x,y+1),plateau)== True):  # Flèche droite
        y += 1
    elif (event.key == pygame.K_UP and pos_possible((x-1,y), plateau)== True):  # Flèche haut
        x -= 1
    elif (event.key == pygame.K_DOWN and pos_possible((x+1,y), plateau)==True):  # Flèche bas
        x += 1
    plateau[pos[0]][pos[1]]=BACKGROUND[pos[0]][pos[1]]
    pos = (x,y)
    if BACKGROUND[x][y]=='=':
        Lvl +=1
    elif BACKGROUND[x][y]=='*':
        Or +=10
        BACKGROUND[x][y]=="."
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
        pygame.display.update()
    pygame.time.delay(100)

