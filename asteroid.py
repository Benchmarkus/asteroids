from circleshape import CircleShape
from constants import *
import random
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, surface):
        pygame.draw.circle(surface, color="green", center=(self.position), radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        turn_amount = random.uniform(20, 50)
        new_velocity1 = self.velocity.rotate(turn_amount)
        new_velocity2 = self.velocity.rotate(-turn_amount)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid1.velocity = new_velocity1
        new_asteroid2.velocity = new_velocity2
        
        new_asteroid1.velocity *= 1.2
        new_asteroid2.velocity *= 1.2



