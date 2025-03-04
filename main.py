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
        self.current_level = self.show_level_menu()
        self.player = Player()
        self.camera = Camera(config.SCREEN_SIZE[0], config.SCREEN_SIZE[1])

    def show_level_menu(self):
        font = pygame.font.Font(None, 50)
        selected_level = 0
        menu_running = True

        while menu_running:
            self.screen.fill((50, 50, 50))
            title_text = font.render("Select a Level:", True, (255, 255, 255))
            self.screen.blit(title_text, (config.SCREEN_SIZE[0] // 2 - 100, 100))

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
                        menu_running = False

        return selected_level

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse click
                    if self.is_back_to_menu_button_clicked(event.pos):
                        self.current_level = self.show_level_menu()

        keys = pygame.key.get_pressed()
        self.player.handle_input(keys)

    def update(self):
        self.player.update(self.levels[self.current_level].platforms, self.levels[self.current_level].moving_platforms,
                           self.levels[self.current_level].walls)

        if hasattr(self.levels[self.current_level], "enemies"):
            for enemy in self.levels[self.current_level].enemies:
                enemy.update()
                if enemy.check_collision(self.player):
                    print("Collision with enemy detected!")

        self.camera.update(self.player)

        if hasattr(self.levels[self.current_level], "update"):
            self.levels[self.current_level].update(self.player)

        if hasattr(self.levels[self.current_level], "door") and self.levels[self.current_level].door.check_collision(self.player):
            self.next_level()

        if self.player.rect.y > 700:
            self.player.rect.y = config.STARTING_Y
            self.player.rect.x = config.STARTING_X

    def next_level(self):
        if self.current_level < len(self.levels) - 1:
            self.current_level += 1
            self.player.rect.y = config.FLOOR - 25
            self.player.rect.x = 50

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(config.BACKGROUND_IMAGE, (0, 0))
        self.levels[self.current_level].draw(self.screen, self.camera)
        self.screen.blit(self.player.image, self.camera.apply(self.player))

        # Draw circular "Back to Menu" button with a menu icon
        self.draw_back_to_menu_button()

        pygame.display.flip()

    def draw_back_to_menu_button(self):
        # Circle button configuration
        button_radius = 22
        button_x = config.SCREEN_SIZE[0] - button_radius - 10
        button_y = config.SCREEN_SIZE[1] - button_radius - 10

        # Draw circle button
        pygame.draw.circle(self.screen, (139,69, 19), (button_x, button_y), button_radius)

        # Draw menu icon (three horizontal lines)
        line_length = 20
        line_thickness = 3
        for i in range(3):
            pygame.draw.rect(self.screen, (255, 255, 255), (button_x - line_length // 2, button_y - 10 + i * 8, line_length, line_thickness))

    def is_back_to_menu_button_clicked(self, mouse_pos):
        button_radius = 30
        button_x = config.SCREEN_SIZE[0] - button_radius - 10
        button_y = config.SCREEN_SIZE[1] - button_radius - 10

        x, y = mouse_pos
        distance = ((x - button_x) ** 2 + (y - button_y) ** 2) ** 0.5
        return distance <= button_radius

if __name__ == "__main__":
    game = Game()
    game.run()