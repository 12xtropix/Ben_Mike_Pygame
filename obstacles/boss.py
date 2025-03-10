import config
from config import BOSS_IMAGE
import pygame

"""
This is our boss class, which functions like the enemies class but has a health parameter as well. It also has a different image.
"""

class Boss:
    def __init__(self, x, y, left_bound, right_bound):
        self.image = BOSS_IMAGE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.y_vel = 0
        self.left_bound = left_bound
        self.right_bound = right_bound
        self.speed = 2
        self.direction = 1
        self.health = 5
        self.top_limit = 500 - 40
        self.bottom_limit = 500

    def update(self): #this method has capabilities for vertical boss movement, but it is not implemented at this time.
        self.rect.x += self.speed * self.direction
        if self.rect.x <= self.left_bound:
            self.direction = 1
        elif self.rect.x >= self.right_bound:
            self.direction = -1
        if self.rect.y < self.top_limit and self.y_vel == -1:
            self.rect.y += 2
        elif self.rect.y <= self.top_limit and self.y_vel == -1:
            self.y_vel = 1
            self.rect.y += 2
        elif self.rect.y > self.bottom_limit and self.y_vel == 1:
            self.rect.y -= 2
        elif self.rect.y >= self.bottom_limit and self.y_vel == 1:
            self.y_vel = -1
            self.rect.y -= 2
    def draw(self, screen, camera):
        square_rect = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        square_rect = camera.apply(square_rect)
        screen.blit(self.image, square_rect.topleft)

    def check_collision(self, player):
        if self.rect.colliderect(player.rect):
            if player.rect.bottom <= self.rect.top + 10: #if the player jumps on the head, make the boss take damage
                player.vel_y = -7
                self.health -= 1
                if self.health == 0: #if the boss dies, make the player jump very high and then destroy the boss
                    player.vel_y = -20
                    self.destroy()
            else: #if the player does not jump onto the boss head, reset the health and send the player back to the starting point
                self.health = 5
                player.rect.x = config.STARTING_X
                player.rect.y = config.STARTING_Y

    def destroy(self):
        self.rect.x = -1000
        self.rect.y = -1000
