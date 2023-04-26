import pygame
import random
import schedule

# Cores No Formato RGB
white = (255, 255, 255)
red = (255, 0, 0)

# Inicializa o Pygame
pygame.init()

# largura e altura da janela
width, height = 800, 600

# Cria a janela
window = pygame.display.set_mode((width, height))

# Titulo da Janela
pygame.display.set_caption('Space Invaders')

# Carregando imagem da nave
img_nave = pygame.image.load('nave.png')

# Carregando imagem do inimigo
enemies, count_enemies = [], 5
for i in range(count_enemies):
    pos_x, pos_y = random.randint(10, width - 10), -10
    enemy = [pygame.image.load('enemy.png'), pos_x, pos_y]
    enemies.append(enemy)

# Posição inicial da nave
pos_nave = [350, 520]

# Carregando a imagem do míssel
img_missile = pygame.image.load('missile.png')

# Posição inicial do míssel
pos_missile = [None, None]

# Flag do missel
flag_missile = False

# Tempo restante em segundos
time_remaining = 60


# Atualiza os inimigos
def update_enemies():
    for i in range(count_enemies):
        enemies[i][2] += 1
        if enemies[i][2] > (height + 10):
            pos_x = random.randint(10, width - 10)
            enemies[i][1], enemies[i][2] = pos_x, -10


# Atualiza o míssel
def update_missile():
    global flag_missile
    if flag_missile:
        # Verifica se passou do limite da tela
        if pos_missile[1] < -img_missile.get_rect().size[1]:
            flag_missile = False
        else:
            pos_missile[1] -= 1


# Atualiza o tempo restante
def update_time_remaning():
    global time_remaning_text, time_remaining
    if time_remaining > 0:
        time_remaining -= 1
        time_remaning_text = font.render("Tempo: " + str(time_remaining), True, red)


# programa uma tarefa para ser executada a cada x segundos
schedule.every(0.01).seconds.do(update_enemies)
schedule.every(0.01).seconds.do(update_missile)
schedule.every(1).seconds.do(update_time_remaning)

# Pontuação do jogo
score = 0
font = pygame.font.Font(None, 30)
score_text = font.render("Score: " + str(score), True, red)

# Tempo restante
font_time = pygame.font.Font(None, 30)
time_remaning_text = font_time.render("Tempo: " + str(time_remaining), True, red)


# Atualiza a pontuação
def update_score(decrement=False):
    global score_text, score
    if time_remaining > 0:
        score = (score - 1) if decrement else (score + 1)
        score_text = font.render("Score: " + str(score), True, red)


# Resera a posição do inimigo
def reset_enemy(index):
    enemies[index][1] = random.randint(10, width - 10)
    enemies[index][2] = -10


# Flag para o loop principal
main_loop = True

# Main loop da aplicação
while main_loop:

    # busca por eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            main_loop = False

        # Verifica se a tecla espaço foi pressionada
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            flag_missile = True

    # Obtem a tecla pressionada
    pressed = pygame.key.get_pressed()
    # ocorrencia de evento de tecla pressionada
    if pressed[pygame.K_LEFT]:  # Eixo X
        pos_nave[0] -= 1
    elif pressed[pygame.K_RIGHT]:  # Eixo X
        pos_nave[0] += 1
    elif pressed[pygame.K_UP]:  # Eixo Y
        pos_nave[1] -= 1
    elif pressed[pygame.K_DOWN]:  # Eixo Y
        pos_nave[1] += 1

    window.fill(white)

    schedule.run_pending()

    # Verifica se o míssel está ativo
    if not flag_missile:
        pos_missile = [pos_nave[0], pos_nave[1]]

    # Desenha o míssel
    missile = window.blit(img_missile, pos_missile)

    nave = window.blit(img_nave, pos_nave)

    for i in range(count_enemies):
        enemy = window.blit(enemies[i][0], (enemies[i][1], enemies[i][2]))
        # Verifica colisão dos inimigos com a nave
        if nave.collidepoint((enemies[i][1], enemies[i][2])):
            reset_enemy(i)  # reseta o inimigo
            update_score(decrement=True)  # decrementa a pontuação

        # Verifica colisão dos inimigos com o míssel
        if missile.collidepoint((enemies[i][1], enemies[i][2])):
            reset_enemy(i)  # reseta o inimigo
            update_score()  # incrementa a pontuação

    window.blit(score_text, (10, 10))
    window.blit(time_remaning_text, (680, 10))
    pygame.display.flip()

# Finaliza o Pygame
pygame.quit()
