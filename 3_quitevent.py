"""
Created on 10/14/2021
@author: Ahmed Ryan
"""

import pygame

# initializing pygame
pygame.init()

# setting display
gameDisplay = pygame.display.set_mode((800, 600))

# setting caption
pygame.display.set_caption('Slither')

# flip updates the specific part of the display
pygame.display.update()

# game loop
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        # checking event type
        if event.type == pygame.QUIT:
            gameExit = True
        print(event)

# quitting pygame
pygame.quit()

# quitting python
quit()
