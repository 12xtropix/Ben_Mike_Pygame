import pygame
import os
import random
import sys

# Initialize Pygame
pygame.init()

# Window setup
W, H = 800, 437
win = pygame.display.set_mode((W, H))
pygame.display.set_caption('Level 1')

bg = pygame.image.load(os.path.join('images', 'bg.png')).convert()
bg_width = bg.get_width()  # Get the width of the background
bg_x = 0  # Initialize bg_x outside the function to ensure it is always in scope

clock = pygame.time.Clock()

class player(object):
    run = [pygame.Surface((64, 64))]  # Red ball
    run[0].fill((255, 0, 0))  # Fill with red color

    jump = [pygame.Surface((64, 64))]  # Jump surface (same red ball)
    jump[0].fill((255, 0, 0))

    slide = [pygame.Surface((64, 64))]  # Slide surface (same red ball)
    slide[0].fill((255, 0, 0))

    fall = pygame.Surface((64, 64))  # Falling surface (same red ball)
    fall.fill((255, 0, 0))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.jumping = False
        self.sliding = False
        self.falling = False
        self.runCount = 0
        self.vel = 5  # How fast the ball moves
        self.facing_right = True
        self.gravity = 1  # Falling speed
        self.is_on_ground = True  # Whether the ball is on the ground or not

    def draw(self, win):
        # Red ball for all actions
        if self.falling:
            win.blit(self.fall, (self.x, self.y - 30))
        elif self.jumping:
            self.y -= 10  # Simulate jump
            win.blit(self.jump[0], (self.x, self.y))
        else:
            if self.runCount > 42:
                self.runCount = 0
            if self.facing_right:
                win.blit(self.run[0], (self.x, self.y))
            else:
                win.blit(pygame.transform.flip(self.run[0], True, False), (self.x, self.y))
            self.runCount += 1

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def fall_logic(self):
        if not self.is_on_ground:
            self.y += self.gravity  # Apply gravity
        if self.y >= H - 64:  # Check if ball reaches ground
            self.y = H - 64
            self.is_on_ground = True
            self.falling = False

class saw(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        win.blit(pygame.image.load(os.path.join('images', 'SAW0.png')), (self.x, self.y))

    def collide(self, rect):
        if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
            if rect[1] + rect[3] > self.hitbox[1]:
                return True
        return False

def startlevel1(screen):
    global bg_x  # Add global reference for bg_x in this function
    runner = player(200, 313, 64, 64)
    obstacles = []
    speed = 30
    score = 0
    run = True

    while run:
        screen.fill((255, 255, 255))

        # Move the background
        bg_x -= 4  # Speed of background scroll
        if bg_x <= -bg_width:
            bg_x = 0  # Reset the background when it goes off-screen

        # Draw the background
        screen.blit(bg, (bg_x, 0))
        if bg_x < 0:
            screen.blit(bg, (bg_x + bg_width, 0))  # Draw the next part of the background

        runner.draw(screen)

        # Draw score
        score_text = pygame.font.SysFont('comicsans', 30).render('Score: ' + str(score), 1, (255, 255, 255))
        screen.blit(score_text, (700, 10))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Game events
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            runner.x += runner.vel
            runner.facing_right = True
        if keys[pygame.K_LEFT]:
            runner.x -= runner.vel
            runner.facing_right = False
        if not runner.falling:
            if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
                runner.jumping = True

        # Add obstacles and handle collisions
        for obstacle in obstacles:
            if obstacle.collide(runner.get_rect()):
                pygame.quit()
                sys.exit()

        if random.randint(0, speed) == 0:
            obstacles.append(saw(900, random.randint(300, 400), 64, 64))

        for obstacle in obstacles:
            obstacle.draw(screen)
            obstacle.x -= 4  # Move the obstacle leftward

        runner.fall_logic()
        clock.tick(30)
