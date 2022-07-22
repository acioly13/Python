# Calcular Fatorial
def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n-1)


# Calcular a potencia
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente-1)


# Calcular area do quadrado
def area_quadrado(lado):
    return lado * lado
