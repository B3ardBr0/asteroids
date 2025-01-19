import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown = 0
        self.score = 0
        self.lives = PLAYER_START_LIVES
        self.respawn_timer = 0 # For invulnerability after respawning
    
    def is_vulnerable(self):
        return self.respawn_timer <= 0    

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt    

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        
    def update(self, dt):
        if self.respawn_timer > 0:
            self.respawn_timer -= dt
        
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.rotate(-dt)  
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()   
            
        self.wrap_position()

    def shoot(self):
        if self.shoot_cooldown > 0: 
            return  
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN    
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    
        
    def add_score(self, asteroid_radius):
        if asteroid_radius == ASTEROID_MIN_RADIUS * 3:
            self.score += SCORE_LARGE_ASTEROID
        elif asteroid_radius == ASTEROID_MIN_RADIUS * 2:
            self.score += SCORE_MEDIUM_ASTEROID
        elif asteroid_radius == ASTEROID_MIN_RADIUS:
            self.score += SCORE_SMALL_ASTEROID        
            
    def respawn(self):
        self.position.x = PLAYER_SPAWN_X
        self.position.y = PLAYER_SPAWN_Y
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.respawn_timer = PLAYER_RESPAWN_TIME
    
    def draw(self, screen):
        # Make player flash while invulnerable
        if self.respawn_timer <= 0 or int(self.respawn_timer * 10) % 2:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)