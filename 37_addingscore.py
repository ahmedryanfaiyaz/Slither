"""
Created on 10/16/2021
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
small_font = pygame.font.SysFont('comicsansms', 25)
medium_font = pygame.font.SysFont('comicsansms', 50)
large_font = pygame.font.SysFont('comicsansms', 80)

# setting display
game_display = pygame.display.set_mode((display_width, display_height))

# setting caption
pygame.display.set_caption('Slither')

# update icon
icon = pygame.image.load('img/apple.png')
# 32x32 fits ideally
pygame.display.set_icon(icon)

# loading image
img_snake = pygame.image.load('img/small_snake.png')
img_apple = pygame.image.load('img/apple.png')

# setting up clock
clock = pygame.time.Clock()

# setting direction
direction = 'right'


def score(_score):
    text = small_font.render('Score: ' + str(_score), True, black)
    game_display.blit(text, [0,0])


# generate random apple
def random_apple_generation():
    rand_apple_x = round(random.randrange(0, display_width - apple_thickness))
    rand_apple_y = round(random.randrange(0, display_height - apple_thickness))

    return rand_apple_x, rand_apple_y


# game intro
def game_intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        game_display.fill(white)
        message_to_screen('Welcome to Slither', green, -100, 'large')
        message_to_screen('The objective of the game is to eat red apples', black, -30)
        message_to_screen('The more apples you eat, the longer you get', black, 10)
        message_to_screen('If you run into edges or yourself, you will die', black, 50)
        message_to_screen('Press C to play or Q to quit', black, 180)

        pygame.display.update()
        # intro screens require lower fps
        clock.tick(15)


# define snake
def snake(_block_size, _snake_list):
    # rotating snake head
    if direction == 'right':
        head = pygame.transform.rotate(img_snake, 90)
    if direction == 'up':
        head = pygame.transform.rotate(img_snake, 180)
    if direction == 'left':
        head = pygame.transform.rotate(img_snake, 270)
    if direction == 'down':
        head = pygame.transform.rotate(img_snake, 360)

    # adding snake sprite
    game_display.blit(head, (_snake_list[-1][0], _snake_list[-1][1]))
    # draw snake
    for x_y in _snake_list[:-1]:
        pygame.draw.rect(game_display, green, [x_y[0], x_y[1], _block_size, _block_size])


# helper function to show message on screen
def text_objects(text, color, size):
    if size == 'small':
        text_surface = small_font.render(text, True, color)
    elif size == 'medium':
        text_surface = medium_font.render(text, True, color)
    elif size == 'large':
        text_surface = large_font.render(text, True, color)

    return text_surface, text_surface.get_rect()


# function to print text on game screen
def message_to_screen(msg, color, y_displace=0, size='small'):
    text_surf, text_rect = text_objects(msg, color, size)
    text_rect.center = (display_width / 2), (display_height / 2) + y_displace
    game_display.blit(text_surf, text_rect)


# game loop
def game_loop():
    global direction

    direction = 'right'
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
    rand_apple_x, rand_apple_y = random_apple_generation()

    while not game_exit:
        # game_over == True
        while game_over:
            game_display.fill(white)
            message_to_screen('Game over!', red, y_displace=-50, size='large')
            message_to_screen('Press C to play again or Q to quit...', black, 50, size='medium')
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                    game_over = False
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
                    direction = 'left'
                    lead_x_change = -block_size
                    lead_y_change = 0
                if event.key == pygame.K_RIGHT:
                    direction = 'right'
                    lead_x_change = +block_size
                    lead_y_change = 0
                if event.key == pygame.K_UP:
                    direction = 'up'
                    lead_x_change = 0
                    lead_y_change = -block_size
                if event.key == pygame.K_DOWN:
                    direction = 'down'
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
        game_display.fill(white)

        # draw apple
        # pygame.draw.rect(game_display, red, [rand_apple_x, rand_apple_y, apple_thickness, apple_thickness])
        game_display.blit(img_apple, (rand_apple_x, rand_apple_y))

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

        # display score
        score(snake_length-1)

        # flip updates the specific part of the display
        pygame.display.update()

        # detecting collision
        if rand_apple_x < lead_x < rand_apple_x + apple_thickness or rand_apple_x < lead_x + block_size < rand_apple_x + apple_thickness:
            # print('x crossover')
            if rand_apple_y < lead_y < rand_apple_y + apple_thickness:
                print('x and y crossover')
                # generating new apple
                rand_apple_x, rand_apple_y = random_apple_generation()
                snake_length += 1
            elif rand_apple_y < lead_y + block_size < rand_apple_y + apple_thickness:
                print('x and y crossover')
                # generating new apple
                rand_apple_x, rand_apple_y = random_apple_generation()
                snake_length += 1

        # setting frames per second
        clock.tick(fps)

    # quitting pygame
    pygame.quit()

    # quitting python
    quit()


game_intro()
game_loop()
