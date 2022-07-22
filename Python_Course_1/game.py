import simplegui, random

center_point = [50, 50]
window_width = 800
window_height = 600
radius = 20
score = 0


def draw(canvas):
    canvas.draw_circle(center_point, radius, 1, "White", "White")


def timer_handler():
    center_point[0] = random.randint(0, window_height)
    center_point[1] = random.randint(0, window_width)


def mouse_handler(position):
    global score
    # Calculo distancia entre ponto e click
    distance = ((center_point[0] - position[0]) ** 2 + (center_point[1] - position[1]) ** 2) ** 0.5
    # Verifica
    if distance < radius:
        score += 1
    else:
        if score > 0:
            score -= 1
    label.set_text("Score: " + str(score))


# Cria janela passando titulo, largura e altura
frame = simplegui.create_frame("Clique na bolinha", window_width, window_height)
# Cria temporizador passando intervalo e manipulador
timer = simplegui.create_timer(1000, timer_handler)
# Seta os manipuladores de eventos
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(mouse_handler)

label = frame.add_label("Score: " + str(score))
timer.start()
frame.start()
