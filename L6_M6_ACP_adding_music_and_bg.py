import math
import random
import pygame

# --- Game Window Setup ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame and the Sound Mixer
pygame.init()
pygame.mixer.init() # Crucial line to turn on audio processing

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader Project - Part 2")

# --- Load External Assets ---
# 1. Background Image
# This loads your 'Bg.jpg' file and scales it to fill the entire window dimensions
background = pygame.transform.scale(pygame.image.load('Bg.jpg'), (SCREEN_WIDTH, SCREEN_HEIGHT))

# 2. Background Music
# This streams the external audio file without eating up all your computer memory
pygame.mixer.music.load('music.mp3') 
pygame.mixer.music.play(-1) # The argument -1 tells Pygame to loop the track infinitely

# --- Colors ---
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# --- Player Setup ---
player_size = 40
playerX = (SCREEN_WIDTH // 2) - (player_size // 2)
playerY = SCREEN_HEIGHT - 80  
playerX_change = 0
playerY_change = 0
player_speed = 7

# --- Enemy Setup ---
enemy_size = 30
num_of_enemies = 7
enemyX = []
enemyY = []

for i in range(num_of_enemies):
    enemyX.append(random.randint(0, SCREEN_WIDTH - enemy_size))
    enemyY.append(random.randint(50, SCREEN_HEIGHT // 2))

# --- Score Setup ---
score_value = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, WHITE)
    screen.blit(score, (x, y))

def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, (x, y, player_size, player_size))

def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, (x, y, enemy_size, enemy_size))

def isCollision(pX, pY, eX, eY):
    distance = math.sqrt((pX - eX)**2 + (pY - eY)**2)
    return distance < 35

# --- Main Game Loop ---
clock = pygame.time.Clock()
running = True

while running:
    # Instead of screen.fill(BLACK), we draw your background image directly at position (0, 0)
    screen.blit(background, (0, 0))

    # 1. Keyboard Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -player_speed
            elif event.key == pygame.K_RIGHT:
                playerX_change = player_speed
            elif event.key == pygame.K_UP:
                playerY_change = -player_speed
            elif event.key == pygame.K_DOWN:
                playerY_change = player_speed

        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                playerX_change = 0
            elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                playerY_change = 0

    # 2. Update Positions
    playerX += playerX_change
    playerY += playerY_change

    playerX = max(0, min(playerX, SCREEN_WIDTH - player_size))
    playerY = max(0, min(playerY, SCREEN_HEIGHT - player_size))

    # 3. Handle Enemies & Collision
    for i in range(num_of_enemies):
        if isCollision(playerX, playerY, enemyX[i], enemyY[i]):
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - enemy_size)
            enemyY[i] = random.randint(50, SCREEN_HEIGHT // 2)

        draw_enemy(enemyX[i], enemyY[i])

    # 4. Render Updates
    draw_player(playerX, playerY)
    show_score(10, 10)

    pygame.display.update()
    clock.tick(60) 

pygame.quit()