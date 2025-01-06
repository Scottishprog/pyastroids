import pygame
from pygame import Color

from constants import *

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    #Main Game Loop
    while(True):
        screen.fill(color=Color(0,0,0), rect=None)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()

if __name__ == "__main__":
    main()