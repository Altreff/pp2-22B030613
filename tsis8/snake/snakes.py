import pygame
import time
import random

snake_speed = 15
pygame.init()
window_x = 720
window_y = 480
pygame.mixer.music.load('background.mp3')
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.play(-1)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pink = pygame.Color(255, 100, 203)
yellow = pygame.Color(255, 255, 0)

pygame.init()

pygame.display.set_caption('Snakes')
game_window = pygame.display.set_mode((window_x, window_y))

fps = pygame.time.Clock()

snake_position = [100, 50]

snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
cherry_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
gold_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]
bomb_position = [random.randrange(1, (window_x // 10)) * 10,
                  random.randrange(1, (window_y // 10)) * 10]

fruit_spawn = True
bomb_spawn = True
cherry_spawn = True
gold_spawn = True

direction = 'RIGHT'
change_to = direction


score = 0
levelscore = 0
level = 1



def show_score(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)

def show_level(color, font, size):
    level_font = pygame.font.SysFont(font, size)
    level_surface = level_font.render('Level : ' + str(level), True, color)
    level_rect = level_surface.get_rect()
    level_rect.midtop = (window_x - 50, 0)
    game_window.blit(level_surface, level_rect)


def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render(
        'Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()


goldtimer = pygame.USEREVENT + 1
pygame.time.set_timer(goldtimer, 10000)


while True:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == goldtimer:
            gold_spawn = False
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10


    snake_body.insert(0, list(snake_position))
    if snake_position[0] == bomb_position[0] and snake_position[1] == bomb_position[1]:
        snake_body.pop()
        bomb_spawn = False
        pygame.mixer.Sound('bomb.wav').play()
    if not bomb_spawn:
        bomb_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]

    bomb_spawn = True
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        levelscore += 10
        pygame.mixer.Sound('food.wav').play()
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
    fruit_spawn = True
    if snake_position[0] == cherry_position[0] and snake_position[1] == cherry_position[1]:
        score += 20
        levelscore += 20
        pygame.mixer.Sound('food.wav').play()
        cherry_spawn = False

    if not cherry_spawn:
        cherry_position = [random.randrange(1, (window_x // 10)) * 10,
                           random.randrange(1, (window_y // 10)) * 10]

    cherry_spawn = True
    if snake_position[0] == gold_position[0] and snake_position[1] == gold_position[1]:
        score += 30
        levelscore += 30
        pygame.mixer.Sound('food.wav').play()
        gold_spawn = False

    if not gold_spawn:
        gold_position = [random.randrange(1, (window_x // 10)) * 10,
                         random.randrange(1, (window_y // 10)) * 10]
    if levelscore >= 40:
        level += 1
        snake_speed += 4
        levelscore -= 40;
    gold_spawn = True
    game_window.fill(black)

    for pos in snake_body:
        pygame.draw.rect(game_window, green,
                         pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(game_window, white, pygame.Rect(
        fruit_position[0], fruit_position[1], 10, 10))
    pygame.draw.rect(game_window, red, pygame.Rect(
        bomb_position[0], bomb_position[1], 10, 10))
    pygame.draw.rect(game_window, pink, pygame.Rect(
        cherry_position[0], cherry_position[1], 10, 10))
    pygame.draw.rect(game_window, yellow, pygame.Rect(
        gold_position[0], gold_position[1], 10, 10))


    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()


    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(white, 'times new roman', 20)
    show_level(white, 'times new roman', 20)

    pygame.display.update()

    fps.tick(snake_speed)