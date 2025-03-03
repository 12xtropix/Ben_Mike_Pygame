import pygame

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, camera):
        temprect = camera.apply(self.rect)
        pygame.draw.rect(screen, (169, 70, 9), temprect)  # Brown wall