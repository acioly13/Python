# Algoritmo K-Means
import random
from math import sqrt


class Ponto:

    def __init__(self, id_ponto, valores):
        self.id_ponto = id_ponto
        self.valores = valores
        self.total_valores = len(valores)
        self.id_cluster = -1

    def get_id(self):
        return self.id_ponto

    def set_cluster(self, id_cluster):
        self.id_cluster = id_cluster

    def get_cluster(self):
        return self.id_cluster

    def get_valor(self, indice):
        return self.valores[indice]

    def get_total_valores(self):
        return self.total_valores

    def add_valor(self, valor):
        self.valores.append(valor)


class Cluster:

    def __init__(self, id_cluster, ponto):
        self.id_cluster = id_cluster
        self.total_valores = ponto.get_total_valores()
        self.valores_centrais = []
        self.pontos = []

        for i in range(self.total_valores):
            self.valores_centrais.append(ponto.get_valor(i))
        self.pontos.append(ponto)

    def add_ponto(self, ponto):
        self.pontos.append(ponto)

    def remover_ponto(self, id_ponto):
        total_pontos = len(self.pontos)
        for i in range(total_pontos):
            if self.pontos[i].get_id() == id_ponto:
                self.pontos.pop(i)
                return True
        return False

    def get_valor_central(self, indice):
        return self.valores_centrais[indice]

    def set_valor_central(self, indice, valor):
        self.valores_centrais[indice] = valor

    def get_ponto(self, indice):
        return self.pontos[indice]

    def get_total_pontos(self):
        return len(self.pontos)

    def get_id(self):
        return self.id_cluster


class KMeans:

    def __init__(self, k, total_pontos, total_valores, max_iter):
        self.k = k
        self.total_pontos = total_pontos
        self.total_valores = total_valores
        self.max_iter = max_iter
        self.pontos = []
        self.clusters = []

    def get_id_centro_proximo(self, ponto):
        soma = 0.0
        id_cluster_centro = 0

        for i in range(self.total_valores):
            soma += pow(self.clusters[0].get_valor_central(i) - ponto.get_valor(i), 2)

        min_dist = sqrt(soma)

        for i in range(1, self.k):
            soma = 0.0
            for j in range(self.total_valores):
                soma += pow(self.clusters[i].get_valor_central(j) - ponto.get_valor(j), 2)
            dist = sqrt(soma)
            if dist < min_dist:
                min_dist = dist
                id_cluster_centro = i
        return id_cluster_centro

    def executar(self, pontos):
        if self.k > self.total_pontos:
            print('Número de clusters maior que o número de pontos')
            return False

        indices_proibidos = []
        # Escolhe K valores distintos para os centros dos clusters
        for i in range(self.k):
            while True:
                indice_ponto = random.randint(0, self.total_pontos - 1)
                if indice_ponto not in indices_proibidos:
                    indices_proibidos.append(indice_ponto)
                    pontos[indice_ponto].set_cluster(i)
                    cluster = Cluster(i, pontos[indice_ponto])
                    self.clusters.append(cluster)
                    break
        iter_ = 1
        while True:
            done = True
            # Associa cada ponto ao centro mais proximo
            for i in range(self.total_pontos):
                id_cluster_velho = pontos[i].get_cluster()
                id_cluster_proximo = self.get_id_centro_proximo(pontos[i])
                if id_cluster_velho != id_cluster_proximo:
                    if id_cluster_velho != -1:
                        self.clusters[id_cluster_velho].remover_ponto(pontos[i].get_id())
                    pontos[i].set_cluster(id_cluster_proximo)
                    self.clusters[id_cluster_proximo].add_ponto(pontos[i])
                    done = False

            # Recalcula os centros dos clusters
            for i in range(self.k):
                for j in range(self.total_valores):
                    total_pontos_cluster = self.clusters[i].get_total_pontos()
                    soma = 0.0
                    if total_pontos_cluster > 0:
                        for k in range(total_pontos_cluster):
                            soma += self.clusters[i].get_ponto(k).get_valor(j)
                        self.clusters[i].set_valor_central(j, soma / total_pontos_cluster)

            if done == True or iter_ >= self.max_iter:
                print('Parou na iteração %d' % iter_)
                break
            iter_ += 1

        # mostra os elementos de cada cluster
        for i in range(self.k):
            total_pontos_cluster = self.clusters[i].get_total_pontos()
            print('\nCluster %d: ' % (i + 1), end='')
            for j in range(total_pontos_cluster):
                print(' %d' % (self.clusters[i].get_ponto(j).get_id() + 1), end='')


if __name__ == "__main__":

    arq = open('dataset.txt')
    linhas = arq.readlines()
    arq.close()
    primeira_linha = linhas[0].split()
    num_pontos, num_atributos, num_clusters, max_iter = [int(x) for x in primeira_linha]
    print('%d %d %d %d' % (num_pontos, num_atributos, num_clusters, max_iter))
    pontos = []
    for i in range(1, num_pontos + 1):
        atributos = linhas[i].split()
        valores = [float(i) for i in atributos]
        ponto = Ponto(i - 1, valores)
        pontos.append(ponto)

    kmeans = KMeans(num_clusters, num_pontos, num_atributos, max_iter)
    kmeans.executar(pontos)
