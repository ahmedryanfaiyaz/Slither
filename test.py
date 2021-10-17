import pygame

# initialize pygame
pygame.init()

# setting up clock
clock = pygame.time.Clock()

print(pygame.font.get_fonts())

# variables
display_width = 500
display_height = 500

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)

# fonts
small_font = pygame.font.SysFont('arial', 25)
medium_font = pygame.font.SysFont('arial', 50)
large_font = pygame.font.SysFont('arial', 80)

# game display
game_display = pygame.display.set_mode((display_width, display_height))


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
gameExit = False

while not gameExit:
    for event in pygame.event.get():
        print(event)
    message_to_screen('Game over!', red, y_displace=-50, size='large')
    message_to_screen('Press C to play again or Q to quit...', black, 50, size='medium')
    pygame.display.update()

    clock.tick(15)

pygame.quit()
quit()
