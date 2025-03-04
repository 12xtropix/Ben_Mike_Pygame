import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.spike import Spike
from objects.door import Door

class Level3:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 700, 20),  # Ground
            pygame.Rect(200, 460, 120, 20),  # Mid-level platform
            pygame.Rect(400, 400, 150, 20),  # Higher platform
        ]

        self.walls =[

        ]
        self.moving_platforms = {
            MovingPlatform(500, 300, 100, 20, 2, (250, 400))  # Moves up & down
        }
        self.spikes = [
            Spike(300, config.FLOOR - 20, 40, 20),  # Add spikes on the floor
            Spike(600, config.FLOOR - 20, 40, 20)
        ]
        self.door = Door(600, 200)

    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for spike in self.spikes:
            spike.check_collision(player)

    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))  # Green platforms

        for platform in self.moving_platforms:
            platform.draw(screen, camera)

        for spike in self.spikes:
            spike.draw(screen, camera)
        self.door.draw(screen, camera)
