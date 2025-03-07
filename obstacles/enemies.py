import config
from config import ENEMY_IMAGE
import pygame

"""
This is our enemy class, which allows us to create enemies on the screen. 
"""

class Enemy:
    def __init__(self, x, y, left_bound, right_bound):
        self.image = ENEMY_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.speed = 2
        self.direction = 1

    def update(self):
        self.rect.x += self.speed * self.direction
        if self.rect.x <= self.left_bound: #these if statements define the horizontal boundaries of the enemies, and they will alternate between them
            self.direction = 1
        elif self.rect.x >= self.right_bound: #the other side of the boundary
            self.direction = -1

    def draw(self, screen, camera):
        square_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        square_rect = camera.apply(square_rect)
        screen.blit(self.image, square_rect.topleft)

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            if player.rect.bottom <= self.rect.top + 10: #if the player has jumped on the top of the enemy, destroy the enemy and boost the player
                player.vel_y = -10
                self.destroy()
            else: #otherwise send the player back to the start
                player.rect.x = config.STARTING_X
                player.rect.y = config.STARTING_Y

    def destroy(self): #this is the destroy method, which sends the enemy to off the screen
        self.rect.x = -1000
        self.rect.y = -1000
