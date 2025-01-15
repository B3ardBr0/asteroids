#Wilhelm Maritz

import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    font = pygame.font.Font(None, 36)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)
            
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game Over")
                sys.exit()
            
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision(shot):
                    shot.kill()
                    player.add_score(asteroid.radius)  # Add score before splitting       
                    asteroid.split()   

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        score_text = font.render(f"Score: {player.score}", True, "white")
        screen.blit(score_text, (10, 10))    

        pygame.display.flip()

        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()