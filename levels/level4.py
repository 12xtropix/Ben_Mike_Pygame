import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.water import Water
from objects.door import Door


class Level4:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 1500, 20),  # Ground
            # pygame.Rect(200, 460, 120, 20),  # Mid-level platform
            # pygame.Rect(500, 460, 120, 20),  # Higher platform
        ]
        self.moving_platforms = {
            MovingPlatform(550, 300, 100, 20, 2, (250, 400))  # Moves up & down
        }
        self.water = [

        ]
        # self.door = Door(1400, 400)

        self.walls = [

        ]


    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for water in self.water:
            water.check_collision(player)

    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))  # Green platforms

        for platform in self.moving_platforms:
            platform.draw(screen, camera)

        for water in self.water:
            water.draw(screen, camera)

        self.door.draw(screen, camera)
