import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
from pygame import Color

from constants import *

def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    deltaClock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)


    # Init Player object
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroidfield = AsteroidField()

    #Main Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collideaaaaaaaas(player):
                print("Game over!")
                return

        screen.fill("black", rect=None)

        for obj in drawable:
            obj.draw(screen)
        

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = deltaClock.tick(60)/1000


if __name__ == "__main__":
    main()