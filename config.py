import pygame

SCREEN_SIZE = (800, 600)
FPS = 60
GRAVITY = 0.4
JUMP_STRENGTH = -10
FLOOR = 500

# Load Background Image
BACKGROUND_IMAGE = pygame.transform.scale(pygame.image.load("redballbackground.jpg"), SCREEN_SIZE)

