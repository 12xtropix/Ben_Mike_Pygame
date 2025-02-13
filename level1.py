import pygame
import config

class Level1:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, 550, 700, 20),
            pygame.Rect(200, 450, 100, 20),
            pygame.Rect(400, 350, 100, 20),
            pygame.Rect(600, 250, 100, 20),
        ]

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)  # Green platforms
