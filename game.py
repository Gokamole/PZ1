import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аркадная игра")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Игрок
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]

# Препятствие
obstacle_size = 50
obstacle_pos = [random.randint(0, WIDTH - obstacle_size), 0]

# Скорость движения
speed = 10
game_over = False

# Основной игровой цикл
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += speed

    # Обновление позиции препятствия
    obstacle_pos[1] += speed
    if obstacle_pos[1] > HEIGHT:
        obstacle_pos[1] = 0
        obstacle_pos[0] = random.randint(0, WIDTH - obstacle_size)

    # Проверка на столкновение
    if (obstacle_pos[0] >= player_pos[0] and obstacle_pos[0] < player_pos[0] + player_size) or \
       (player_pos[0] >= obstacle_pos[0] and player_pos[0] < obstacle_pos[0] + obstacle_size):
        if (obstacle_pos[1] >= player_pos[1] and obstacle_pos[1] < player_pos[1] + player_size):
            print("Игра окончена!")
            game_over = True

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (obstacle_pos[0], obstacle_pos[1], obstacle_size, obstacle_size))
    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()