import pygame
import sys
from button import Button

pygame.init()

# setup area
Width, Height = 850, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Red Ball Game Menu')

White = (255,255,255)
R = (255,0,0)
G = (0,255,0)
B = (0,0,255)

font = pygame.font.Font(None, 40)
banner_font = pygame.font.Font(None, 60)

# Create buttons
start_button = Button("Level Selector", 75, 400, 200, 50, G, B)
shop_button = Button("Shop",            325, 400, 200, 50, G, B)
wardrobe_button = Button("Wardrobe",    575, 400, 200, 50, G, B)
back_button = Button("Back",            325, 450, 200, 50, G, B)




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