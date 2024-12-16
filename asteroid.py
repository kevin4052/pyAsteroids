import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(new_angle)
        v2 = self.velocity.rotate(new_angle * -1)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position[0], self.position[1], new_radius)
        a2 = Asteroid(self.position[0], self.position[1], new_radius)
        a1.velocity = v1 * 1.2
        a2.velocity = v2 * 1.2
