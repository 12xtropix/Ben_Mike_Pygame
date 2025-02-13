import pygame
import sys

def startlevel4(screen):
    # Set up colors
    R = (255, 0, 0)
    G = (0, 255, 0)
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Width = 850
    Height = 600

    # Ball setup
    ball = pygame.Surface((40, 40))  # Ball size
    ball.fill(R)
    ball_rect = ball.get_rect(center=(Width // 2, Height // 2))

    # Multiple obstacles setup
    obstacles = [
        pygame.Rect(150, 250, 100, 20),
        pygame.Rect(300, 350, 100, 20),
        pygame.Rect(500, 450, 100, 20),
    ]

    # Movement speed
    ball_speed = 5

    # Game loop for level 4
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(White)

        # Draw the ball and obstacles
        screen.blit(ball, ball_rect)
        for obs in obstacles:
            pygame.draw.rect(screen, Black, obs)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movement controls (WASD or Arrow Keys)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            ball_rect.x -= ball_speed
        if keys[pygame.K_RIGHT]:
            ball_rect.x += ball_speed
        if keys[pygame.K_UP]:
            ball_rect.y -= ball_speed
        if keys[pygame.K_DOWN]:
            ball_rect.y += ball_speed

        # Check for collision with obstacles
        for obs in obstacles:
            if ball_rect.colliderect(obs):
                ball_rect.x = Width // 2  # Reset ball position if it hits an obstacle

        # Simple win condition: reach the top-right corner
        if ball_rect.colliderect(pygame.Rect(Width - 50, 50, 40, 40)):
            win_text = pygame.font.Font(None, 50).render("You Win!", True, G)
            screen.blit(win_text, (Width // 2 - 100, Height // 2))

        # Update the screen
        pygame.display.flip()
        clock.tick(60)
