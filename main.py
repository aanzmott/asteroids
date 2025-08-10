# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField



def main():    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()


    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)


    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    

    # game loop
    # this is the main loop that runs the game
    # draws the player and asteroids
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)

        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

                
        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()


        dt = fpsClock.tick(60)/1000  # limit to 60 FPS


if __name__ == "__main__":
    main()
