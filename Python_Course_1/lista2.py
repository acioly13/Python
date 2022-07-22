lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, c, d, e, f, g, h, _, j = lista
print(a, b, c, d, e, f, g, h, j)

nome = 'João'
c1, c2, _, _, = nome
print(c1, c2)


def funcao(x, y):
    return x**2,  y**2


r1, r2 = funcao(2, 3)
print(r1, r2)