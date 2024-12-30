import pygame
import random

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аркадная Игра: Космическое Приключение")

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Игрок
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 10

# Враги
enemy_size = 50
enemy_speed = 8
enemy_count = 5  # Количество врагов
enemies = [[random.randint(0, WIDTH - enemy_size), random.randint(-HEIGHT, 0)] for _ in range(enemy_count)]

# Бонусы
bonus_size = 30
bonus_pos = [random.randint(0, WIDTH - bonus_size), 0]
bonus_speed = 7

# Параметры игры
score = 0
game_over = False
clock = pygame.time.Clock()

# Пули игрока и врагов
bullets = []
bullet_speed = 20
enemy_bullets = []
enemy_bullet_speed = 15

# Задержка выстрелов игрока
bullet_cooldown = 500  # Милисекунды
last_bullet_time = pygame.time.get_ticks()  # Время последнего выстрела

# Основной игровой цикл
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    
    # Проверка времени для выстрела игрока
    current_time = pygame.time.get_ticks()
    if keys[pygame.K_SPACE] and current_time - last_bullet_time > bullet_cooldown:
        bullets.append([player_pos[0] + player_size // 2, player_pos[1]])  # Добавляем пулю игрока
        last_bullet_time = current_time  # Обновляем время последнего выстрела

    # Движение врагов и стрельба
    for enemy in enemies:
        enemy[1] += enemy_speed
        if enemy[1] > HEIGHT:
            enemy[1] = random.randint(-HEIGHT, 0)
            enemy[0] = random.randint(0, WIDTH - enemy_size)

        # Враги стреляют периодически
        if random.randint(0, 100) < 2:  # 5% вероятность выстрела
            enemy_bullets.append([enemy[0] + enemy_size // 2, enemy[1] + enemy_size])

    # Движение пуль врагов
    for enemy_bullet in enemy_bullets:
        enemy_bullet[1] += enemy_bullet_speed
        if enemy_bullet[1] > HEIGHT:  # Если выходит за пределы игрового окна, удаляем пулю
            enemy_bullets.remove(enemy_bullet)

    # Движение пуль игрока
    for bullet in bullets:
        bullet[1] -= bullet_speed
        if bullet[1] < 0:  # Если выходит за пределы игрового окна, удаляем пулю
            bullets.remove(bullet)

    # Проверка на столкновения с врагами
    for enemy in enemies:
        for bullet in bullets:
            if (enemy[0] <= bullet[0] <= enemy[0] + enemy_size) and (enemy[1] <= bullet[1] <= enemy[1] + enemy_size):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                enemies.append([random.randint(0, WIDTH - enemy_size), random.randint(-HEIGHT, 0)])  # Добавляем нового врага
                break

    # Проверка на столкновения с врагами и игроком
    for enemy in enemies:
        if (enemy[0] >= player_pos[0] and enemy[0] < player_pos[0] + player_size) or \
           (player_pos[0] >= enemy[0] and player_pos[0] < enemy[0] + enemy_size):
            if (enemy[1] >= player_pos[1] and enemy[1] < player_pos[1] + player_size) or \
               (player_pos[1] >= enemy[1] and player_pos[1] < enemy[1] + enemy_size):
                game_over = True

    # Проверка на столкновения пуль врагов с игроком
    for enemy_bullet in enemy_bullets:
        if (enemy_bullet[0] >= player_pos[0] and enemy_bullet[0] < player_pos[0] + player_size) or \
           (player_pos[0] >= enemy_bullet[0] and player_pos[0] < enemy_bullet[0] + 5):  # Ширина пули 5 пикселей
            if (enemy_bullet[1] >= player_pos[1] and enemy_bullet[1] < player_pos[1] + player_size):
                game_over = True

    # Отрисовка
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))  # Игрок

    # Рисуем врагов
    for enemy in enemies:
        pygame.draw.rect(screen, RED, (enemy[0], enemy[1], enemy_size, enemy_size))  # Враги

    # Рисуем бонус
    pygame.draw.rect(screen, GREEN, (bonus_pos[0], bonus_pos[1], bonus_size, bonus_size))  # Бонус

    # Рисуем пули игрока
    for bullet in bullets:
        pygame.draw.rect(screen, BLACK, (bullet[0], bullet[1], 5, 10))  # Пули игрока

    # Рисуем пули врагов
    for enemy_bullet in enemy_bullets:
        pygame.draw.rect(screen, RED, (enemy_bullet[0], enemy_bullet[1], 5, 10))  # Пули врагов

    # Отображение счета
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Счет: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))

    bonus_pos[1] += bonus_speed
    if bonus_pos[1] > HEIGHT:
        bonus_pos[1] = 0
        bonus_pos[0] = random.randint(0, WIDTH - bonus_size)

    if (bonus_pos[0] >= player_pos[0] and bonus_pos[0] < player_pos[0] + player_size) or \
       (player_pos[0] >= bonus_pos[0] and player_pos[0] < bonus_pos[0] + bonus_size):
        if (bonus_pos[1] >= player_pos[1] and bonus_pos[1] < player_pos[1] + player_size) or \
           (player_pos[1] >= bonus_pos[1] and player_pos[1] < bonus_pos[1] + bonus_size):
            score += 30 
            bonus_pos[1] = 0
            bonus_pos[0] = random.randint(0, WIDTH - bonus_size)

    pygame.display.update()
    clock.tick(30)

pygame.quit()