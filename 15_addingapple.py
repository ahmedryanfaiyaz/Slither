"""
Created on 10/15/2021
@author: Ahmed Ryan
"""

import pygame
import time
import random

# initializing pygame
pygame.init()

# variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_width = 800
display_height = 600

block_size = 10
fps = 30

# initializing font object
font = pygame.font.SysFont(None, 25)

# setting display
gameDisplay = pygame.display.set_mode((display_width, display_height))

# setting caption
pygame.display.set_caption('Slither')

# setting up clock
clock = pygame.time.Clock()


# function to print text on game screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (display_width / 2, display_height / 2))


# game loop
def game_loop():
    # game loop
    game_exit = False
    game_over = False

    # location of lead block
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    rand_apple_x = random.randrange(0, display_width-block_size)
    rand_apple_y = random.randrange(0, display_height-block_size)

    while not game_exit:
        while game_over == True:
            gameDisplay.fill(white)
            message_to_screen('Game over, press C to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        # checking all events
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                game_exit = True
            # for single key tap
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = +block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    lead_x_change = 0
                    lead_y_change = -block_size
                if event.key == pygame.K_DOWN:
                    lead_x_change = 0
                    lead_y_change = +block_size

        # game over logic
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            print('GAME OVER!!!')
            game_over = True

        # rendering logic
        lead_x += lead_x_change
        lead_y += lead_y_change

        # white background
        gameDisplay.fill(white)

        # draw apple
        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, block_size, block_size])

        # draw rectangle
        pygame.draw.rect(gameDisplay, black, [lead_x, lead_y, block_size, block_size])

        # flip updates the specific part of the display
        pygame.display.update()

        # setting frames per second
        clock.tick(fps)

    # quitting pygame
    pygame.quit()

    # quitting python
    quit()


game_loop()
