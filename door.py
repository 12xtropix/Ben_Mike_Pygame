import pygame
import config
# Door class
class Door:
    def __init__(self):
        self.front = pygame.Rect(config.SCREEN_SIZE[0] - 100, 400, 5, 20)
        self.top = pygame.Rect(config.SCREEN_SIZE[0] - 100, 410, 10, 5)
        self.back = pygame.Rect(config.SCREEN_SIZE[0] - 90, 400, 5, 20)
        self.middle = pygame.Rect(config.SCREEN_SIZE[0] - 100, 400, 10, 10)

    def draw(self, screen, camera):
        front_rect = camera.apply(self.front)
        top_rect = camera.apply(self.top)
        back_rect = camera.apply(self.back)
        middle_rect = camera.apply(self.middle)

        pygame.draw.rect(screen, (190, 3, 250), front_rect)
        pygame.draw.rect(screen, (190, 3, 250), top_rect)
        pygame.draw.rect(screen, (190, 3, 250), back_rect)
        pygame.draw.rect(screen, (190, 3, 250), middle_rect)

    def check_collision(self, player):
        # Check if any part of the door's rect collides with the player's rect
        return self.front.colliderect(player.rect) or self.top.colliderect(player.rect) or \
               self.back.colliderect(player.rect) or self.middle.colliderect(player.rect)
