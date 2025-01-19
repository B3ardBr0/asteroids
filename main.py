import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from explosion import ExplosionParticle
from menu import Menu
from game_over import GameOverScreen

def game_loop(screen):
    clock = pygame.time.Clock()
    game_over_screen = GameOverScreen()
    font = pygame.font.Font(None, 36)

    def init_game():
        updatable = pygame.sprite.Group()
        drawable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        shots = pygame.sprite.Group()
        
        ExplosionParticle.containers = (updatable, drawable)
        Asteroid.containers = (asteroids, updatable, drawable)
        Shot.containers = (shots, updatable, drawable)
        AsteroidField.containers = updatable
        asteroid_field = AsteroidField()

        Player.containers = (updatable, drawable)
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        
        return updatable, drawable, asteroids, shots, asteroid_field, player

    updatable, drawable, asteroids, shots, asteroid_field, player = init_game()
    dt = 0
    game_state = "playing"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

        if game_state == "playing":
            for obj in updatable:
                obj.update(dt)
                
            for asteroid in asteroids:
                if asteroid.collision(player) and player.is_vulnerable():
                    player.lives -= 1
                    if player.lives <= 0:
                        game_state = "game_over"
                    else:
                        player.respawn()
                
            for asteroid in asteroids:
                for shot in shots:
                    if asteroid.collision(shot):
                        shot.kill()
                        from explosion import create_explosion
                        create_explosion(asteroid.position.x, asteroid.position.y, asteroid.radius)
                        player.add_score(asteroid.radius)  # Add score before splitting       
                        asteroid.split()   

            screen.fill("black")

            for obj in drawable:
                obj.draw(screen)

            score_text = font.render(f"Score: {player.score}", True, "white")
            lives_text = font.render(f"Lives: {player.lives}", True, "white")
            screen.blit(score_text, (10, 10))
            screen.blit(lives_text, (10, 50))
            
            pygame.display.flip()

        elif game_state == "game_over":
            game_over_screen.draw(screen, player.score)
            action = game_over_screen.update()
            
            if action == "restart":
                # Reset the game
                updatable, drawable, asteroids, shots, asteroid_field, player = init_game()
                game_state = "playing"
            elif action == "quit":
                return False

        dt = clock.tick(60) / 1000

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    menu = Menu()
    
    while True:
        screen.fill("black")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        # Show menu and wait for input
        menu.draw(screen)
        pygame.display.flip()
        
        if menu.update():  # If space is pressed
            # Start the game
            if not game_loop(screen):  # If player quit
                return

if __name__ == "__main__":
    main()