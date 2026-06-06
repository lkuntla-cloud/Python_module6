import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# Define constants based on instructions
WINDOW_SIZE = (500, 500)
BACKGROUND_COLOR = (58, 58, 58)  # Grey
IMAGE_SIZE = (300, 300)

# 2. Create the game window and set the caption
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My first game screen")

# 3. Load and resize the image
# Replace 'your_image.png' with the actual path to your image file
try:
    original_image = pygame.image.load("your_image.png")
    image = pygame.transform.scale(original_image, IMAGE_SIZE)
except pygame.error:
    # Fallback: Creates a white placeholder box if the image file isn't found
    image = pygame.Surface(IMAGE_SIZE)
    image.fill((255, 255, 255))

# Calculate the center position (X: 100, Y: 100)
image_position = (
    (WINDOW_SIZE[0] - IMAGE_SIZE[0]) // 2,
    (WINDOW_SIZE[1] - IMAGE_SIZE[1]) // 2,
)

# 4. Main Game Loop
running = True
while running:
    # Handle events (like clicking the close 'X' button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with the specified grey color
    screen.fill(BACKGROUND_COLOR)

    # Draw (blit) the image onto the screen at the centered coordinates
    screen.blit(image, image_position)

    # Update the display
    pygame.display.flip()

# Clean up and close the window safely
pygame.quit()
sys.exit()