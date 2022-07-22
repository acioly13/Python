import unittest


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


class TestMath(unittest.TestCase):

    def test_potencia(self):
        self.assertEqual(potencia(2, 3), 8)

    def test_fatorial(self):
        self.assertEqual(fatorial(5), 120)

    def test_area_quadrado(self):
        self.assertEqual(area_quadrado(5), 35)


if __name__ == '__main__':
    unittest.main()