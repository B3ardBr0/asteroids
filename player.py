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
        self.respawn_timer = 0  # For invulnerability after respawning
        # New physics properties
        self.thrust_vector = pygame.Vector2(0, 0)
        self.is_thrusting = False
    
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

    def apply_thrust(self, dt):
        # Calculate thrust direction based on rotation
        thrust_direction = pygame.Vector2(0, 1).rotate(self.rotation)
        # Apply thrust acceleration
        self.thrust_vector += thrust_direction * PLAYER_THRUST * dt
        # Limit maximum velocity
        if self.thrust_vector.length() > PLAYER_MAX_VELOCITY:
            self.thrust_vector.scale_to_length(PLAYER_MAX_VELOCITY)
        self.is_thrusting = True

    def apply_reverse_thrust(self, dt):
        # Calculate thrust direction based on rotation
        thrust_direction = pygame.Vector2(0, -1).rotate(self.rotation)
        # Apply reverse thrust (at half strength)
        self.thrust_vector += thrust_direction * (PLAYER_THRUST * 0.5) * dt
        # Limit maximum velocity
        if self.thrust_vector.length() > PLAYER_MAX_VELOCITY:
            self.thrust_vector.scale_to_length(PLAYER_MAX_VELOCITY)
        self.is_thrusting = True
        
    def update(self, dt):
        if self.respawn_timer > 0:
            self.respawn_timer -= dt
        
        self.shoot_cooldown -= dt
        keys = pygame.key.get_pressed()
        
        # Reset thrust flag
        self.is_thrusting = False
        
        # Handle rotation
        if keys[pygame.K_a]:
            self.rotate(-dt)  
        if keys[pygame.K_d]:
            self.rotate(dt)
            
        # Handle thrust
        if keys[pygame.K_w]:
            self.apply_thrust(dt)
        if keys[pygame.K_s]:
            self.apply_reverse_thrust(dt)
            
        # Apply drag/friction
        self.thrust_vector *= PLAYER_DRAG
            
        # Update position based on thrust vector
        self.position += self.thrust_vector * dt
            
        if keys[pygame.K_SPACE]:
            self.shoot()   
            
        self.wrap_position()

    def shoot(self):
        if self.shoot_cooldown > 0: 
            return  
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN    
        shot = Shot(self.position.x, self.position.y)
        # Add player's velocity to shot velocity for realistic momentum
        base_velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = base_velocity + self.thrust_vector
    
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
        self.thrust_vector = pygame.Vector2(0, 0)
        self.rotation = 0
        self.respawn_timer = PLAYER_RESPAWN_TIME
    
    def draw(self, screen):
        # Draw thrust particles when thrusting
        if self.is_thrusting:
            self.draw_thrust(screen)
            
        # Make player flash while invulnerable
        if self.respawn_timer <= 0 or int(self.respawn_timer * 10) % 2:
            pygame.draw.polygon(screen, "white", self.triangle(), 2)
            
    def draw_thrust(self, screen):
        # Calculate thrust exhaust points
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2
        
        # Base of the thrust (back of ship)
        thrust_base = self.position - forward * self.radius
        
        # Draw two small triangles for thrust
        left_thrust = [
            thrust_base - right / 2,
            thrust_base - right - forward * self.radius / 2,
            thrust_base - forward * self.radius
        ]
        right_thrust = [
            thrust_base + right / 2,
            thrust_base + right - forward * self.radius / 2,
            thrust_base - forward * self.radius
        ]
        
        pygame.draw.polygon(screen, (255, 165, 0), left_thrust)  # Orange color
        pygame.draw.polygon(screen, (255, 165, 0), right_thrust)