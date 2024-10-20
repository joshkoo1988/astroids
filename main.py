import pygame
from constants import *
from player import *

def main ():
    ## initalize pygame ##
    ## create a screen with constants using pygame.display ##
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ## set FPS refresh rate & create player obj ##
    clock = pygame.time.Clock()

    ## group to handle obj that can be updated ##
    ## group to handle obj that can be drawn ##
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

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
        for obj in updateable:
            obj.update(dt)

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        ## update the display ##
        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()