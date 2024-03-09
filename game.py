import pygame
import sys
from pygame.locals import USEREVENT
from pygame_gui.elements.ui_button import UIButton
import pygame_gui
from createmap import generatemap
from rendermap import startgraphic

# Initialize pygame
pygame.init()
green_square_image = pygame.image.load('green.png')
# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hamsterclick')

# Create a UIManager object
ui_manager = pygame_gui.UIManager((screen_width, screen_height))

# Function to start the game
def start_game():
    global last_score, highest_score
    map_data, startpoint = generatemap()
    last_score = startgraphic(map_data, startpoint)
    # Update highest score if necessary
    if last_score > highest_score:
        highest_score = last_score

# Function to quit the game
def quit_game():
    pygame.quit()
    sys.exit()

# Read the highest score from file
try:
    with open("highest_score.txt", "r") as file:
        highest_score = int(file.read())
except FileNotFoundError:
    highest_score = 0

# Variable to store the last score
last_score = 0

# Create buttons for the menu
start_button = UIButton(relative_rect=pygame.Rect((300, 200), (200, 50)),
                        text='Start Game',
                        manager=ui_manager)

quit_button = UIButton(relative_rect=pygame.Rect((300, 300), (200, 50)),
                       text='Quit',
                       manager=ui_manager)

lastscore_button = UIButton(relative_rect=pygame.Rect((300, 400), (200, 50)),
                            text='Last score: ' + str(last_score),
                            manager=ui_manager)

highest_score_button = UIButton(relative_rect=pygame.Rect((300, 500), (200, 50)),
                                text='Highest Score: ' + str(highest_score),
                                manager=ui_manager)

# Game loop
clock = pygame.time.Clock()
game_running = True
while game_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

        if event.type == USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    start_game()
                elif event.ui_element == quit_button:
                    quit_game()

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    scaled_image = pygame.transform.scale(green_square_image, (screen_width, screen_height))

    # Draw the scaled image
    screen.blit(scaled_image, (0, 0))

    ui_manager.draw_ui(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
