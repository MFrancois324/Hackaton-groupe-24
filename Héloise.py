"""
def move(pose): 
    #demande la direction souhaité par l'utilisateur et renvoie les nouvelle position du joueur en prenant en paramètre l'ancienne position
    x, y = pose 

    direction = input("Où voulez-vous aller ? (gauche= g, droite= d, haut= h, bas= b) ")

    if direction == "g": 
        x -= 1
    elif direction == "d": 
        x += 1
    elif direction == "h":
        y += 1
    elif direction == "b": 
        y -= 1
    else:
        print("Direction invalide.")

    return (x, y)


position = (1, 1) # Position initiale
new_pos = move(position)


print(f"Ancienne position : {position}")
print(f"Nouvelle position : {new_pos}")
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pygame as pg 

from pygame.locals import *
import pygame, sys
# Initialisation
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('MiniRogue')
#La boucle de jeu principale
while True:
    sysFont = pygame.font.SysFont("None", 32)
    rendered = sysFont.render('Hello World', 0, (255,100, 100))
    screen.blit(rendered, (100, 100))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.update()





def move(position, event):
    # Déplace le joueur en fonction de l'événement clavier
    x, y = position

    if event.key == pygame.K_LEFT:  # Flèche gauche
        x -= 1
    elif event.key == pygame.K_RIGHT:  # Flèche droite
        x += 1
    elif event.key == pygame.K_UP:  # Flèche haut
        y -= 1
    elif event.key == pygame.K_DOWN:  # Flèche bas
        y += 1

    return ((x, y))
