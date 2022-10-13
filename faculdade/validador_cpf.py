# Validador CPF

class CPF:
    def __init__(self, cpf):
        self.cpf = cpf

    def valida_tamanho_cpf(self):
        if len(self.cpf) == 11:
            return True
        else:
            return False

    def valida_caracteres_cpf(self):
        if self.cpf.isnumeric():
            return True
        else:
            return False

    def valida_digito_cpf(self):
        soma_digito_1,  soma_digito_2 = 0, 0
        lista = list(self.cpf)
        if lista[0] == lista[1] == lista[2] == lista[3] == lista[4] == lista[5] == lista[6] == lista[7] == lista[8] == lista[9] == lista[10]:
            return False
        else:
            for i in range(0, 9):
                soma_digito_1 += int(lista[i]) * (10 - i)
            resto1 = int(soma_digito_1 * 10) % 11
            if resto1 == 10:
                resto1 = 0

            for i in range(0, 10):
                soma_digito_2 += int(lista[i]) * (11 - i)
            resto2 = int(soma_digito_2 * 10) % 11
            if resto2 == 10:
                resto2 = 0

            if resto1 == int(lista[9]) and resto2 == int(lista[10]):
                return True
            else:
                return False

    def valida_cpf(self):
        if self.valida_tamanho_cpf() and self.valida_caracteres_cpf() and self.valida_digito_cpf():
            return True
        else:
            return False


cpf = CPF(input('Digite o CPF: '))
print(cpf.valida_tamanho_cpf())
print(cpf.valida_caracteres_cpf())
print(cpf.valida_digito_cpf())
print(cpf.valida_cpf())
