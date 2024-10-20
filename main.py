import pygame
from constants import *
import sys
from player import Player
from astroidfield import AsteroidField
from asteroid import Asteroid
from shot import Shot

def main ():
    ## initalize pygame ##
    ## create a screen with constants using pygame.display ##
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ## set FPS refresh rate & create player obj ##
    clock = pygame.time.Clock()

    ## group to handle obj that can be updated ##
    ## group to handle obj that can be drawn ##
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    

    Player.containers = (updatable, drawable)


    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    dt = 0

    ##create an infinate game loop for the game screen ##
    running = True
    while running:
    ## close game if game window is closed ##
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        ## prints player ##
        ## update players rotation ##
        for obj in updatable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        ## update the display ##
        pygame.display.flip()

        for obj in asteroids:
            if player.collissions(obj):
                print ("Game over!")
                running = False

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()