import pygame
import config
from config import ENEMY_IMAGE
from objects.door import Door
from obstacles.enemies import Enemy


class Level2:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 700, 20),  # Ground
            pygame.Rect(150, 450, 120, 20),  # Small platform
            pygame.Rect(350, 400, 150, 20),  # Higher platform
            pygame.Rect(550, 300, 120, 20),  # Hard-to-reach platform
            pygame.Rect(250, 250, 100, 20),  # Small floating platform
        ]
        self.walls =[

        ]

        self.moving_platforms = {

        }
        self.door = Door(600, 200)
        self.enemies = [Enemy(200, config.FLOOR - 27, 100, 300)]

    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))  # Green platforms
        self.door.draw(screen, camera)
        for enemy in self.enemies:
            enemy.draw(screen, camera)  # Call the draw method on each enemy instance


