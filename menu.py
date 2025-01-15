import pygame
from constants import *

class Menu:
    def __init__(self):
        self.font_large = pygame.font.Font(None, 74)
        self.font_small = pygame.font.Font(None, 36)
        
    def draw(self, screen):
        # Draw title
        title = self.font_large.render("ASTEROIDS", True, "white")
        title_rect = title.get_rect(centerx=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/3)
        screen.blit(title, title_rect)
        
        # Draw instructions
        start_text = self.font_small.render("Press SPACE to Start", True, "white")
        start_rect = start_text.get_rect(centerx=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
        screen.blit(start_text, start_rect)
        
        controls_text = self.font_small.render("WASD to move, SPACE to shoot", True, "white")
        controls_rect = controls_text.get_rect(centerx=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2 + 50)
        screen.blit(controls_text, controls_rect)
        
    def update(self):
        keys = pygame.key.get_pressed()
        return keys[pygame.K_SPACE]  # Return True if space is pressed