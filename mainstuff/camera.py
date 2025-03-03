import pygame
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)  # Camera view
        self.camera.width = width
        self.camera.height = height
        self.world_size = (5000, 1200)

    def apply(self, entity):
        """Adjusts the entity's position based on camera position."""
        # If the entity has a 'rect' attribute (like Player or pygame.Rect)
        if hasattr(entity, 'rect'):
            return entity.rect.move(self.camera.topleft)
        elif isinstance(entity, pygame.Rect):
            # If the entity is already a pygame.Rect (like a platform), move it directly
            return entity.move(self.camera.topleft)
        else:
            # If the entity is a tuple (e.g., position tuple), return the tuple adjusted by the camera
            return (entity[0] + self.camera.topleft[0], entity[1] + self.camera.topleft[1])

    def update(self, target):
        """Smoothly follow the player"""
        x = -target.rect.centerx + self.camera.width // 2
        y = -target.rect.centery + self.camera.height // 2

        # Implement a slight delay effect for smooth scrolling
        self.camera.x += (x - self.camera.x) * 0.1
        self.camera.y += (y - self.camera.y) * 0.1

        # Keep within world bounds
        self.camera.x = min(0, self.camera.x)
        self.camera.y = min(0, self.camera.y)
        self.camera.x = max(-(self.world_size[0] - self.camera.width), self.camera.x)
        self.camera.y = max(-(self.world_size[1] - self.camera.height), self.camera.y)

        #self.camera = pygame.Rect(x, y, self.camera.width, self.camera.height)
