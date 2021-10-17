"""
Created on 10/15/2021
@author: Ahmed Ryan
"""
from typing import Tuple

import pygame
import random

# initializing pygame
pygame.init()

# variables
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

display_width = 800
display_height = 600

block_size = 20
apple_thickness = 30
fps = 15

# initializing font object
font = pygame.font.SysFont(None, 25)

# setting display
gameDisplay = pygame.display.set_mode((display_width, display_height))

# setting caption
pygame.display.set_caption('Slither')

# setting up clock
clock = pygame.time.Clock()


# define snake
def snake(_block_size, _snake_list):
    # draw snake
    for x_y in _snake_list:
        pygame.draw.rect(gameDisplay, green, [x_y[0], x_y[1], _block_size, _block_size])


def text_objects(text, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


# function to print text on game screen
def message_to_screen(msg, color):
    text_surf, text_rect = text_objects(msg, color)
    # screen_text = font.render(msg, True, color)
    # gameDisplay.blit(screen_text, (display_width / 2, display_height / 2))
    text_rect.center = (display_width / 2), (display_height / 2)
    gameDisplay.blit(text_surf, text_rect)


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

    # snake initialization
    snake_list = []
    snake_length = 1

    # setting apple location
    # rounding apple location to align it with snake
    rand_apple_x = round(random.randrange(0, display_width - block_size))  # / 10.0) * 10.0
    rand_apple_y = round(random.randrange(0, display_height - block_size))  # / 10.0) * 10.0

    while not game_exit:
        while game_over:  # game_over == True
            gameDisplay.fill(white)
            message_to_screen('Game over, press C to play again or Q to quit', red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.QUIT:
                        game_exit = True
                        game_over = False
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
        pygame.draw.rect(gameDisplay, red, [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])

        # snake details
        snake_head = [lead_x, lead_y]
        snake_list.append(snake_head)

        # resizing snake
        if len(snake_list) > snake_length:
            del snake_list[0]

        for each_segment in snake_list[:-1]:
            if each_segment == snake_head:
                game_over = True

        # invoking snake drawing function
        snake(block_size, snake_list)

        # flip updates the specific part of the display
        pygame.display.update()

        # detecting collision
        if rand_apple_x < lead_x < rand_apple_x + apple_thickness or rand_apple_x < lead_x + block_size < rand_apple_x + apple_thickness:
            # print('x crossover')
            if rand_apple_y < lead_y < rand_apple_y + apple_thickness:
                print('x and y crossover')
                # generating new apple
                rand_apple_x = round(random.randrange(0, display_width - block_size))
                rand_apple_y = round(random.randrange(0, display_height - block_size))
                snake_length += 1
            elif rand_apple_y < lead_y + block_size < rand_apple_y + apple_thickness:
                print('x and y crossover')
                # generating new apple
                rand_apple_x = round(random.randrange(0, display_width - block_size))
                rand_apple_y = round(random.randrange(0, display_height - block_size))
                snake_length += 1

        # setting frames per second
        clock.tick(fps)

    # quitting pygame
    pygame.quit()

    # quitting python
    quit()


game_loop()
