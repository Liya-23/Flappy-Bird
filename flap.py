import pygame
import random

# Initialize Pygame
pygame.init()

# Window dimensions
WIDTH = 288
HEIGHT = 512

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

   # Load game assets
background_image = pygame.image.load("background.png")
bird_image = pygame.image.load("bird.png")
pipe_image = pygame.image.load("pipe.png")

# Bird properties
bird_x = 50
bird_y = 200
bird_speed = 0
bird_gravity = 0.5

# Pipe properties
pipe_x = WIDTH
pipe_y = 0
pipe_width = 70
pipe_height = random.randint(150, 350)
pipe_speed = 3

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_speed = -10

    # Update bird position
    bird_speed += bird_gravity
    bird_y += bird_speed

    # Update pipe position
    pipe_x -= pipe_speed

    # Check collision with pipe
    if bird_x + bird_image.get_width() > pipe_x and bird_x < pipe_x + pipe_width:
        if bird_y < pipe_height or bird_y + bird_image.get_height() > pipe_height + 150:
            running = False

    # Check if pipe has passed the bird
    if pipe_x + pipe_width < bird_x:
        score += 1
        pipe_x = WIDTH
        pipe_height = random.randint(150, 350)

    # Check if bird hits the ground or goes above the window
    if bird_y + bird_image.get_height() > HEIGHT or bird_y < 0:
        running = False 

    # Draw elements on the screen
    window.blit(background_image, (0, 0))
    window.blit(bird_image, (bird_x, bird_y))
    window.blit(pipe_image, (pipe_x, pipe_y))
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    # Update the display
    pygame.display.update()

# Quit the game
# pygame.quit()
