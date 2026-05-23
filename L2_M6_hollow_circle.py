import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Circle Example")

GREEN = (0, 255, 0)
running = True

while running:
    # Fill background every frame
    window.fill((255, 255, 255))

    # Draw circles
    pygame.draw.circle(window, GREEN, (300, 300), 50)
    pygame.draw.circle(window, GREEN, (100, 100), 50, 3)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update display
    pygame.display.update()
pygame.quit()