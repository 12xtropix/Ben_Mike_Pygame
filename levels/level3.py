import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.spike import Spike
from objects.door import Door
from obstacles.water import Water
from obstacles.enemies import Enemy


class Level3:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 850, 20),  # Ground
            pygame.Rect(1070, 300, 500, 20),  # Mid-level platform
            pygame.Rect(1120, 400, 500, 20), # Higher platform
            pygame.Rect(1070, 500, 500, 20),  # Higher platform
            pygame.Rect(1120, 600, 500, 20),  # Higher platform
            pygame.Rect(1070, 700, 1520, 20),
            pygame.Rect(1670, 300, 500, 20),  # Mid-level platform
            pygame.Rect(1640, 400, 500, 20),  # Higher platform
            pygame.Rect(1670, 500, 500, 20),  # Higher platform
            pygame.Rect(1640, 600, 500, 20),  # Higher platform

            pygame.Rect(2520, 600, 50, 20),
            pygame.Rect(2520, 500, 50, 20),
            pygame.Rect(2520, 400, 50, 20),
            pygame.Rect(2520, 300, 50, 20),

            pygame.Rect(2580, 600, 50, 20),
            pygame.Rect(2580, 500, 50, 20),
            pygame.Rect(2580, 400, 50, 20),
            pygame.Rect(2580, 300, 50, 20),



        ]
        self.water = [
            Water(200, config.FLOOR - 20, 700, 20),  # Add a water pit
        ]
        self.walls =[
            pygame.Rect(1070, 300, 20, 400),
            pygame.Rect(1620,0, 20, 620),
            pygame.Rect(2170, 300, 20, 400),
            pygame.Rect(2570, 300, 20, 400),
        ]
        self.moving_platforms = {
            MovingPlatform(200, 300, 100, 20, 2, (300, 500)),
            MovingPlatform(450, 300, 100, 20, 2, (300, 500)),
            MovingPlatform(700, 300, 100, 20, 2, (300, 500)),
            MovingPlatform(950, 300, 100, 20, 2, (300, 500))
        }
        self.enemies = [
            Enemy(1120, 380, 1150, 1550),
            Enemy(1070, 480, 1070, 1470),
            Enemy(1120, 580, 1150, 1550),
            Enemy(1640, 380, 1640, 2040),
            Enemy(1670, 480, 1670, 2070),
            Enemy(1640, 580, 1640, 2040),
        ]
        self.spikes = [
            # Spike(200, 580, 40, 20),
            ]
        self.door = Door(2400, 750)

    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for spike in self.spikes:
            spike.check_collision(player)

        for water in self.water:
            water.check_collision(player)


    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))  # Green platforms

        for enemy in self.enemies:
            enemy.draw(screen, camera)  # Call the draw method on each enemy instance

        for platform in self.moving_platforms:
            platform.draw(screen, camera)

        for spike in self.spikes:
            spike.draw(screen, camera)
        self.door.draw(screen, camera)

        for water in self.water:
            water.draw(screen, camera)
        self.door.draw(screen, camera)

        for wall in self.walls:
            pygame.draw.rect(screen, (255, 0, 0), camera.apply(wall))  # Red walls for visibility
