import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.water import Water
from objects.door import Door
from obstacles.spike import Spike


class Level4:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 4000, 20),  # Extended Ground
            pygame.Rect(150, 460, 30, 20),  # Mid-level platforms
            pygame.Rect(300, 380, 30, 20),
            pygame.Rect(450, 300, 30, 20),
            pygame.Rect(600, 220, 30, 20),
            pygame.Rect(750, 140, 30, 20),
            pygame.Rect(1200, 460, 30, 20),
            pygame.Rect(1400, 380, 30, 20),
            pygame.Rect(1600, 300, 30, 20),
            pygame.Rect(1800, 220, 30, 20),
            pygame.Rect(2000, 140, 30, 20),
        ]

        self.moving_platforms = {

        }

        self.water = [
            Water(200, config.FLOOR - 20, 875, 20),
            Water(1300, config.FLOOR - 20, 875, 20)
        ]

        self.door = Door(2250, 100)  # Moved further to extend the level

        self.walls = [
            pygame.Rect(4000, 0, 20, 600),
            pygame.Rect(1000, 200, 20, 100)
        ]

        self.spikes = [
            Spike(995,180,30,20)
        ]

    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for water in self.water:
            water.check_collision(player)

        for spike in self.spikes:
            spike.check_collision(player)

    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))

        for platform in self.moving_platforms:
            platform.draw(screen, camera)

        for water in self.water:
            water.draw(screen, camera)

        self.door.draw(screen, camera)

        for wall in self.walls:
            pygame.draw.rect(screen, (255, 0, 0), camera.apply(wall))

        for spike in self.spikes:
            spike.draw(screen,camera)