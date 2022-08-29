import heapq
class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome


class FilaPrioridade:

    def __init__(self):
        self.__fila = []
        self.__indice = 0

    def inserir(self, item, prioridade):
        heapq.heappush(self.__fila, (-prioridade, self.__indice, item))
        self.__indice += 1

    def remover(self):
        return heapq.heappop(self.__fila)[-1]


fila = FilaPrioridade()
fila.inserir(Pessoa('João'), 20)
fila.inserir(Pessoa('Pedro'), 16)
fila.inserir(Pessoa('Felipe'), 25)

print(fila.remover())