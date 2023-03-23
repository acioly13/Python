import pygame
import random

# Inicializa a pygame
pygame.init()

# Define cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define a tela
window_size = (800, 600)

# Inicializa a janela
window = pygame.display.set_mode(window_size)

# Seta titulo para a janela
pygame.display.set_caption("Rocket Game")

# carrega imagem de fundo
img_rocket = pygame.image.load("rocket.png")

# posição da imagem



speed = 5  # velocidade da imagem
score = 0  # pontuação
rocket_positions = []  # lista de posições
rocket_positions.append([window_size[0], random.randint(0, window_size[1])])
rocket_pos = rocket_positions.append([window_size[0], random.randint(0, window_size[1])])



def score_text(score):
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score) + ' - Velocidade: ' + str(speed) + 'x', True, BLACK)
    return text


def update_position(match=False):
    global rocket_positions, speed, score

    for i in range(len(rocket_positions)):
        # atualiza a posição no eixo horizontal
        rocket_positions[i][0] -= speed

        # verifica se a imagem saiu da tela
        if rocket_positions[i][0] + img_rocket.get_rect().size[0] <= 0 or match:
            # atualiza as posiçooes da imagem
            rocket_positions[i][0] = window_size[0]
            rocket_positions[i][1] = random.randint(img_rocket.get_rect().size[0],
                                                    window_size[1] - img_rocket.get_rect().size[0])

            speed += 1  # aumenta a velocidade
            if speed > 20:
                speed = 1

            # verifica se não foi clique do mouse
            if not match:
                if score > 0:
                    score -= 1


done = True  # variavel de controle do loop
rocket = None  # Verifica colisão

# Loop principal
while done:
    # Verifica se o usuário quer fechar a janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # evento para sair do jogo
            done = False  # atualiza a flag para sair do loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(rocket_positions)):
                rocket_rect = pygame.Rect(rocket_positions[i], img_rocket.get_rect().size)
                if rocket_rect.collidepoint(event.pos):
                    score += 1
                    update_position(True)
                    break
            else:
                if score > 0:
                    score -= 1

    # Preenche o fundo com a cor branca
    window.fill(WHITE)

    # Desenha a imagem na tela
    for rocket_pos in rocket_positions:
        rocket = window.blit(img_rocket, rocket_pos)

    # Desenha o texto
    window.blit(score_text(score), (0, 0))

    # Atualiza a tela
    pygame.display.update()

    # delay de 1/10 segundos
    pygame.time.delay(100)

    # atualiza a posição
    update_position()

pygame.quit()
