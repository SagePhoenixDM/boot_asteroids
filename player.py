import pygame
from circleshape import CircleShape
from constants import PLAYER_TURN_SPEED, PLAYER_RADIUS, PLAYER_SPEED

class Player(CircleShape):
    # constructor
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)  # parent constructor
        self.rotation = 0  # initial rotation angle in degrees
        # in the player class
    

    # provided triangle points
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]


    # overriding draw method
    def draw(self, screen):
        pygame.draw.polygon(
            surface=screen,
            color='white',
            points=self.triangle(),
            width=2
        )


    # rotate method
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    
    # update method (provided by boot.dev)
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # turning left
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # turning right
            self.rotate(dt)
        if keys[pygame.K_w]:
            # moving forward
            self.move(dt)
        if keys[pygame.K_s]:
            # moving backward
            self.move(-dt)


    # adding movement method
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt