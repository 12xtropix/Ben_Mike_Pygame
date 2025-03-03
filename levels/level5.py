import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.water import Water
from obstacles.enemies import Enemy
from obstacles.boss import Boss


class Level5:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 1500, 20),  # Ground
        ]
        self.moving_platforms = {
            MovingPlatform(550, 300, 100, 20, 2, (250, 400))  # Moves up & down
        }
        self.water = [
            Water(300, config.FLOOR - 20, 1000, 20),  # Add a water pit
        ]
        self.enemies = [Enemy(200, config.FLOOR - 27, 100, 300),
                        Enemy(600, config.FLOOR - 27, 500, 700)
                        ]
        self.bosses = [Boss(400, config.FLOOR - 27, 300, 500)]


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

        for enemy in self.enemies:
            enemy.draw(screen, camera)

        for boss in self.bosses:
            boss.draw(screen, camera)

