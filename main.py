import pygame
from constants import *

def main ():
    ## initalize pygame ##
    pygame.init
    
    ## create a screen with constants using pygame.display ##
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    ##create an infinate loop for the game screen ##
    black_color = (0,0,0)
    while True:
        screen.fill(black_color)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

    print ("Starting asteroids!")
    print (f"Screen width: {SCREEN_WIDTH}")
    print (f"Screen height: {SCREEN_HEIGHT}")

    if __name__ == "__main__":
        main()

main()