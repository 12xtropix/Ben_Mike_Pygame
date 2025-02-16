import pygame
import config

class Spike:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen, camera):
        pygame.draw.polygon(screen, (255, 0, 0), [
            camera.apply((self.rect.x, self.rect.y + self.rect.height)),  # Bottom-left
            camera.apply((self.rect.x + self.rect.width // 2, self.rect.y)),  # Top-center
            camera.apply((self.rect.x + self.rect.width, self.rect.y + self.rect.height))  # Bottom-right
        ])

    def check_collision(self, player):
        """Resets player position if they collide with a spike."""
        if self.rect.colliderect(player.rect):
            player.rect.x = config.STARTING_X
            player.rect.y = config.STARTING_Y
