import pygame


# Door class
class Door:
    def __init__(self, x, y):
        # Set the position of the finish line (door is now the finish line)
        self.x = x
        self.y = y
        self.width = 200  # Width of the finish line
        self.height = 20  # Height of the finish line

    def draw(self, screen, camera):
        # Create a camera-adjusted position for the finish line
        finish_line_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        finish_line_rect = camera.apply(finish_line_rect)

        # Drawing the checkered pattern for the finish line
        checkered_width = 20  # Width of each small rectangle
        checkered_height = self.height  # Height will be the height of the finish line
        for i in range(0, self.width, checkered_width * 2):
            # Alternate between black and white rectangles
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(finish_line_rect.x + i, finish_line_rect.y, checkered_width, checkered_height))  # Black
            pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(finish_line_rect.x + i + checkered_width, finish_line_rect.y, checkered_width, checkered_height))  # White

    def check_collision(self, player):
        # Check if the player collides with the finish line area
        finish_line_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return finish_line_rect.colliderect(player.rect)

