from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import pygame
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    AsteroidField()
        
    Player.cooldown = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(color=(0,0,0))

        updatable.update(dt)

        for o in drawable:
            o.draw(screen)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.kill()
                    shot.kill()
        
        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("Game over!")
        


        dt = clock.tick(60) / 1000
        pygame.display.flip()





if __name__ == "__main__":
    main()