"""
Created on 10/15/2021
@author: Ahmed Ryan
"""

import pygame

# initializing pygame
pygame.init()

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# setting display
gameDisplay = pygame.display.set_mode((800, 600))

# setting caption
pygame.display.set_caption('Slither')

# game loop
gameExit = False

# location of lead block
lead_x = 400
lead_y = 300

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
                lead_x_change = -10
                lead_y_change = 0
            if event.key == pygame.K_RIGHT:
                lead_x_change = +10
                lead_y_change = 0
            if event.key == pygame.K_UP:
                lead_x_change = 0
                lead_y_change = -10
            if event.key == pygame.K_DOWN:
                lead_x_change = 0
                lead_y_change = +10

    # game over logic
    if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0:
        print('GAME OVER!!!')
        gameExit = True

    # rendering logic
    lead_x += lead_x_change
    lead_y += lead_y_change

    # white background
    gameDisplay.fill(white)

    # draw rectangle
    pygame.draw.rect(gameDisplay, black, rect=(lead_x, lead_y, 10, 10))

    # flip updates the specific part of the display
    pygame.display.update()

    # setting frames per second
    clock.tick(15)

# quitting pygame
pygame.quit()

# quitting python
quit()
