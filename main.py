import pygame
import sys
from button import Button
from level1 import startlevel1
from level2 import startlevel2
from level3 import startlevel3
from level4 import startlevel4
from level5 import startlevel5

pygame.init()

# setup area
Width, Height = 850, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Red Ball Game Menu')

White = (255, 255, 255)
R = (255, 0, 0)
G = (0, 255, 0)
B = (0, 0, 255)

font = pygame.font.Font(None, 40)
banner_font = pygame.font.Font(None, 60)

# Create buttons
start_button = Button("Level Selector", 75, 400, 200, 50, G, B)
shop_button = Button("Shop", 325, 400, 200, 50, G, B)
wardrobe_button = Button("Wardrobe", 575, 400, 200, 50, G, B)
back_button = Button("Back", 325, 450, 200, 50, G, B)

# Level buttons for level selector screen
level1_button = Button("Level 1", 75, 200, 200, 50, G, B)
level2_button = Button("Level 2", 325, 200, 200, 50, G, B)
level3_button = Button("Level 3", 575, 200, 200, 50, G, B)
level4_button = Button("Level 4", 75, 270, 200, 50, G, B)
level5_button = Button("Level 5", 325, 270, 200, 50, G, B)

def main_menu():
    while True:
        screen.fill(White)

        welcome_text = banner_font.render("Welcome to Red Ball!", True, R)
        welcome_rect = welcome_text.get_rect(center=(Width // 2, 100))
        screen.blit(welcome_text, welcome_rect)

        # Draw buttons
        start_button.draw(screen)
        shop_button.draw(screen)
        wardrobe_button.draw(screen)

        # Handle button clicks
        if start_button.is_clicked():
            level_selector()
        if shop_button.is_clicked():
            shop_menu()
        if wardrobe_button.is_clicked():
            wardrobe_menu()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

def level_selector():
    while True:
        screen.fill(White)

        # Draw "Back" button
        back_button.draw(screen)

        # Handle back button click
        if back_button.is_clicked():
            return  # Go back to main menu

        # Draw banner for level selector
        level_text = font.render("Level Selector", True, R)
        level_rect = level_text.get_rect(center=(Width // 2, 100))
        screen.blit(level_text, level_rect)

        # Draw the level buttons
        level1_button.draw(screen)
        level2_button.draw(screen)
        level3_button.draw(screen)
        level4_button.draw(screen)
        level5_button.draw(screen)

        # Handle level button clicks and only enter the level when the button is clicked
        if level1_button.is_clicked():
            startlevel1(screen)  # Run the level
            return  # After finishing the level, return to the level selector
        if level2_button.is_clicked():
            startlevel2(screen)
            return
        if level3_button.is_clicked():
            startlevel3(screen)
            return
        if level4_button.is_clicked():
            startlevel4(screen)
            return
        if level5_button.is_clicked():
            startlevel5(screen)
            return

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

def shop_menu():
    while True:
        screen.fill(White)

        # Draw "Back" button
        back_button.draw(screen)

        # Handle back button click
        if back_button.is_clicked():
            return  # Go back to main menu

        # Draw banner for shop menu
        shop_text = font.render("Shop", True, R)
        shop_rect = shop_text.get_rect(center=(Width // 2, 100))
        screen.blit(shop_text, shop_rect)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

def wardrobe_menu():
    while True:
        screen.fill(White)

        # Draw "Back" button
        back_button.draw(screen)

        # Handle back button click
        if back_button.is_clicked():
            return  # Go back to main menu

        # Draw banner for wardrobe menu
        wardrobe_text = font.render("Wardrobe", True, R)
        wardrobe_rect = wardrobe_text.get_rect(center=(Width // 2, 100))
        screen.blit(wardrobe_text, wardrobe_rect)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

# Run the main menu
if __name__ == "__main__":
    main_menu()
