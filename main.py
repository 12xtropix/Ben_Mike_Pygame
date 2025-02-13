import pygame
from player import Player  # Import Player class
from level1 import Level1
from level2 import Level2
from level3 import Level3
import config  # Import config settings


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)
        pygame.display.set_caption("Red Ball Clone")
        self.clock = pygame.time.Clock()
        self.running = True

        self.levels = [Level1(), Level2(), Level3()]
        self.current_level = 0
        self.player = Player()

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
        self.player.update(self.levels[self.current_level].platforms)

        # Check if player reached the right edge of the screen
        if self.player.rect.x > config.SCREEN_SIZE[0]:
            self.next_level()

        # Update moving platforms (if any) in the current level
        if hasattr(self.levels[self.current_level], "update"):
            self.levels[self.current_level].update()

    def next_level(self):
        if self.current_level < len(self.levels) - 1:
            self.current_level += 1
            self.player.rect.x = 50  # Reset player position

    def draw(self):
        self.screen.fill(config.BG_COLOR)
        self.levels[self.current_level].draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()


if __name__ == "__main__":
    game = Game()
    game.run()
