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

    def bfs(self, v):
        # lista de visitados
        visitados = [False] * self.vertices
        # marcar o vertice como visitado
        visitados[v - 1] = True
        # insere vertices na fila
        fila = [v - 1]
        print(f'{v} visitado')
        # enquanto a fila nao estiver vazia
        while len(fila) > 0:
            # obtem o primeiro elemento da fila
            v = fila[0]
            # para cada vertice u adjacente a v
            for u in range(self.vertices):
                # verifica se existe conexao
                if self.grafo[v][u] == 1:
                    # verifica se u não foi visitado
                    if not visitados[u]:
                        # marca u como visitado
                        visitados[u] = True
                        # insere u na fila
                        fila.append(u)
                        # imprime o elemento visitado
                        print(f'{u + 1} visitado')
            # remove o primeiro elemento da fila
            fila.pop(0)


g = Grafo(10)
g.adicionar_aresta(1, 2)
g.adicionar_aresta(1, 3)
g.adicionar_aresta(1, 4)
g.adicionar_aresta(2, 5)
g.adicionar_aresta(3, 6)
g.adicionar_aresta(3, 7)
g.adicionar_aresta(4, 8)
g.adicionar_aresta(5, 9)
g.adicionar_aresta(6, 10)

g.bfs(1)