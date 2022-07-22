import unittest
from ouro import main, areValidDigits


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.cpf_valido = main([0, '757.331.783-29'])  # CPF valido retorna True
        # self.cpf_invalido = main('111.111.111-00')  # CPF invalido retorna False

    # Testar CPF valido
    def test_cpf_valido(self):
        self.assertEqual(self.cpf_valido, True)

    # # Testar CPF invalido
    # def test_cpf_invalido(self):
    #     self.assertEqual(self.cpf_invalido, False)


if __name__ == '__main__':
    unittest.main()
