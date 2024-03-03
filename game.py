import pygame
from pygame.locals import *
import sys
from createmap import generatemap  # Assuming createmap.py contains the generatemap function
from rendermap import startgraphic

# Example usage
if __name__ == "__main__":
    map_data, startpoint = generatemap()
    startgraphic(map_data, startpoint)
