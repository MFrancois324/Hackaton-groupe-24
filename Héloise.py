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


def move(position, plateau, event):
    # Déplace le joueur en fonction de l'événement clavier
    x, y = position

    if (event.key == pygame.K_LEFT and pos_possible((x-20,y), plateau)==True) :  # Flèche gauche
        x -= 20
    elif (event.key == pygame.K_RIGHT and pos_possible((x+20,y),plateau)== True):  # Flèche droite
        x += 20
    elif (event.key == pygame.K_UP and pos_possible((x,y-20), plateau)== True):  # Flèche haut
        y -= 20
    elif (event.key == pygame.K_DOWN and pos_possible((x,y+20), plateau)==True):  # Flèche bas
        y += 20

    return ((x, y))




def check(pos):
    x,y=pos[0],pos[1]
    return x>=0 and x<W and y>=0 and y<H


def pos_possible(pos,plateau):
    autorisé=['.','#','+','=']
    interdit=['|','-','@']

    