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
        # Fade out as lifetime decreases.
        # pygame.draw discards the alpha channel unless the target surface has
        # per-pixel alpha, and the display surface does not. Draw onto a small
        # SRCALPHA surface instead and blit that, so the blend actually happens.
        alpha = max(0, min(255, int((self.lifetime / EXPLOSION_PARTICLE_LIFETIME) * 255)))
        size = EXPLOSION_PARTICLE_SIZE * 2
        particle = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(
            particle,
            (255, 255, 255, alpha),
            (EXPLOSION_PARTICLE_SIZE, EXPLOSION_PARTICLE_SIZE),
            EXPLOSION_PARTICLE_SIZE,
        )
        screen.blit(
            particle,
            (self.position.x - EXPLOSION_PARTICLE_SIZE,
             self.position.y - EXPLOSION_PARTICLE_SIZE),
        )

def create_explosion(x, y, radius):
    for _ in range(EXPLOSION_PARTICLE_COUNT):
        # Create particles moving in random directions
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(EXPLOSION_PARTICLE_SPEED * 0.5, EXPLOSION_PARTICLE_SPEED)
        velocity = pygame.Vector2(math.cos(angle), math.sin(angle)) * speed
        ExplosionParticle(x, y, velocity)