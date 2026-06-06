import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# Define constants based on instructions
WINDOW_SIZE = (640, 480)
BACKGROUND_COLOR = (0, 0, 0)       # Black (as defined by 0,0,0 in the prompt)
RECT_COLOR = (0, 128, 255)         # A nice blue color for the rectangle
TEXT_COLOR = (255, 255, 255)       # White text so it's visible on black

# 2. Create the game window and set the caption
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My first game screen")

# 3. Define the Rectangle and position it at the center
rect_width, rect_height = 200, 100
# pygame.Rect(left, top, width, height)
my_rect = pygame.Rect(0, 0, rect_width, rect_height)
# Center the rectangle using the window's dimensions
my_rect.center = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# 4. Prepare the Text elements
# Set up a font (None uses the default system font, size 36)
font = pygame.font.Font(None, 36)
text_surface = font.render("Hello Pygame!", True, TEXT_COLOR)
# Center the text right above the rectangle
text_rect = text_surface.get_rect()
text_rect.center = (WINDOW_SIZE[0] // 2, (WINDOW_SIZE[1] // 2) - 80)

# Main Game Loop
running = True
while running:
    # Handle events (like clicking the close 'X' button)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background screen
    screen.fill(BACKGROUND_COLOR)

    # Draw the rectangle onto the screen
    pygame.draw.rect(screen, RECT_COLOR, my_rect)

    # Draw (blit) the text onto the screen
    screen.blit(text_surface, text_rect)

    # Update the display
    pygame.display.flip()

# Clean up and close the window safely
pygame.quit()
sys.exit()