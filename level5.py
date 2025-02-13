import pygame

def startlevel5(screen):
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

    # Moving platform setup
    platform = pygame.Rect(100, 300, 200, 20)

    # Enemies setup (simple rectangles for now)
    enemies = [
        pygame.Rect(350, 100, 50, 50),
        pygame.Rect(600, 200, 50, 50)
    ]

    # Movement speed
    ball_speed = 5
    platform_speed = 3

    # Game loop for level 5
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill(White)

        # Draw the ball, platform, and enemies
        screen.blit(ball, ball_rect)
        pygame.draw.rect(screen, Black, platform)
        for enemy in enemies:
            pygame.draw.rect(screen, (0, 0, 255), enemy)

        # Move the platform
        platform.x += platform_speed
        if platform.right >= Width or platform.left <= 0:
            platform_speed *= -1

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

        # Check for collisions with enemies
        for enemy in enemies:
            if ball_rect.colliderect(enemy):
                ball_rect.x = Width // 2  # Reset ball position if it hits an enemy

        # Simple win condition: reach the top-right corner
        if ball_rect.colliderect(pygame.Rect(Width - 50, 50, 40, 40)):
            win_text = pygame.font.Font(None, 50).render("You Win!", True, G)
            screen.blit(win_text, (Width // 2 - 100, Height // 2))

        # Update the screen
        pygame.display.flip()
        clock.tick(60)
