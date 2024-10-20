import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Screen settings
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

# Game variables
snake_block = 10
snake_speed = 15
clock = pygame.time.Clock()

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("arial", 35)

# Functions
def display_score(score):
    value = score_font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for segment in snake_list:
        pygame.draw.rect(screen, GREEN, [segment[0], segment[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [SCREEN_WIDTH / 6, SCREEN_HEIGHT / 3])

def game_loop():
    game_over = False
    game_close = False

    # Snake settings
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    x_change = 0
    y_change = 0
    snake_list = []
    snake_length = 1

    # Food settings
    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press Q-Quit or C-Play Again", RED)
            display_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        # Event handling (movement)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        if x >= SCREEN_WIDTH or x < 0 or y >= SCREEN_HEIGHT or y < 0:
            game_close = True
        x += x_change
        y += y_change
        screen.fill(BLACK)

        pygame.draw.rect(screen, BLUE, [food_x, food_y, snake_block, snake_block])

        # Snake movement
        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Snake collision with itself
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
