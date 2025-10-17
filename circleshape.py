import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    # draw method to be overridden by sub-classes
    def draw(self, screen):
        # sub-classes must override
        pass

    # update method to be overridden by sub-classes
    def update(self, dt):
        # sub-classes must override
        pass

    # collision detection method
    def collision_detect(self, other):
        distance = self.position.distance_to(other.position)
        return distance < (self.radius + other.radius)