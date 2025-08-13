import math
import pygame
import random
# from .. import config
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS
)
from .circleshape import CircleShape



class Asteroid(CircleShape):
    def __init__(self, x, y, radius, num_vertices=None):
        super().__init__(x, y, radius)
        # Generate a random polygon for the asteroid
        self.num_vertices = num_vertices or random.randint(8, 16)
        self.angles = [i * (360 / self.num_vertices) for i in range(self.num_vertices)]
        random.shuffle(self.angles)
        self.vertices = []
        for angle in self.angles:
            # rad = angle * 3.14159 / 180
            rad = angle * math.pi / 180  # Use math.pi  
            # Randomize radius for jagged shape
            r = random.uniform(self.radius * 0.7, self.radius)
            # x = self.position.x + r * pygame.math.cos(rad)
            x = self.position.x + r * math.cos(rad)
            y = self.position.y + r * math.sin(rad)
            # y = self.position.y + r * pygame.math.sin(rad)
            self.vertices.append(pygame.Vector2(x, y))




    def draw(self, screen):
        # Draw the polygon
        points = [(v.x, v.y) for v in self.vertices]
        pygame.draw.polygon(screen, "white", points, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Move vertices
        for i in range(len(self.vertices)):
            self.vertices[i] += self.velocity * dt
        # Screen wrap-around
        w, h = SCREEN_WIDTH, SCREEN_HEIGHT
        if self.position.x < 0:
            self.position.x += w
            for v in self.vertices:
                v.x += w
        elif self.position.x > w:
            self.position.x -= w
            for v in self.vertices:
                v.x -= w
        if self.position.y < 0:
            self.position.y += h
            for v in self.vertices:
                v.y += h
        elif self.position.y > h:
            self.position.y -= h
            for v in self.vertices:
                v.y -= h

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        
        split_to = random.uniform( 20, 50)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = self.velocity.rotate(split_to) * 1.2
        asteroid2.velocity = self.velocity.rotate(-split_to) * 1.2