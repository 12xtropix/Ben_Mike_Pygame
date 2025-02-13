import pygame
import config  # Ensure you have a config.py file with GRAVITY and JUMP_STRENGTH

class Player:
    def __init__(self):
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)  # Red ball
        self.rect = self.image.get_rect(midbottom=(100, 500))
        self.vel_y = 0
        self.on_ground = False

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP] and self.on_ground:
            print("Jumping!")  # Debugging output
            self.vel_y = config.JUMP_STRENGTH
            self.on_ground = False

    def update(self, platforms):
        self.vel_y += config.GRAVITY  # Apply gravity
        self.rect.y += self.vel_y  # Move vertically

        self.check_collisions(platforms)  # Check collisions with platforms

    def check_collisions(self, platforms):
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:  # Falling down
                    self.rect.bottom = platform.top
                    self.vel_y = 0
                    self.on_ground = True
                    print("Player landed on a platform.")  # Debugging output
                elif self.vel_y < 0:  # Jumping up (hitting ceiling)
                    self.rect.top = platform.bottom
                    self.vel_y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

