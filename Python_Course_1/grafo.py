class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]

    def adicionar_aresta(self, u, v):
        self.grafo[u - 1][v - 1] = 1
        self.grafo[v - 1][u - 1] = 1

    def show(self):
        for i in self.grafo:
            for j in i:
                print(j, end=' ')
            print('')

    def busca_ligacao(self, u, v):
        if self.grafo[u - 1][v - 1] == 1:
            return True
        else:
            return False


g = Grafo(5)
g.adicionar_aresta(1, 3)
g.adicionar_aresta(3, 4)
g.adicionar_aresta(2, 3)
g.adicionar_aresta(3, 5)
g.adicionar_aresta(4, 5)
g.show()
print(g.busca_ligacao(1, 3))
