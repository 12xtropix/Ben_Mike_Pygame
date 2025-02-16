import pygame
import config
import math

class Water:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.start_time = pygame.time.get_ticks()  # Store start time when the water is created

    def draw(self, screen, camera):
        # Apply the camera offset to the water's position (call apply on the camera object)
        adjusted_rect = camera.apply(self.rect)  # Adjusted water position based on the camera

        # Calculate elapsed time
        elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000  # Time in seconds

        # Parameters for the cells
        cell_width = 10  # Width of each "cell" in the water surface
        wave_amplitude = 10  # Height of the waves (vertical movement)
        wave_frequency = 2  # Controls how fast the wave oscillates
        wave_speed = 4  # Speed of wave movement

        points = []

        # Loop through each cell across the width of the water surface
        for i in range(adjusted_rect.x, adjusted_rect.x + adjusted_rect.width, cell_width):
            # Calculate oscillation offset for each cell
            if i // cell_width % 2 == 0:
                # Even-numbered cells are "high" when the time is right
                y_offset = wave_amplitude * math.sin(wave_frequency * (elapsed_time + (i * wave_speed)))
                if (y_offset > 0):
                    y_offset = 0
            else:
                # Odd-numbered cells are "flat" or the opposite
                y_offset = -wave_amplitude * math.sin(wave_frequency * (elapsed_time + (i * wave_speed)))
                if (y_offset > 0):
                    y_offset = 0

            # Add points for each "slice", oscillating between 0 and maximum height
            points.append((i, adjusted_rect.y + adjusted_rect.height + y_offset))

        # Pin the first point (left-most) at the base level (do not oscillate)
        points[0] = (adjusted_rect.x, adjusted_rect.y + adjusted_rect.height)

        # Pin the last point (right-most) at the same base level
        points[-1] = (adjusted_rect.x + adjusted_rect.width, adjusted_rect.y + adjusted_rect.height)

        # Draw the polygon with the oscillating points
        pygame.draw.polygon(screen, (0, 0, 255), points)

    def check_collision(self, player):

        if self.rect.colliderect(player.rect):
            player.rect.x = config.STARTING_X
            player.rect.y = config.STARTING_Y
