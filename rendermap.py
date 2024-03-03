import pygame
from pygame.locals import *
import sys 
# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
BLOCK_SIZE = 200
FRAME_THICKNESS = 3
# Colors
WHITE = (255, 255, 255)
BLUE = (93, 71, 237)
BLACK = (0, 0, 0)
RED = (255, 145, 0)
ORANGE = (255, 0, 0)
def startgraphic(map_data, startpoint):
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Render Map')
    clock = pygame.time.Clock()

    player_pos = [startpoint, 0]
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not game_over:
                # Check if the mouse click is inside a block
                x, y = pygame.mouse.get_pos()
                clicked_column = x // BLOCK_SIZE
                clicked_row = y // BLOCK_SIZE
                # Update player position if clicked inside the map
                if 0 <= clicked_column < len(map_data[0]) and 0 <= clicked_row < len(map_data):
                    if map_data[clicked_row][clicked_column] == 0:
                        game_over = True
                    else:
                        player_pos = [clicked_column, clicked_row]

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
        pygame.draw.rect(screen, BLACK, player_rect, 3)
        
        
        
        if game_over:
            # Draw game over text
            font = pygame.font.SysFont(None, 90)
            game_over_text = font.render('GAME OVER', True, ORANGE)
            screen.blit(game_over_text, ((WINDOW_WIDTH - game_over_text.get_width()) // 2, (WINDOW_HEIGHT - game_over_text.get_height()) // 2))
        
        pygame.display.flip()
        clock.tick(30)
