import pygame
import config
import math

class Angle:
    def __init__(self, magnitude, angle):
        self.magnitude = magnitude
        self.angle = angle  # Angle in degrees

        # Convert angle from degrees to radians for trigonometric functions
        angle_rad = math.radians(angle)

        # Calculate width and height using trigonometry
        self.width = magnitude * math.cos(angle_rad)  # Horizontal component
        self.height = magnitude * math.sin(angle_rad)  # Vertical component

        # Create a rect based on the calculated width and height
        self.rect = pygame.Rect(0, 0, self.width, self.height)

        # The offset of the rotation center (around the center of the platform)
        self.center = (self.rect.width / 2, self.rect.height / 2)

        # Create the platform's surface and rotate it
        self.image = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        self.image.fill((255, 0, 0))  # Red color
        self.image = pygame.transform.rotate(self.image, self.angle)

        # Recalculate the rect size after rotation
        self.rect = self.image.get_rect(center=self.center)

    def draw(self, screen, camera):
        # Draw the rotated surface to the screen at the platform's location
        camera_pos = camera.apply(self.rect.topleft)
        screen.blit(self.image, camera_pos)

    def check_collision(self, player):
        """Resets player position if they collide with the platform."""
        if self.rect.colliderect(player.rect):
            player.rect.x = config.STARTING_X
            player.rect.y = config.STARTING_Y
