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
BLACK = (0, 0, 0)
RED = (255, 0, 0)

def rendermap(map_data):
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Render Map')
    clock = pygame.time.Clock()

    player_pos = [0, 0]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                # Move the player based on arrow key inputs
                if event.key == K_UP and player_pos[1] > 0:
                    player_pos[1] -= 1
                elif event.key == K_DOWN and player_pos[1] < len(map_data) - 1:
                    player_pos[1] += 1
                elif event.key == K_LEFT and player_pos[0] > 0:
                    player_pos[0] -= 1
                elif event.key == K_RIGHT and player_pos[0] < len(map_data[0]) - 1:
                    player_pos[0] += 1

        screen.fill(WHITE)
        for y, row in enumerate(map_data):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                if cell == 1:
                    pygame.draw.rect(screen, BLUE, rect)
                elif cell == 0:
                    pygame.draw.rect(screen, WHITE, rect)
                pygame.draw.rect(screen, BLACK, rect, 3)
        
        # Draw player
        player_rect = pygame.Rect(player_pos[0] * BLOCK_SIZE, player_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(screen, RED, player_rect)
        
        pygame.display.flip()
        clock.tick(30)

# Example usage
if __name__ == "__main__":
    from createmap import generatemap

    map_data = generatemap()
    rendermap(map_data)
