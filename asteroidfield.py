import pygame
import random
from asteroid import Asteroid
from constants import *


class AsteroidField(pygame.sprite.Sprite):
    # Manages spawning and behavior of asteroids
    # Inherits from pygame.sprite.Sprite for sprite group management
    
    # edges: List of spawn configurations for each screen edge
    # Each edge config contains:
    #   1. Direction vector - Where asteroids will move
    #   2. Position lambda - Function to calculate spawn position
    edges = [
        # Right edge spawn config
        [
            pygame.Vector2(1, 0),  # Move right to left
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        # Left edge spawn config       
        [
            pygame.Vector2(-1, 0), # Move left to right
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        # Bottom edge spawn config        
        [
            pygame.Vector2(0, 1), # Move bottom to top
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        # Top edge spawn config        
        [
            pygame.Vector2(0, -1), # Move top to bottom
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        # Initialize AsteroidField
        # - Set up sprite container
        # - Initialize spawn timer
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        # Create new asteroid with given parameters
        # Params:
        #   radius: Size of asteroid
        #   position: Vector2 spawn location
        #   velocity: Vector2 movement direction/speed  
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, dt):
        # Update asteroid field state
        # Handles spawning new asteroids on timer
        # Params:
        #   dt: Delta time since last frame
             
        # Update spawn timer
        self.spawn_timer += dt
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # Configure random spawn parameters
            edge = random.choice(self.edges) # Pick random edge
            speed = random.randint(40, 100) # Random speed
            
            # Calculate velocity vector
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            
            # Get spawn position along edge
            position = edge[1](random.uniform(0, 1))# Add random angle
            
            # Determine asteroid size
            kind = random.randint(1, ASTEROID_KINDS)

            # Spawn new asteroid
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
