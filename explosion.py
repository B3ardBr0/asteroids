import pygame
import random
import math
from constants import *

class ExplosionParticle(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = velocity
        self.lifetime = EXPLOSION_PARTICLE_LIFETIME

    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
        self.position += self.velocity * dt

    def draw(self, screen):
        # Fade out as lifetime decreases
        alpha = int((self.lifetime / EXPLOSION_PARTICLE_LIFETIME) * 255)
        pygame.draw.circle(screen, (255, 255, 255, alpha), self.position, EXPLOSION_PARTICLE_SIZE)

def create_explosion(x, y, radius):
    for _ in range(EXPLOSION_PARTICLE_COUNT):
        # Create particles moving in random directions
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(EXPLOSION_PARTICLE_SPEED * 0.5, EXPLOSION_PARTICLE_SPEED)
        velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
        ExplosionParticle(x, y, velocity)