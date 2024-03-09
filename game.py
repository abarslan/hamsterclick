import pygame
from pygame.locals import *
import sys
from createmap import generatemap 
from rendermap import startgraphic
game_running=1

while game_running:
    if __name__ == "__main__":
        map_data, startpoint = generatemap()
        startgraphic(map_data, startpoint)
        break
__name__
