import pygame
import config


class Player:
    def __init__(self):
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (15, 15), 15)  # Red ball
        self.rect = self.image.get_rect(midbottom=(100, 450))
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

    def update(self, platforms, moving_platforms, walls):
        self.vel_y += config.GRAVITY  # Apply gravity
        self.rect.y += self.vel_y  # Move vertically

        self.check_collisions(platforms, moving_platforms, walls)

    def check_collisions(self, platforms, moving_platforms, walls):
        self.on_ground = False

        for wall in walls:
            if self.rect.colliderect(wall):
                # Horizontal collision
                if self.rect.right > wall.left and self.rect.left < wall.right:
                    if self.rect.centerx < wall.centerx:
                        self.rect.right = wall.left  # Stop the player from moving right through the wall
                    elif self.rect.centerx > wall.centerx:
                        self.rect.left = wall.right  # Stop the player from moving left through the wall

                # Vertical collision (falling down or jumping up)
                if self.vel_y > 0:  # Falling down
                    if self.rect.bottom > wall.top and self.rect.top < wall.top:
                        self.rect.bottom = wall.top  # Prevent going through the wall
                        self.vel_y = 0  # Stop falling
                        self.on_ground = True  # Set player on ground
                elif self.vel_y < 0:  # Jumping up
                    if self.rect.top < wall.bottom and self.rect.bottom > wall.bottom:
                        self.rect.top = wall.bottom  # Prevent going through the ceiling
                        self.vel_y = 0  # Stop upward velocity

        # Collision with static platforms
        for platform in platforms:
            if self.rect.colliderect(platform):
                if self.vel_y > 0:  # Falling down
                    self.vel_y = 0
                    self.rect.bottom = platform.top
                    self.on_ground = True
                    print("Player landed on a platform.")  # Debugging output
                elif self.vel_y < 0:  # Jumping up (hitting ceiling)
                    self.rect.top = platform.bottom
                    self.vel_y = 0

        # Collision with moving platforms
        for moving_platform in moving_platforms:
            if self.rect.colliderect(moving_platform.rect):
                if self.vel_y > 0:  # Falling down
                    self.rect.bottom = moving_platform.rect.top
                    self.vel_y = moving_platform.speed  # Move with platform
                    self.on_ground = True
                    print("Player landed on a moving platform.")  # Debugging output
                elif self.vel_y < 0 and moving_platform.speed > 0:
                    self.rect.top = moving_platform.rect.bottom
                    self.vel_y = moving_platform.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


