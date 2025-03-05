import pygame

"""
This is our config file, which we made to contain our constants that define our game operation. This is really useful, as you will see in all of our other classes
"""

# Screen settings
SCREEN_SIZE = (800, 600)
ENEMY_SIZE = (30, 30)
BOSS_SIZE = (200, 200)
MC_SIZE = (30,30)
FPS = 60
GRAVITY = 0.4
JUMP_STRENGTH = -10
FLOOR = 565
STARTING_X = 2700 #50
STARTING_Y = 600 #550

# Load Background Image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("images/redballbackground4.jpg"), SCREEN_SIZE)
FLOOR_IMAGE = pygame.transform.scale(pygame.image.load("images/redballbackground4.jpg"), SCREEN_SIZE)

ENEMY_IMAGE = pygame.transform.scale(pygame.image.load("images/redballenemy.webp"), ENEMY_SIZE)
BOSS_IMAGE =  pygame.transform.scale(pygame.image.load("images/moonboss.png"), ENEMY_SIZE)
MC_IMAGE = pygame.transform.scale(pygame.image.load("images/redballmc(1).png"), MC_SIZE)

def load_enemy_image(size=ENEMY_SIZE):
    image = pygame.image.load("images/redballenemy.webp")
    return pygame.transform.scale(image, size)

def load_boss_image(size=BOSS_SIZE):
    image = pygame.image.load("images/moonboss.png")
    return pygame.transform.scale(image, size)

