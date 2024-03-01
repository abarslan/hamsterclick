import pygame
from pygame.locals import *
import sys 
# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BLOCK_SIZE = 200

# Colors
WHITE = (255, 255, 255)
BLUE = (93, 71, 237)
BLACK = (199, 87, 255)

def rendermap(map):
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Render Map')
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(WHITE)
        for y in range(4):
            for x in range(4):
                    rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                    pygame.draw.rect(screen, BLUE, rect)
                    pygame.draw.rect(screen, BLACK, rect, 3)
        pygame.display.flip()
        clock.tick(30)
