import pygame
import config
from objects.door import Door

class Level1:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, config.FLOOR, 100, 20), # pyramid platforms
            pygame.Rect(200, 450, 100, 20),
            pygame.Rect(400, 350, 100, 20),
            pygame.Rect(600, 250, 100, 20),
            pygame.Rect(800, 150, 100, 20),
            pygame.Rect(1000, 250, 100, 20),
            pygame.Rect(1200, 350, 100, 20), # pyramid platforms
            pygame.Rect(1400, 450, 600, 20),

            pygame.Rect(1700, 150, 20, 300), # wall

        ]
        self.moving_platforms = [

        ]
        self.ground = [pygame.Rect(50, config.FLOOR, 100, 20)]
        self.door = Door(3000, 200)


    def draw(self, screen, camera):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), camera.apply(platform))  # Green platforms
        for ground in self.ground:
            pygame.draw.rect(screen,(255,255,255),camera.apply(ground))
        self.door.draw(screen,camera)





