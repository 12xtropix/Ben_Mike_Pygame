import pygame
import config

class Player:
    def __init__(self):
        self.image = config.MC_IMAGE
        self.image = pygame.transform.scale(self.image, (30, 30))  # Scale the image to fit the player size
        self.original_image = self.image.copy()  # Keep a copy of the original image for rotation
        self.rect = self.image.get_rect(midbottom=(100, 450))  # Position the player at the initial location
        self.vel_y = 0
        self.on_ground = False
        self.rotation_angle = 0  # Track the rotation angle for the ball

    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.rotation_angle += 5  # Rotate when moving left
            print(f"Rotating left: {self.rotation_angle}")  # Debug output
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.rotation_angle -= 5  # Rotate when moving right
            print(f"Rotating right: {self.rotation_angle}")  # Debug output
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

        # Collision with static platforms
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

    def draw(self, screen, camera):
        rotated_image = pygame.transform.rotate(self.original_image, self.rotation_angle)
        rotated_rect = rotated_image.get_rect(center=self.rect.center)

        # Apply camera transformation
        adjusted_rect = camera.apply(self.rect)
        rotated_rect.topleft = adjusted_rect.topleft  # Align the rotated rect with the camera

        screen.blit(rotated_image, rotated_rect)