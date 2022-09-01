from collections import defaultdict


# vertice/no/node
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_nome(self):
        return self.nome

    def get_idade(self):
        return self.idade


# # aresta/link/edge
# class Amizade:
#     def __init__(self, pessoa1, pessoa2):
#         self.pessoa1 = pessoa1
#         self.pessoa2 = pessoa2
#
#     def get_pessoa1(self):
#         return self.pessoa1
#
#     def get_pessoa2(self):
#         return self.pessoa2


# grafo/graph
class Grafo:
    def __init__(self):
        self.grafo = defaultdict(list)

    def add_amizade(self, p1, p2):
        self.grafo[p1.get_nome()].append(p2)
        self.grafo[p2.get_nome()].append(p1)

    def show_amizades(self, pessoa):
        for amizade in self.grafo[pessoa.get_nome()]:
            print(f'{amizade.get_nome()}')


g = Grafo()
p1 = Pessoa('Maria', 20)
p2 = Pessoa('Pedro', 30)
p3 = Pessoa('Diego', 18)
p4 = Pessoa('Carol', 25)
p5 = Pessoa('Yankee', 14)
g.add_amizade(p1, p2)
g.add_amizade(p1, p3)
g.add_amizade(p2, p4)
g.add_amizade(p4, p3)
g.add_amizade(p3, p5)
g.add_amizade(p5, p1)

g.show_amizades(p3)
