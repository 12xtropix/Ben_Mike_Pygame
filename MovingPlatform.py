import pygame

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