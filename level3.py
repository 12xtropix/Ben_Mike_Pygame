import pygame
import config

class MovingPlatform:
    def __init__(self, x, y, width, height, speed, range_y):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed
        self.range_y = range_y
        self.direction = 1  # Moving up/down

    def update(self):
        self.rect.y += self.speed * self.direction
        if self.rect.y < self.range_y[0] or self.rect.y > self.range_y[1]:
            self.direction *= -1  # Reverse direction when hitting limits

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 200, 200), self.rect)  # Cyan moving platform

class Level3:
    def __init__(self):
        self.platforms = [
            pygame.Rect(50, 550, 700, 20),  # Ground
            pygame.Rect(200, 480, 120, 20),  # Mid-level platform
            pygame.Rect(400, 400, 150, 20),  # Higher platform
        ]
        self.moving_platforms = [
            MovingPlatform(500, 300, 100, 20, 2, (250, 400))  # Moves up & down
        ]

    def update(self):
        for platform in self.moving_platforms:
            platform.update()

    def draw(self, screen):
        for platform in self.platforms:
            pygame.draw.rect(screen, (0, 255, 0), platform)  # Green platforms
        for platform in self.moving_platforms:
            platform.draw(screen)
