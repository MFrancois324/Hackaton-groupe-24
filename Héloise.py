import numpy
import pygame
import random as rd
import sys



###### Partie Monstre fixe #######

def generate_monster(matrice):
    """
    Remplace aléatoirement 10% des points dans la matrice par de l'or ('*').
    Les points sont initialement des '.'.
    """
    for i in range(matrice.shape[0]):
        for j in range(matrice.shape[1]):
            if matrice[i][j] == '.':  # Si c'est un point
                if rd.random() < 0.1:  # 10% de chance de devenir un monstre
                    matrice[i][j] = 'M'  # Remplacer le point par un monstre
    return matrice

def compte_points_monstre_fixe(matrice, position) :
    i,j = position[0], position[1]
    if matrice[i+1][j]=="M" or matrice[i-1][j]=="M" or matrice[i][j+1]=="M" or matrice[i][j-1]=="M" :
        Pv-=10
        if Pv==0 : 
            print("Game Over")
        
def tuer_monstre(matrice, position) :
    
    i,j = position[0],position[1]
    if (event.key == pygame.K_LEFT and matrice[i-1][j]=="M" or matrice[i-1][j]=="K") :  # Flèche gauche pour tuer le monstre 
        if rd.random() < 0.5:
           matrice[i-1][j]=="."    # monstre tué 
           Pv+=30   # gagne des vies

    if (event.key == pygame.K_RIGHT and matrice[i+1][j]=="M" or matrice[i+1][j]=="K") :  # Flèche gauche pour tuer le monstre 
        if rd.random() < 0.5:
           matrice[i+1][j]=="."    # monstre tué 
           Pv+=30   # gagne des vies

    if (event.key == pygame.K_UP and matrice[i][j+1]=="M" ormatrice[i][j+1]=="K") :  # Flèche gauche pour tuer le monstre 
        if rd.random() < 0.5:
           matrice[i][j+1]=="."    # monstre tué 
           Pv+=30   # gagne des vies

        
    if (event.key == pygame.K_DOWN and matrice[i][j-1]=="M" or matrice[i][j-1]=="K") :  # Flèche gauche pour tuer le monstre 
        if rd.random() < 0.5:
           matrice[i][j-1]=="."    # monstre tué 
           Pv+=30   # gagne des vies

        