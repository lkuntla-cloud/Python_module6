import math
import random
import pygame

SCREEN_WIDTH=1300
SCREEN_HEIGHT=900
PLAYER_START_X=400
PLAYER_START_Y=380
ENEMY_START_Y_MIN=10
ENEMY_START_Y_MAX=80
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=10
BULLET_SPEED_Y=30
COLLISION_DISTANCE=25

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

background=pygame.transform.scale(pygame.image.load('Bg.jpg'),SCREEN_WIDTH,SCREEN_HEIGHT)

pygame.display.set_caption("Space Invader")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player (scaled)
playerImg = pygame.transform.scale(
    pygame.image.load('player.png'), (80, 80)
)
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

# Enemy (scaled)
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(
        pygame.transform.scale(
            pygame.image.load('enemy.jpg'), (64, 64)
        )
    )
    enemyX.append(random.randint(0, SCREEN_WIDTH - 64))
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

# Bullet (scaled)
bulletImg = pygame.transform.scale(
    pygame.image.load('bullet.png'), (70, 70)
)
bulletX = 0
bulletY = PLAYER_START_Y
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255:, 255))
    screen.blit(over_text, (400, 300))

def player(x, y):
    screen.blit(playerImg, (x, y))
def enemy(x,y,i):
    screen.blit(enemyImg[i],(x,y))
def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x,y))
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance=math.sqrt((enemyX-bulletX)**2+(enemyY-bulletY)**2)
running=True
while running:
  screen.fill((0,0,0))
  screen.blit(background,(0,0))
  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT:
        playerX_change=-5
      if event.key==pygame.K_RIGHT:
        playerX_change=5
      if event.key==pygame.K_SPACE and bullet_state=="ready":
        bulletX=playerX+20
        bulletY=playerY
        fire_bullet(bulletX,bulletY)
    if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
      playerX_change=0
  playerX+=playerX_change
  playerX=max(0,min(playerX,SCREEN_WIDTH-80))
  for i in range(num_of_enemies):