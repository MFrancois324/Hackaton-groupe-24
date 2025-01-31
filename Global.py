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