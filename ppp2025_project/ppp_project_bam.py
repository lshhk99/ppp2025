import sys
import random
import pygame
from pygame.locals import QUIT, KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN, Rect

#초기 설정
pygame.init()
SURFACE = pygame.display.set_mode((600, 600))
FPSCLOCK = pygame.time.Clock()
FOODS = []
SNAKE = []
(W, H) = (20, 20)

#음식생성
def add_food():
    while True:
        pos = (random.randint(0, W-1), random.randint(0, H-1))
        if pos in FOODS or pos in SNAKE:
            continue
        FOODS.append(pos)
        break

#음식 먹은 후 처리
def move_food(pos):
    i = FOODS.index(pos)
    del FOODS[i]
    add_food()

#화면 그리기
def paint(message, score):
    SURFACE.fill((0, 0, 0))
    for food in FOODS:
        pygame.draw.ellipse(SURFACE, (0, 255, 0), Rect(food[0]*30, food[1]*30, 30, 30))
    for body in SNAKE:
        pygame.draw.rect(SURFACE, (0, 255, 255), Rect(body[0]*30, body[1]*30, 30, 30))
    for index in range(20):
        pygame.draw.line(SURFACE, (64, 64, 64), (index*30, 0), (index*30, 600))
        pygame.draw.line(SURFACE, (64, 64, 64), (0, index*30), (600, index*30))
    if message != None:
        SURFACE.blit(message, (150, 300))
    font = pygame.font.SysFont(None, 36)
    score_msg = font.render(f"Score: {score}", True, (255, 255, 255))
    SURFACE.blit(score_msg, (10, 10))

    pygame.display.update()

#게임 초기화
def reset_game():
    global SNAKE, FOODS
    SNAKE.clear()
    FOODS.clear()
    SNAKE.append((int(W/2), int(H/2)))
    for _ in range(10):
        add_food()



def main():
    myfont = pygame.font.SysFont(None, 80)
    reset_game()
    direction = None
    score = 0
    speed = 10
    message = None
    game_over = False

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if game_over:
                    if event.key == pygame.K_r:
                        reset_game()
                        direction = None
                        score = 0
                        speed = 10
                        message = None
                        game_over = False
                        key = K_DOWN
                else:
                    if event.key in (K_LEFT, K_RIGHT, K_UP, K_DOWN):
                        if direction is None:
                            direction = event.key
                        elif (direction == K_LEFT and event.key != K_RIGHT) or \
                            (direction == K_RIGHT and event.key != K_LEFT) or \
                            (direction== K_UP and event.key != K_DOWN) or \
                            (direction == K_DOWN and event.key != K_UP):
                            direction = event.key

        if not game_over and direction is not None:
            if direction == K_LEFT:
                head = (SNAKE[0][0] - 1, SNAKE[0][1])
            elif direction == K_RIGHT:
                head = (SNAKE[0][0] + 1, SNAKE[0][1])
            elif direction == K_UP:
                head = (SNAKE[0][0], SNAKE[0][1] - 1)
            elif direction == K_DOWN:
                head = (SNAKE[0][0], SNAKE[0][1] + 1)

            if head in SNAKE or  head[0] < 0 or head[0] >= W or  head[1] < 0 or head[1] >= H:
                message = myfont.render("Game Over!", True, (255, 255, 0))
                game_over = True

            SNAKE.insert(0, head)
            if head in FOODS:
                move_food(head)
                score += 10
                if score % 50 == 0:
                    speed += 2
            else:
                SNAKE.pop()

        paint(message, score)
        FPSCLOCK.tick(speed)
if __name__ == "__main__":
    main()
