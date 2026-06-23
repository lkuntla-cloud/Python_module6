import math
import random
import pygame

# --- Game Window Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 1")

# --- Colors ---
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# --- Player Setup ---
# A simple 40x40 square
player_size = 40
playerX = (SCREEN_WIDTH // 2) - (player_size // 2)
playerY = SCREEN_HEIGHT - 70
playerX_change = 0
playerY_change = 0
player_speed = 6

# --- Enemies Setup ---
# Lists to hold the 7 enemies
enemyX = []
enemyY = []
enemy_size = 30
num_of_enemies = 7

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, SCREEN_WIDTH - enemy_size))
    # Keep them in the upper half of the screen
    enemyY.append(random.randint(50, SCREEN_HEIGHT - 250))

# --- Score Setup ---
score_value = 0
font = pygame.font.SysFont(None, 36)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

def isCollision(pX, pY, eX, eY):
    # Distance formula to check if the center points get close enough
    distance = math.sqrt((pX - eX)**2 + (pY - eY)**2)
    if distance < 35:  # Collision threshold based on square sizes
        return True
    return False

# --- Main Game Loop ---
clock = pygame.time.Clock()
running = True

while running:
    # 1. Background Fill
    screen.fill(BLACK)

    # 2. Key Input Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
            if event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            if event.key == pygame.K_UP:
                playerY_change = -player_speed
            if event.key == pygame.K_DOWN:
                playerY_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0
            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                playerY_change = 0

    # 3. Update Player Position & Check Screen Boundaries
    playerX += playerX_change
    playerY += playerY_change

    playerX = max(0, min(playerX, SCREEN_WIDTH - player_size))
    playerY = max(0, min(playerY, SCREEN_HEIGHT - player_size))

    # 4. Manage Enemies & Check Collisions
    for i in range(num_of_enemies):
        # Check if the player ran into this specific enemy
        if isCollision(playerX, playerY, enemyX[i], enemyY[i]):
            score_value += 1
            # Teleport enemy to a new random location
            enemyX[i] = random.randint(0, SCREEN_WIDTH - enemy_size)
            enemyY[i] = random.randint(50, SCREEN_HEIGHT - 250)

        # Draw the enemy
        draw_enemy(enemyX[i], enemyY[i])

    # 5. Draw Player and Score
    draw_player(playerX, playerY)
    show_score(10, 10)

    # Update Frame
    pygame.display.update()
    clock.tick(60)

pygame.quit()