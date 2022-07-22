class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade

    def set_idade(self, idade):
        self.idade = idade


p1 = Pessoa('João', 24)
p2 = Pessoa('Maria', 22)
p3 = Pessoa('Pedro', 20)
p4 = Pessoa('Nathy', 24)
pessoas = [p1, p2, p3]
pessoas.append(p4)
print(f'Nome: {p1.get_nome()}')
print(f'Idade: {p1.get_idade()}')


for pessoa in pessoas:
    print(pessoa.get_nome())

print(f'Idade: {p1.get_idade()}')
p1.set_idade(25)
print(f'Idade: {p1.get_idade()}')

pares = [num for num in range(1, 11) if num % 2 == 0]
print(pares)