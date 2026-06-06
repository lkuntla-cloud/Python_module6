import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# Window Configuration
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Sprites Assignment")

# Colors (RGB)
BG_COLOR = (30, 30, 40)       # Dark slate blue background
PLAYER_COLOR = (46, 204, 113)  # Green for the controllable sprite
STATIC_COLOR = (231, 76, 60)  # Red for the second static sprite

# Clock to control the game's frame rate
clock = pygame.time.Clock()


# 2. Define the Custom Sprite Class
class CustomSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, start_x, start_y):
        super().__init__()
        # Create a rectangular surface for the sprite
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        
        # Get the rectangle object that defines position and dimensions
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        
        # Movement speed factor
        self.speed = 5

    def move(self, dx, dy):
        """Updates position and keeps the sprite within screen boundaries."""
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
        # Screen boundaries check
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


# 3. Instantiate Sprites and Groups
# Create Sprite 1 (Player - Green)
player_sprite = CustomSprite(PLAYER_COLOR, 50, 50, 200, 300)

# Create Sprite 2 (Static Target - Red)
static_sprite = CustomSprite(STATIC_COLOR, 60, 60, 550, 300)

# Add both sprites to a unified Pygame Render Group
all_sprites = pygame.sprite.Group()
all_sprites.add(player_sprite)
all_sprites.add(static_sprite)


# 4. Main Game Loop
running = True
while running:
    # Frame rate management (60 Frames Per Second)
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 5. Continuous Keyboard Input Checking (Controls)
    keys = pygame.key.get_pressed()
    
    dx = 0
    dy = 0
    
    if keys[pygame.K_LEFT]:
        dx = -1
    if keys[pygame.K_RIGHT]:
        dx = 1
    if keys[pygame.K_UP]:
        dy = -1
    if keys[pygame.K_DOWN]:
        dy = 1

    # Apply movement vectors to the controlled sprite
    player_sprite.move(dx, dy)

    # 6. Render/Draw everything
    screen.fill(BG_COLOR)          # Clear screen with background color
    all_sprites.draw(screen)       # Draw all sprites inside the group to the screen
    pygame.display.flip()          # Refresh display buffer

# Exit framework cleanly
pygame.quit()
sys.exit()