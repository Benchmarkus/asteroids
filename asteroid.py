from circleshape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, color="green", center=(self.position), radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt