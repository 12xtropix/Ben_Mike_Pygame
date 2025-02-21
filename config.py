import pygame

# Screen settings
SCREEN_SIZE = (800, 600)
ENEMY_SIZE = (30, 30)
FPS = 60
GRAVITY = 0.4
JUMP_STRENGTH = -10
FLOOR = 565
STARTING_X = 50
STARTING_Y = 550

# Load Background Image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("images/redballbackground4.jpg"), SCREEN_SIZE)
FLOOR_IMAGE = pygame.transform.scale(pygame.image.load("images/redballbackground4.jpg"), SCREEN_SIZE)

ENEMY_IMAGE = pygame.transform.scale(pygame.image.load("images/redballenemy.webp"), ENEMY_SIZE)

def load_enemy_image(size=ENEMY_SIZE):
    image = pygame.image.load("images/redballenemy.webp")
    return pygame.transform.scale(image, size)
