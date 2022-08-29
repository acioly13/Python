class Grafo:
    def __init__(self, vertices):
        self.vertice = vertices
        self.grafo = [[] for i in range(vertices)]

    def adicionar_aresta(self, u, v):
        self.grafo[u-1].append(v-1)

    def mostrar_grafo(self):
        for i in range(self.vertice):
            print('%d: ' % (i+1), end='')
            for j in self.grafo[i]:
                print('%d ' % (j+1), end='')
            print('')


g = Grafo(5)
g.adicionar_aresta(1, 2)
g.adicionar_aresta(4, 1)
g.adicionar_aresta(2, 3)
g.adicionar_aresta(2, 5)
g.adicionar_aresta(5, 3)

g.mostrar_grafo()
