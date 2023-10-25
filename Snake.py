import pygame

# Initialize Pygame
pygame.init()

# Get the screen dimensions
screen_info = pygame.display.Info()
width, height = screen_info.current_w, screen_info.current_h

# Snake Game Display in Fullscreen
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Snake Game")

# Set background color to black
background_color = (0, 0, 0)

# Set green color
green = (0, 255, 0)

# Set red color
red = (255, 0, 0)

# Apple Dimensions
ball_width = 25
ball_height = 25

# Snake Dimensions
rect_width = 75
rect_height = 25

# Create the ball (a rectangular surface)
ball = pygame.Surface((ball_width, ball_height))
ball.fill(red)  # Fill the apple with red

# Create the rectangle (a rectangular surface)
rect = pygame.Surface((rect_width, rect_height))
rect.fill(green)  # Fill the snake with green

# Initial position of the apple
ball_x, ball_y = width // 2 - 50, height // 2  # Start in the center of the screen, shifted to the left

# Initial position of the Snake
rect_x, rect_y = width // 2 + 30, height // 2  # Start in the center of the screen, shifted to the right

# Initial speed of the snake
speed = 5

# Initial direction of the snake
direction = 'UP'

# Main loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        direction = 'UP'
    elif keys[pygame.K_DOWN]:
        direction = 'DOWN'
    elif keys[pygame.K_LEFT]:
        direction = 'LEFT'
    elif keys[pygame.K_RIGHT]:
        direction = 'RIGHT'

    # Move the snake
    if direction == 'UP' and rect_y > 0:
        rect_y -= speed
    elif direction == 'DOWN' and rect_y < height - rect_height:
        rect_y += speed
    elif direction == 'LEFT' and rect_x > 0:
        rect_x -= speed
    elif direction == 'RIGHT' and rect_x < width - rect_width:
        rect_x += speed

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the apple
    screen.blit(ball, (ball_x, ball_y))

    # Draw the rectangle (snake)
    screen.blit(rect, (rect_x, rect_y))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
