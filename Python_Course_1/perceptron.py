"""
    Implementação da rede neural Perceptron
    w = w + N * (d(k) - y) * x(k)
"""
import random, copy


class Perceptron:

    def __init__(self, amostras, saidas, taxa_aprendizado=0.1, epocas=1000, limiar=-1):
        self.amostras = amostras  # todas as amostras
        self.saidas = saidas  # saídas respectivas de cada amostra
        self.taxa_aprendizado = taxa_aprendizado  # taxa de aprendizado
        self.epocas = epocas  # número de épocas
        self.limiar = limiar  # limiar
        self.num_amostras = len(amostras)  # número de amostras
        self.num_amostra = len(amostras[0])  # número de elementos por amostra
        self.pesos = []  # vetor de pesos

    # função de ativação: degrau bippolar(sinal)
    def sinal(self, u):
        return 1 if u >= 0 else -1

    # Função de treinamento da rede
    def treinar(self):

        # adiciona -1 para cada uma das amostras
        for amostra in self.amostras:
            amostra.insert(0, -1)

        # inicia o vetor de peso com valores aleatorios
        for i in range(self.num_amostra):
            self.pesos.append(random.random())

        # insere o limiar no vetor de pesos
        self.pesos.insert(0, self.limiar)

        # inicia o contador de épocas
        num_epocas = 0

        while True:
            erro = False  # erro inicialmente é falso

            # para todas as amostras de treinamento
            for i in range(self.num_amostras):
                u = 0
                """
                    realiza o somatorio, o limite (self.amostra +1)
                    porque foi inserifo o -1 para cada amostra
                """
                for j in range(self.num_amostra + 1):
                    u += self.pesos[j] * self.amostras[i][j]

                # obtém a saída da rede usando a função de ativação
                y = self.sinal(u)

                # verifica se a saida da rede é diferente da saida desejada
                if y != self.saidas[i]:

                    # calcula o erro: subtração entre saida desejada e a saida da rede
                    erro_aux = self.saidas[i] - y

                    # faz o ajuste dos pesos para cada elemento da amostra
                    for j in range(self.num_amostra + 1):
                        self.pesos[j] = self.pesos[j] + self.taxa_aprendizado * erro_aux * self.amostras[i][j]
                    erro = True  # ainda existe erro

            # incrementa o número de épocas
            num_epocas += 1

            # critério de parada: épocas ou erro = 0
            if num_epocas > self.epocas or not erro:
                break

    # Função de teste da rede
    # recebe uma amostra para ser classificada e o nome das classes
    # utiliza funcao sinal, se é -1 entao é classe1, senão classe2
    def testar(self, amostra, classe1, classe2):
        # insere o -1
        amostra.insert(0, -1)

        # utiliza o vetor de pesos que foi ajustado no treinamento
        u = 0
        for i in range(self.num_amostra + 1):
            u += self.pesos[i] * amostra[i]

        # calcula a saida da rede
        y = self.sinal(u)

        # verifica se é classe1 ou classe2
        if y == -1:
            print('Classe: %s' % classe1)
        else:
            print('Classe: %s' % classe2)


print('\nA ou B?\n')

# amostras de treinamento
amostras = [[0.1, 0.4, 0.7], [0.3, 0.7, 0.2], [0.6, 0.9, 0.8], [0.5, 0.7, 0.1]]
# saidas desejadas
saidas = [1, -1, -1, 1]
# conjunto de amostras de testes
testes = copy.deepcopy(amostras)
# cria uma rede Perceptron
rede = Perceptron(amostras=amostras, saidas=saidas, taxa_aprendizado=0.1, epocas=1000)
# treina a rede
rede.treinar()
# testa a rede com uma amostra
for teste in testes:
    rede.testar(teste, 'A', 'B')