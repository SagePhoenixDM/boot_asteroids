# importing packages
import pygame
from constants import *


# defining main function
def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # creating GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # creating game loop
    while True:
        # exiting game loop if screen closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # creating black screen
        screen.fill(color=(0, 0, 0))
        # refreshing screen
        pygame.display.flip()


# only allowing main to run if executed from CLI
if __name__ == '__main__':
    main()
