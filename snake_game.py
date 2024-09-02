import pygame
import sys
import time
import random

# 定义一些常用颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class SnakeGame:
    def __init__(self):
        self.width = 1024
        self.height = 768
        self.bg_color = BLUE
        self.snake_color = GREEN
        self.food_color = RED

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

    def start(self):
        snake_position = [(200, 200), (220, 200), (240, 200)]
        food_position = (400, 300)
        direction = 'right'
        score = 0

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != 'down':
                        direction = 'up'

                    elif event.key == pygame.K_DOWN and direction != 'up':
                        direction = 'down'

                    elif event.key == pygame.K_LEFT and direction != 'right':
                        direction = 'left'

                    elif event.key == pygame.K_RIGHT and direction != 'left':
                        direction = 'right'

            head = snake_position[-1]

            if direction == 'up':
                new_head = (head[0], head[1] - 20)
            elif direction == 'down':
                new_head = (head[0], head[1] + 20)
            elif direction == 'left':
                new_head = (head[0] - 20, head[1])
            elif direction == 'right':
                new_head = (head[0] + 20, head[1])

            snake_position.append(new_head)

            if (snake_position[-1][0] < 0 or
                    snake_position[-1][0] >= self.width or
                    snake_position[-1][1] < 0 or
                    snake_position[-1][1] >= self.height or
                    snake_position[-1] in snake_position[:-1]):
                break

            if (snake_position[-1][0] == food_position[0] and
                    snake_position[-1][1] == food_position[1]):
                score += 1
                food_position = (random.randint(0, self.width - 20) // 20 * 20,
                                 random.randint(0, self.height - 20) // 20 * 20)
            else:
                snake_position.pop(0)

            self.screen.fill(self.bg_color)
            for pos in snake_position:
                pygame.draw.rect(self.screen, self.snake_color, (pos[0], pos[1], 20, 20))
            pygame.draw.rect(self.screen, self.food_color, (food_position[0], food_position[1], 20, 20))

            font = pygame.font.Font(None, 36)
            text = font.render('分数：' + str(score), True, WHITE)
            self.screen.blit(text, (10, 10))

            pygame.display.flip()

            time.sleep(0.2)

            self.clock.tick(60)

        print('游戏结束。')
        print('你的最高分是' + str(score) + '分。')

if __name__ == '__main__':
    game = SnakeGame()
    random.seed(time.time())
    game.start()