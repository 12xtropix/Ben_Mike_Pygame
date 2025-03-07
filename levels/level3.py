import pygame
import config
from objects.MovingPlatform import MovingPlatform
from obstacles.spike import Spike
from objects.door import Door
from obstacles.water import Water

class Level3:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 850, 20),  # Ground
            pygame.Rect(1070, 300, 500, 20),  # Mid-level platform
            pygame.Rect(1120, 400, 500, 20), # Higher platform
            pygame.Rect(1070, 500, 500, 20),  # Higher platform
            pygame.Rect(1120, 600, 500, 20),  # Higher platform
            pygame.Rect(1070, 700, 1000, 20)

        ]
        self.water = [
            Water(200, config.FLOOR - 20, 700, 20),  # Add a water pit
        ]
        self.walls =[
            pygame.Rect(1070, 300, 20, 400),
            pygame.Rect(1620,0, 20, 620)
        ]
        self.moving_platforms = {
            MovingPlatform(200, 300, 100, 20, 2, (300, 500)),
            MovingPlatform(450, 300, 100, 20, 2, (300, 500)),
            MovingPlatform(700, 300, 100, 20, 2, (300, 500)),
            MovingPlatform(950, 300, 100, 20, 2, (300, 500))
        }
        self.spikes = [
            #Spike(300, config.FLOOR - 20, 40, 20),  # Add spikes on the floor
            # Spike(600, config.FLOOR - 20, 40, 20)
        ]
        self.door = Door(600, 200)

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
