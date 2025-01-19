import pygame
import random
import math
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius) # Initialize base class
        self.vertices = self._generate_vertices() # Create polygon points
    
    def _generate_vertices(self):
        # Creates irregular polygon shape by:
        # 1. Dividing circle into equal segments
        # 2. Adding random variation to radius
        # 3. Converting polar to cartesian coordinates
        vertices = []
        for i in range(ASTEROID_VERTICES):
            angle = (i / ASTEROID_VERTICES) * 2 * math.pi
            # Vary the radius randomly
            random_radius = self.radius * (1 - random.uniform(0, ASTEROID_IRREGULARITY))
            x = math.cos(angle) * random_radius
            y = math.sin(angle) * random_radius
            vertices.append((x, y))
        return vertices
    
    def draw(self, screen):
        # Convert local vertices to screen coordinates
        screen_vertices = []
        for x, y in self.vertices:
            screen_x = self.position.x + x
            screen_y = self.position.y + y
            screen_vertices.append((screen_x, screen_y))
        
        pygame.draw.polygon(screen, "white", screen_vertices, 2)
        
    def update(self, dt):
        self.position += self.velocity * dt    
        
        
    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # randomize the angle of the split
        random_angle = random.uniform(20, 50)

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2