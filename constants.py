# Screen dimensions
SCREEN_WIDTH = 1280 # Width of game window in pixels
SCREEN_HEIGHT = 720 # Height of game window in pixels

# Asteroid properties
ASTEROID_MIN_RADIUS = 20    # Smallest asteroid size
ASTEROID_KINDS = 3         # Number of asteroid size variations (small/medium/large)
ASTEROID_SPAWN_RATE = 0.8  # Time between asteroid spawns in seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS  # Largest asteroid size
ASTEROID_VERTICES = 8      # Points used to create asteroid polygon shape
ASTEROID_IRREGULARITY = 0.4  # Random variation in asteroid shape (0=circle, 1=very irregular)

# Player ship settings
PLAYER_RADIUS = 20         # Size of player ship collision circle
PLAYER_TURN_SPEED = 300    # Rotation speed in degrees per second
PLAYER_SPEED = 200        # Movement speed in pixels per second
PLAYER_START_LIVES = 3     # Initial number of player lives
PLAYER_RESPAWN_TIME = 2.0  # Invulnerability duration after death in seconds
PLAYER_SPAWN_X = SCREEN_WIDTH / 2   # Initial X spawn position
PLAYER_SPAWN_Y = SCREEN_HEIGHT / 2  # Initial Y spawn position
PLAYER_SHOOT_SPEED = 500   # Bullet velocity in pixels per second
PLAYER_SHOOT_COOLDOWN = 0.3  # Minimum time between shots in seconds
PLAYER_THRUST = 300.0     # Acceleration units per second
PLAYER_MAX_VELOCITY = 400.0  # Maximum velocity
PLAYER_DRAG = 0.99        # Friction coefficient (1.0 = no drag)

# Projectile properties
SHOT_RADIUS = 5           # Size of bullet collision circle
SHOT_COLOR = (255, 0, 0)  # Bullet color in RGB

# Scoring system
SCORE_LARGE_ASTEROID = 20   # Points for destroying large asteroid
SCORE_MEDIUM_ASTEROID = 50  # Points for destroying medium asteroid
SCORE_SMALL_ASTEROID = 100  # Points for destroying small asteroid

# Particle effect settings
EXPLOSION_PARTICLE_COUNT = 15    # Number of particles per explosion
EXPLOSION_PARTICLE_SPEED = 200   # Base velocity of particles
EXPLOSION_PARTICLE_LIFETIME = 0.5 # Duration particles remain visible
EXPLOSION_PARTICLE_SIZE = 2      # Radius of each particle