import pygame
import sys
import random

# Inicialização do pygame
pygame.init()

# Cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Configurações da tela
WIDTH, HEIGHT = 400, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jogo da Cobrinha")

# Inicialização da cobrinha
snake = [(100, 50), (90, 50), (80, 50)]
snake_direction = "RIGHT"
score = 0

# Comida
food_pos = (random.randrange(1, (WIDTH//10)) * 10,
            random.randrange(1, (HEIGHT//10)) * 10)

# Função para desenhar a cobrinha na tela
def draw_snake(snake):
    for pos in snake:
        pygame.draw.rect(win, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))

# Função para desenhar a comida na tela
def draw_food(food_pos):
    pygame.draw.rect(win, RED, pygame.Rect(
        food_pos[0], food_pos[1], 10, 10))

# Função principal do jogo
def main():
    global snake_direction, score

    # Velocidade da cobrinha
    snake_speed = 15

    # Verifica se o jogo está rodando
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != "DOWN":
                    snake_direction = "UP"
                if event.key == pygame.K_DOWN and snake_direction != "UP":
                    snake_direction = "DOWN"
                if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                    snake_direction = "LEFT"
                if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                    snake_direction = "RIGHT"

        # Movimento da cobrinha
        if snake_direction == "UP":
            snake_head = (snake[0][0], snake[0][1] - 10)
        if snake_direction == "DOWN":
            snake_head = (snake[0][0], snake[0][1] + 10)
        if snake_direction == "LEFT":
            snake_head = (snake[0][0] - 10, snake[0][1])
        if snake_direction == "RIGHT":
            snake_head = (snake[0][0] + 10, snake[0][1])

        snake.insert(0, snake_head)

        # Verifica se a cobrinha comeu a comida
        if snake[0] == food_pos:
            score += 1
            food_pos = (random.randrange(1, (WIDTH//10)) * 10,
                        random.randrange(1, (HEIGHT//10)) * 10)
        else:
            snake.pop()

        # Verifica se a cobrinha colidiu com a parede
        if snake[0][0] >= WIDTH or snake[0][0] < 0 or snake[0][1] >= HEIGHT or snake[0][1] < 0:
            game_over = True

        # Verifica se a cobrinha colidiu com o próprio corpo
        for block in snake[1:]:
            if snake[0] == block:
                game_over = True

        # Preenche a tela com a cor de fundo
        win.fill(WHITE)

        # Desenha a comida
        draw_food(food_pos)

        # Desenha a cobrinha
        draw_snake(snake)

        # Atualiza a tela
        pygame.display.flip()

        # Define a velocidade do jogo
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
