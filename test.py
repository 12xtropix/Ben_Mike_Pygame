import pygame
import math
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
Width, Height = 850, 600
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Red Ball Game")

# Define colors
White = (255, 255, 255)
Red = (255, 0, 0)
Black = (0, 0, 0)
Green = (0, 255, 0)

# Set up fonts
font = pygame.font.Font(None, 40)
banner_font = pygame.font.Font(None, 60)

# Define the player (Red Ball)
ball = pygame.Surface((40, 40))  # Ball size
ball.fill(Red)
ball_rect = ball.get_rect(center=(Width // 2, Height // 2))

# Movement settings
ball_speed = 5
jump_speed = 12
gravity = 0.5
velocity_y = 0
on_ground = False

# Scroll setup
scroll = 0
bg = pygame.image.load("redballbackground.jpg").convert()  # Background image
tiles = math.ceil(Width / bg.get_width()) + 1  # Tiles for infinite scroll

# Infinite floor setup (Repeating platforms)
floor_sections = []

# Game loop
clock = pygame.time.Clock()


def update_platforms():
    global floor_sections
    # Make sure the floor sections move with the ball's movement
    for plat in floor_sections:
        # Scroll platform positions based on ball's movement
        plat.x += ball_speed if ball_rect.x > Width // 2 else -ball_speed

        # If platform moves off-screen, create a new section at the right
        if plat.right < 0:
            plat.left = floor_sections[-1].right + 10  # Add small gap between sections


def main_game():
    global velocity_y, on_ground, scroll, floor_sections
    running = True

    # Create initial floor sections
    for i in range(4):
        floor_sections.append(pygame.Rect(i * Width, Height - 50, Width, 50))

    while running:
        screen.fill(White)

        # Scroll the background based on the ball's horizontal movement
        i = 0
        while i < tiles:
            screen.blit(bg, (bg.get_width() * i + scroll, 0))
            i += 1

        # Get player input for movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ball_rect.x -= ball_speed
        if keys[pygame.K_RIGHT]:
            ball_rect.x += ball_speed

        # Handle jumping (check if the ball is on the ground)
        if keys[pygame.K_SPACE] and on_ground:
            velocity_y = -jump_speed
            on_ground = False

        # Apply gravity to the ball
        velocity_y += gravity
        ball_rect.y += velocity_y

        # Check for collisions with platforms (full collision on platform area)
        on_ground = False
        for plat in floor_sections:
            if ball_rect.colliderect(plat) and velocity_y > 0:  # Check for downward collision
                ball_rect.bottom = plat.top
                velocity_y = 0
                on_ground = True

        # Update the scroll based on the ball's horizontal position (without auto-scrolling)
        scroll = -ball_rect.x  # Scroll background and platforms based on the ball's movement

        # Prevent the scroll from going too far (stop at the edges)
        if scroll > 0:
            scroll = 0
        if scroll < -(bg.get_width() * (tiles - 1)):
            scroll = -(bg.get_width() * (tiles - 1))

        # Update platform positions for infinite floor
        update_platforms()

        # Draw floor sections (infinite floor)
        for plat in floor_sections:
            pygame.draw.rect(screen, Black, plat)

        # Draw the ball
        screen.blit(ball, ball_rect)

        # Simple win condition: reach the top-right corner
        if ball_rect.colliderect(pygame.Rect(Width - 50, 50, 40, 40)):
            win_text = banner_font.render("You Win!", True, Green)
            screen.blit(win_text, (Width // 2 - 100, Height // 2))

        # Event handling (quit game)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


# Main entry point
if __name__ == "__main__":
    main_game()
