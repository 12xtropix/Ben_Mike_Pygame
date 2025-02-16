import pygame
import config
from MovingPlatform import MovingPlatform
from water import Water

class Level4:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 1000, 20),  # Ground
            pygame.Rect(200, 460, 120, 20),  # Mid-level platform
            pygame.Rect(500, 460, 120, 20),  # Higher platform
        ]
        self.moving_platforms = {
            MovingPlatform(550, 300, 100, 20, 2, (250, 400))  # Moves up & down
        }
        self.water = [
            Water(300, config.FLOOR - 20, 275, 20),  # Add a water pit

        ]

    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for water in self.water:
            water.check_collision(player)

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)  # Green platforms

        for platform in self.moving_platforms:
            platform.draw(screen)

        for water in self.water:
            water.draw(screen)
