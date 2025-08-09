import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.color = (0, 255, 0)  # Green color for the player
        self.speed = 5  # Speed of the player
        self.direction = 0  # Direction in degrees
        self.rotation = 0  # Rotation angle in degrees

    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    # in~ the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        """Rotate the player based on the turn speed."""
        self.rotation += PLAYER_TURN_SPEED * dt
        # self.rotation %= 360

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)

        if keys[pygame.K_d]:
            self.rotate(-dt)
            
    # def move(self):
    #     """Move the player in the current direction."""
    #     self.x += self.speed * math.cos(math.radians(self.direction))
    #     self.y += self.speed * math.sin(math.radians(self.direction))
