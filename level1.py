import pygame
import config

class Level1:
    def __init__(self):
        self.platforms = [
            pygame.Rect(200, 450, 100, 20),
            pygame.Rect(400, 350, 100, 20),
            pygame.Rect(600, 250, 100, 20),
            pygame.Rect(50,config.FLOOR, 1000, 20)
        ]
        self.ground = [pygame.Rect(50, config.FLOOR, 1000, 20)]

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)  # Green platforms
        for platform in self.ground:
            pygame.draw.rect(screen,(255,255,255),platform)


