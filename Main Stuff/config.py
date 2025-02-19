import pygame

SCREEN_SIZE = (800, 600)
FPS = 60
GRAVITY = 0.4
JUMP_STRENGTH = -10
FLOOR = 565
STARTING_X = 50
STARTING_Y = 550


# Load Background Image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("../images/redballbackground4.jpg"), SCREEN_SIZE)
FLOOR_IMAGE = pygame.transform.scale(pygame.image.load("../images/redballbackground4.jpg"), SCREEN_SIZE)

