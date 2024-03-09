import pygame
from pygame.locals import *
import sys
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 860
BLOCK_SIZE = 200
# Colors
WHITE = (255, 255, 255)
BLUE = (93, 71, 237)
BLACK = (0, 0, 0)
RED = (255, 145, 0)
ORANGE = (255, 0, 0)
GREEN = (30, 214, 162)

def save_highest_score(score):
    try:
        with open("highest_score.txt", "r") as file:
            highest_score = int(file.read())
    except FileNotFoundError:
        highest_score = 0

    if score > highest_score:
        with open("highest_score.txt", "w") as file:
            file.write(str(score))

def startgraphic(map_data, startpoint):
    pygame.init()

    font_path = 'newfont.ttf'
    font = pygame.font.Font(font_path, 24)
    fontdied = pygame.font.Font(font_path, 50)
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Hamsterclick')
    clock = pygame.time.Clock()

    player_pos = [startpoint, 0]
    game_over = False
    green_square = None
    last_green_time = 0
    squares_chosen = 0
    squares_chosen_timer = 0
    total_square = 0
    squares_chosen_timer5 = 0

    # Load images
    map_image = pygame.image.load('grass.png')
    player_image = pygame.image.load('player.png')
    green_square_image = pygame.image.load('green.png')
    empty_cell_image = pygame.image.load('empty.png')  # Load image for empty cells

    # Resize images to match block size if needed
    map_image = pygame.transform.scale(map_image, (BLOCK_SIZE, BLOCK_SIZE))
    player_image = pygame.transform.scale(player_image, (BLOCK_SIZE, BLOCK_SIZE))
    green_square_image = pygame.transform.scale(green_square_image, (BLOCK_SIZE, BLOCK_SIZE))
    empty_cell_image = pygame.transform.scale(empty_cell_image, (BLOCK_SIZE, BLOCK_SIZE))

    while True:
        current_time = pygame.time.get_ticks()
        squares_chosen_timer += clock.get_time()  # Update the timer
        squares_chosen_timer5 += clock.get_time()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and not game_over:
                x, y = pygame.mouse.get_pos()
                # Adjust mouse coordinates for the gold rectangle
                y -= 60
                clicked_column = x // BLOCK_SIZE
                clicked_row = y // BLOCK_SIZE
                if 0 <= clicked_column < len(map_data[0]) and 0 <= clicked_row < len(map_data):
                    if map_data[clicked_row][clicked_column] == 0:
                        game_over = True
                    elif green_square and green_square.collidepoint(x, y):
                        if current_time - last_green_time <= 1000:
                            # Clicked on the green square within 1 second
                            player_pos = [clicked_column, clicked_row]
                            green_square = None
                            total_square += 1  # Increment the counter
                            squares_chosen += 1
                        else:
                            game_over = True

        if not green_square or current_time - last_green_time >= 1000:
            while not green_square or map_data[green_square.y // BLOCK_SIZE][green_square.x // BLOCK_SIZE] == 0:
                random_column = random.randint(0, len(map_data[0]) - 1)
                random_row = random.randint(0, len(map_data) - 1)
                green_square = pygame.Rect(random_column * BLOCK_SIZE, random_row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            last_green_time = current_time

        # Draw gold background for counters
        gold_rect_height = 60  # Adjust the height of the gold rectangle
        gold_rect = pygame.Rect(0, 0, WINDOW_WIDTH, gold_rect_height)
        gold_surface = pygame.Surface((WINDOW_WIDTH, gold_rect_height), pygame.SRCALPHA)  # Create a surface with alpha channel
        gold_surface.fill((148, 138, 0,170))  # Fill the surface with gold color and set transparency (128 is half opaque)
        screen.blit(gold_surface, (0, 0))  # Blit the gold surface onto the screen
        
        # Draw the map
        map_offset_y = gold_rect_height  # Adjusted Y coordinate for the map
        for y, row in enumerate(map_data):
            for x, cell in enumerate(row):
                rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE + map_offset_y, BLOCK_SIZE, BLOCK_SIZE)
                if cell == 1:
                    screen.blit(map_image, rect)
                elif cell == 0:
                    screen.blit(empty_cell_image, rect)  # Render image for empty cells

        # Draw player
        player_rect = pygame.Rect(player_pos[0] * BLOCK_SIZE, player_pos[1] * BLOCK_SIZE + map_offset_y, BLOCK_SIZE, BLOCK_SIZE)
        screen.blit(player_image, player_rect)

        # Draw the randomly chosen square if it exists
        if green_square:
            green_square_rect = pygame.Rect(green_square.x, green_square.y + map_offset_y, BLOCK_SIZE, BLOCK_SIZE)
            screen.blit(green_square_image, green_square_rect)

        # Draw counter
        counter_text = font.render("SCORE: " + str(total_square), True, BLACK)
        counter_text_rect = counter_text.get_rect(midtop=(WINDOW_WIDTH // 2, 8))  # Adjusted the Y coordinate
        screen.blit(counter_text, counter_text_rect)    

        # Draw time left
        time_left = max(0, 30 - squares_chosen_timer // 1000)  # Convert milliseconds to seconds
        time_left_text = font.render("TIME LEFT: " + str(time_left) + " s", True, BLACK)
        time_left_text_rect = time_left_text.get_rect(midtop=(WINDOW_WIDTH // 2, 35))  # Adjusted the Y coordinate
        screen.blit(time_left_text, time_left_text_rect)

        if squares_chosen_timer5 >= 5000 and squares_chosen_timer5 <= 30000 :  # Check if 5 second has passed
            print("Score in last 5 second:", squares_chosen)
            squares_chosen_timer5 = 0  # Reset the timer
            squares_chosen = 0  # Reset the counter

            
        if squares_chosen_timer > 30000:  # Check if 1 min has passed
            print("TOTAL SCORE:", total_square)
            save_highest_score(total_square)
            squares_chosen_timer = 0  # Reset the timer
            total_square = 0  # Reset the counter
            game_over = True

        if game_over:
            game_over_text = fontdied.render('GAME OVER', True, ORANGE)
            game_over_text_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))  # Centered the text
            screen.blit(game_over_text, game_over_text_rect)
            return total_square
           

        pygame.display.flip()
        clock.tick(30)

# Example usage
# Assuming map_data and startpoint are initialized somewhere before calling startgraphic
# startgraphic(map_data, startpoint)
