"""
Created on 10/15/2021
@author: Ahmed Ryan
"""

import pygame
import time

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


# function to print text on game screen
def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, (display_width / 2, display_height / 2))


# setting display
gameDisplay = pygame.display.set_mode((display_width, display_height))

# setting caption
pygame.display.set_caption('Slither')

# game loop
gameExit = False

# location of lead block
lead_x = display_width / 2
lead_y = display_height / 2

lead_x_change = 0
lead_y_change = 0

# setting up clock
clock = pygame.time.Clock()

while not gameExit:
    # checking all events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
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
        gameExit = True

    # rendering logic
    lead_x += lead_x_change
    lead_y += lead_y_change

    # white background
    gameDisplay.fill(white)

    # draw rectangle
    pygame.draw.rect(gameDisplay, black, rect=(lead_x, lead_y, block_size, block_size))

    # flip updates the specific part of the display
    pygame.display.update()

    # setting frames per second
    clock.tick(fps)

# showing game over message
message_to_screen('You Lose! Get outside you fool!!!', red)
pygame.display.update()
time.sleep(2)

# quitting pygame
pygame.quit()

# quitting python
quit()
