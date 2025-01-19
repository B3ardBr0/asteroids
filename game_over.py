import pygame
from constants import *



class GameOverScreen:
    def __init__(self):
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        
    def draw(self, screen, score):
        screen.fill("black")
        
        # Draw Game Over text
        game_over_text = self.font_large.render("GAME OVER", True, "white")
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
        screen.blit(game_over_text, game_over_rect)
        
        # Draw final score
        score_text = self.font_small.render(f"Final Score: {score}", True, "white")
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(score_text, score_rect)
        
        # Draw restart instruction
        restart_text = self.font_small.render("Press R to Restart", True, "white")
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50))
        screen.blit(restart_text, restart_rect)
        
        # Draw quit instruction
        quit_text = self.font_small.render("Press Q to Quit", True, "white")
        quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 100))
        screen.blit(quit_text, quit_rect)
        
        pygame.display.flip()
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            return "restart"
        elif keys[pygame.K_q]:
            return "quit"
        return None