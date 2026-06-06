import random
import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# Window Setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Add Custom Event Assignment")

# 2. Define a Custom Event
# Pygame reserves IDs below pygame.USEREVENT for internal engine events.
# We define our event by adding an offset to USEREVENT.
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Trigger the custom event every 2000 milliseconds (2 seconds)
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)


# 3. Create the Sprite Class
class ColorChangingSprite(pygame.sprite.Sprite):

    def __init__(self, width, height, x, y):
        super().__init__()
        self.image = pygame.Surface([width, height])

        # Give it an initial random color
        self.change_color()

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_color(self):
        """Generates a random RGB color and fills the sprite's surface."""
        random_color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
        self.image.fill(random_color)


# 4. Instantiate two sprites and add them to a group
sprite1 = ColorChangingSprite(100, 100, 300, 300)
sprite2 = ColorChangingSprite(100, 100, 500, 300)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1)
all_sprites.add(sprite2)

# Clock to control frame rate
clock = pygame.time.Clock()

# 5. Main Game Loop
running = True
while running:
    clock.tick(60)

    # Event Polling Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Check if our custom event has been triggered by the timer
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()

    # 6. Render Screen Canvas
    screen.fill((30, 30, 35))  # Dark background
    all_sprites.draw(screen)  # Draw both sprites inside the container
    pygame.display.flip()  # Update window display

# Clean exit
pygame.quit()
sys.exit()