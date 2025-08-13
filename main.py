# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from config import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT
)
from entities import Player, Asteroid, Shot, AsteroidField



def main():    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()
    dt = 0

    #sprite groups for managing game objects    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    

    # game loop
    # this is the main loop that runs the game
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # update the game state per frame
        updatable.update(dt)

        #background
        screen.fill("black")

        # check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill() 
                    asteroid.split()

        # spawn new asteroids
        for obj in drawable:
            obj.draw(screen)
        
        #screen refresh
        pygame.display.flip()

        dt = fpsClock.tick(60)/1000  # limit to 60 FPS


if __name__ == "__main__":
    main()
