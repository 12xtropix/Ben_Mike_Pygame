import pygame
from mainstuff.player import Player
from mainstuff.camera import Camera
from levels.level1 import Level1
from levels.level2 import Level2
from levels.level3 import Level3
from levels.level4 import Level4
import config

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)
        pygame.display.set_caption("Red Ball Clone")
        self.clock = pygame.time.Clock()
        self.running = True

        self.levels = [Level1(), Level2(), Level3(), Level4()]
        self.current_level = self.show_level_menu()  # Ask player to choose a level
        self.player = Player()

        self.camera = Camera(config.SCREEN_SIZE[0], config.SCREEN_SIZE[1])

    def show_level_menu(self):
        """Displays a menu for level selection."""
        font = pygame.font.Font(None, 50)
        selected_level = 0
        menu_running = True

        while menu_running:
            self.screen.fill((50, 50, 50))  # Dark background

            # Render text
            title_text = font.render("Select a Level:", True, (255, 255, 255))
            self.screen.blit(title_text, (config.SCREEN_SIZE[0] // 2 - 100, 100))

            # Render level options
            for i, level_name in enumerate(["Level 1", "Level 2", "Level 3", "Level 4"]):
                color = (255, 255, 0) if i == selected_level else (200, 200, 200)
                level_text = font.render(level_name, True, color)
                self.screen.blit(level_text, (config.SCREEN_SIZE[0] // 2 - 50, 200 + i * 60))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected_level = (selected_level - 1) % 4
                    elif event.key == pygame.K_DOWN:
                        selected_level = (selected_level + 1) % 4
                    elif event.key == pygame.K_RETURN:
                        menu_running = False  # Start game with selected level

        return selected_level  # Return the selected level index

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(config.FPS)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def update(self):
        self.player.update(self.levels[self.current_level].platforms, self.levels[self.current_level].moving_platforms)

        if hasattr(self.levels[self.current_level], "enemies"):
            for enemy in self.levels[self.current_level].enemies:
                enemy.update()
                if enemy.check_collision(self.player):
                    print("Collision with enemy detected!")

        print("player y-value is ", self.player.rect.y)
        print("player x-value is ", self.player.rect.x)

        self.camera.update(self.player)

        # Check if player reached the right edge of the screen
        if hasattr(self.levels[self.current_level], "update"):
            self.levels[self.current_level].update(self.player)

        # Check if the player has collided with the door to go to the next level
        if hasattr(self.levels[self.current_level], "door") and self.levels[self.current_level].door.check_collision(
                self.player):
            self.next_level()

        # Check if the player is out of bounds (e.g., falls off the screen)
        if self.player.rect.y > 700:
            self.player.rect.y = config.STARTING_Y
            self.player.rect.x = config.STARTING_X

    def next_level(self):
        if self.current_level < len(self.levels) - 1:
            self.current_level += 1
            self.player.rect.y = config.FLOOR - 25
            self.player.rect.x = 50  # Reset player position

    def draw(self):
        # Draw background image instead of solid color
        self.screen.fill((0, 0, 0))
        self.screen.blit(config.BACKGROUND_IMAGE, (0, 0))

        # Draw level elements and player
        self.levels[self.current_level].draw(self.screen, self.camera)
        self.screen.blit(self.player.image, self.camera.apply(self.player))

        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
