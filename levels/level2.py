import pygame
import config
from config import ENEMY_IMAGE
from objects.door import Door
from obstacles.enemies import Enemy
from obstacles.spike import Spike
from objects.MovingPlatform import MovingPlatform



class Level2:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 100, 20),  # Start
            pygame.Rect(150, 600, 1000, 20),  # Ground
            pygame.Rect(1150, 500, 200, 20),
            pygame.Rect(1380, 600, 600, 20),
            pygame.Rect(1600, 50, 200, 20),
            pygame.Rect(1750, 150, 150, 20),

        ]
        self.walls =[
            pygame.Rect(1500, 350, 20, 250),  # wall
            pygame.Rect(1650, 350, 20, 250),
            pygame.Rect(1800, 350, 20, 250),
            pygame.Rect(1950, 350, 20, 250)
        ]


        self.moving_platforms = {
            MovingPlatform(1560, 500, 30, 20, 2, (400, 550)),
            MovingPlatform(1710, 500, 30, 20, 2, (400, 550)),
            MovingPlatform(1860, 500, 30, 20, 2, (400, 550)),
            MovingPlatform(1395, 500, 30, 20, 2, (400, 550)),
            MovingPlatform(2000, 500, 100, 20, 2, (175
                                                   , 500))


        } # Moves up & down


        self.spikes = [
            Spike(200, 580, 40, 20),  # Add spikes on the floor
            Spike(250, 580, 40, 20),
            Spike(300, 580, 40, 20),

            Spike(450, 580, 40, 20),
            Spike(500, 580, 40, 20),
            Spike(550, 580, 40, 20),

            Spike(700, 580, 40, 20),
            Spike(750, 580, 40, 20),
            Spike(800, 580, 40, 20),

            Spike(1380, 580, 30, 20),
            Spike(1410, 580, 30, 20),
            Spike(1440, 580, 30, 20),
            Spike(1470, 580, 30, 20),

            Spike(1520, 580, 30, 20),
            Spike(1550, 580, 30, 20),
            Spike(1580, 580, 30, 20),
            Spike(1610, 580, 30, 20),

            Spike(1670, 580, 30, 20),
            Spike(1700, 580, 30, 20),
            Spike(1730, 580, 30, 20),
            Spike(1760, 580, 30, 20),

            Spike(1820, 580, 30, 20),
            Spike(1850, 580, 30, 20),
            Spike(1880, 580, 30, 20),
            Spike(1910, 580, 30, 20)




        ]
        self.enemies =  [
        Enemy(200, 573, 200, 400),
        Enemy(200, 573, 400, 600),
        Enemy(200, 573, 600, 800),
        Enemy(200, 573, 800, 1000)
        ]
        self.door = Door(1320, 75)


    def update(self, player):
        for platform in self.moving_platforms:
            platform.update()

        for spike in self.spikes:
            spike.check_collision(player)
    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))  # Green platforms
        self.door.draw(screen, camera)
        for enemy in self.enemies:
            enemy.draw(screen, camera)  # Call the draw method on each enemy instance
        for spike in self.spikes:
            spike.draw(screen, camera)
        self.door.draw(screen, camera)
        for platform in self.moving_platforms:
            platform.draw(screen, camera)
        for wall in self.walls:
            pygame.draw.rect(screen, (255, 0, 0), camera.apply(wall))  # Red walls for visibility



