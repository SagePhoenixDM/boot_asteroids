# importing packages
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


# defining main function
def main():
    pygame.init()
    print('Starting Asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')

    # initialization
    # creating game clock
    clock = pygame.time.Clock()
    dt = 0  # delta time b/w frames
    # creating GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # creating groups of game objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    # adding classes to groups
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    # creating player object
    player = Player(x=(SCREEN_WIDTH / 2), y=(SCREEN_HEIGHT / 2))
    field = AsteroidField()

    # creating game loop
    while True:
        # exiting game loop if screen closed
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # creating black screen
        screen.fill(color=(0, 0, 0))
        # looping through drawable objects
        # player.draw(screen)  # old method, superceded by group
        for objects in drawable:
            objects.draw(screen)

        # updating player
        # player.update(dt)  # old method, superceded by group
        updatable.update(dt)  # uses updatable group
        
        # refreshing screen
        pygame.display.flip()
        # calling tick to maintain fps
        dt = clock.tick(60) / 1000  # converted from ms to sec


# only allowing main to run if executed from CLI
if __name__ == '__main__':
    main()
