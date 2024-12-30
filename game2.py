import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Игра с двигающимся врагом")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Игрок
player_size = 15
player_pos = [WIDTH // 2, HEIGHT // 2]
player_health = 50

# Враг
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), random.randint(0, HEIGHT - enemy_size)]
enemy_speed = 7

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
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= speed
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += speed

    # Движение врага к игроку
    if enemy_pos[0] < player_pos[0]:
        enemy_pos[0] += enemy_speed
    if enemy_pos[0] > player_pos[0]:
        enemy_pos[0] -= enemy_speed
    if enemy_pos[1] < player_pos[1]:
        enemy_pos[1] += enemy_speed
    if enemy_pos[1] > player_pos[1]:
        enemy_pos[1] -= enemy_speed

    # Проверка на столкновение с врагом
    if (enemy_pos[0] >= player_pos[0] and enemy_pos[0] < player_pos[0] + player_size) or \
       (player_pos[0] >= enemy_pos[0] and player_pos[0] < enemy_pos[0] + enemy_size):
        if (enemy_pos[1] >= player_pos[1] and enemy_pos[1] < player_pos[1] + player_size) or \
           (player_pos[1] >= enemy_pos[1] and player_pos[1] < enemy_pos[1] + enemy_size):
            player_health -= 10
            print(f"Вы столкнулись с врагом! Здоровье: {player_health}")
            if player_health <= 0:
                print("Игра окончена!")
                game_over = True

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, GREEN, (player_pos[0], player_pos[1], player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))

    # Отображение здоровья игрока
    font = pygame.font.Font(None, 36)
    health_text = font.render(f'Здоровье: {player_health}', True, BLACK)
    screen.blit(health_text, (10, 10))

    pygame.display.update()
    pygame.time.delay(30)

pygame.quit()