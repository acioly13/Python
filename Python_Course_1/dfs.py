class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[0] * vertices for i in range(vertices)]
        self.visitados = [False] * vertices

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

    def dfs(self, u):
        self.visitados[u - 1] = True
        print('%d visitado' % u)
        for i in range(1, self.vertices + 1):
            if self.grafo[u - 1][i - 1] == 1 and self.visitados[i - 1] == False:
                self.dfs(i)


g = Grafo(5)
g.adicionar_aresta(1, 4)
g.adicionar_aresta(4, 2)
g.adicionar_aresta(4, 5)
g.adicionar_aresta(2, 5)
g.adicionar_aresta(5, 3)

g.dfs(1)
