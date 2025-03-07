import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.water import Water
from obstacles.enemies import Enemy
from obstacles.boss import Boss
from objects.door import Door
from obstacles.spike import Spike

class Level5:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 100, 20), #starting platform
            pygame.Rect(200, 450, 100, 20), #second platform
            pygame.Rect(400, 300, 750, 20), #long platform

            pygame.Rect(1300, 450, 1200, 20), #water platform

            pygame.Rect(2700, 650, 500, 50) #boss platform

        ]
        self.moving_platforms = {
            MovingPlatform(1450, 430, 100, 20, 1, (405, 500)),  # Moves up & down
            MovingPlatform(1950, 430, 100, 20, 1, (405, 500))  # Moves up & down
        }
        self.water = [
            Water(1400, 440, 300, 10),  #water 1
            Water(1900, 440, 300, 10) #water 2
        ]
        self.spikes = [
            Spike(455,280, 40 , 20),
            Spike(560, 280, 40, 20),
            Spike(605, 280, 40, 20),
            Spike(680, 280, 40, 20),

            Spike(765, 280, 40, 20),
            Spike(805, 280, 40, 20),
            Spike(880, 280, 40, 20),
            Spike(960, 280, 40, 20)
        ]
        self.enemies = [Enemy(1500, 423, 1400, 1600), #water enemies
                        Enemy(1600, 423, 1500, 1700), #water enemies
                        Enemy(2100, 423, 2000, 2200), #water enemies
                        Enemy(2000, 423, 1900, 2100)  #water enemies

                        ]
        self.bosses = [Boss(2950, 623, 2800, 3100)
             ]
        self.walls = [
            pygame.Rect(2700, 450, 20, 200),  # left wall
            pygame.Rect(3200, 450, 20, 200)  # right wall
        ]
        self.door = Door(2870, 200)

    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for boss in self.bosses:
            boss.update()
            boss.check_collision(player)

        for water in self.water:
            water.check_collision(player)

        for spike in self.spikes:
            spike.check_collision(player)

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

        for wall in self.walls:
            pygame.draw.rect(screen, (255, 0, 0), camera.apply(wall))

        for spike in self.spikes:
            spike.draw(screen,camera)

        self.door.draw(screen, camera)




