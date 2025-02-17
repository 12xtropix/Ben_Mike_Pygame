import pygame
import config
# Door class
class Door:
    def __init__(self, x, y):
        self.front = pygame.Rect(x, y, 5, 20)
        self.top = pygame.Rect(x, y+20, 10, 5)
        self.back = pygame.Rect(x+20, y, 5, 20)
        self.middle = pygame.Rect(x, y, 20, 20)

    def draw(self, screen, camera):
        front_rect = camera.apply(self.front)
        top_rect = camera.apply(self.top)
        back_rect = camera.apply(self.back)
        middle_rect = camera.apply(self.middle)

        pygame.draw.rect(screen, (0, 3, 250), front_rect)
        pygame.draw.rect(screen, (190, 3, 0), top_rect)
        pygame.draw.rect(screen, (0, 3, 250), back_rect)
        pygame.draw.rect(screen, (190, 3, 250), middle_rect)

    def check_collision(self, player):
        # Check if any part of the door's rect collides with the player's rect
        return self.front.colliderect(player.rect) or self.top.colliderect(player.rect) or \
               self.back.colliderect(player.rect) or self.middle.colliderect(player.rect)
