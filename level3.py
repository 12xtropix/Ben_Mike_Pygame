import pygame
import config
from MovingPlatform import MovingPlatform

class Level3:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 700, 20),  # Ground
            pygame.Rect(200, 480, 120, 20),  # Mid-level platform
            pygame.Rect(400, 400, 150, 20),  # Higher platform
        ]
        self.moving_platforms = {
            MovingPlatform(500, 300, 100, 20, 2, (250, 400))  # Moves up & down
        }

    def update(self):
        for platform in self.moving_platforms:
            platform.update()

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)  # Green platforms
        for platform in self.moving_platforms:
            platform.draw(screen)
