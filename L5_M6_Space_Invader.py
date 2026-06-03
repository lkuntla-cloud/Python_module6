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

playerImg=pygame.transform.scale(pygame.image.load('player.png'),(80,80))
player