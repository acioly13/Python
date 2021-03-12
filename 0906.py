class Pilha:
    def __init__(self):
        self.__itens = []  # atributo privado

    def push(self, item):  # adiciona um elemento no topo
        self.__itens.append(item)

    def pop(self):  # remove o elemento do topo
        if self.isEmpty() == False:
            self.__itens.pop()

    def top(self):  # retorna o elemento do topo
        if self.isEmpty() == False:
            return self.__itens[len(self.__itens) - 1]
        return None

    def isEmpty(self):  # retorna true se a lista está vazia
        return self.__itens == []

    def size(self):  # retorna o tamanho da pilha
        return len(self.__itens)

    def items(self):
        return self.__itens


class Fila:
    def __init__(self, tamanho=0):
        self.__itens = []  # atributo privado
        self.__tamanho = tamanho  # atributo de tamanho da fila

    def isEmpty(self):  # retorna true se a lista está vazia
        return self.__itens == []

    def enqueue(self, item):  # adiciona um elemento no final
        if (self.__tamanho != 0):
            if (len(self.__itens) >= self.__tamanho):
                return False

        return self.__itens.insert(0, item)

    def dequeue(self):  # remove o elemento do inicio da fila
        if self.isEmpty() == False:
            self.__itens.pop()

    def peek(self):  # retorna o elemento do início da fila
        if self.isEmpty() == False:
            return self.__itens[len(self.__itens) - 1]
        return None

    def size(self):  # retorna o tamanho da pilha
        return len(self.__itens)

    def isFull(self):
        # true se a quantidade de itens for igual ao tamanho maximo definido
        return (len(self.__itens) == self.__tamanho)

    def items(self):
        return self.__itens


nomes = ['willian', 'george', 'andre',
         'alice', 'andre', 'aurora',
         'andre', 'thamires', 'aurora',
         'andre', 'phillip', 'alice',
         'alice', 'ted', 'adriel',
         'aurora', 'wilson', 'aurora',
         'andre', 'alice', 'marcel',
         'acioly', 'alice', 'vinicius',
         'alice',    'aurora', 'wilson',
         'wilson', 'pipstar', 'george',
         'phillip', 'wilson', 'willson',
         'ted', 'pipstar']


dic = {}  # Criei um dicionario vazio
for nome in nomes:  # cria o dicionario com os nomes de iteração zerados
    dic[nome] = "0"  # valor zero pra todos

for nome in nomes:  # cria os valores de repeticao dos nomes
    dic[nome] = str(int(dic[nome]) + 1)

listaOrdenada = []  # mais repetidos -> menos repetidos

# parametros da funcao
chaves = list(dic.keys())
valores = list(dic.values())

z = 0
w = len(dic)
while z < w:

    maiorVal = 0
    valor = 0
    i = 0  # variavel de iteracao
    x = len(chaves)  # tamanho da lista de chaves
    ind = 0
    while i < x:
        if maiorVal < int(valores[i]):
            maiorVal = int(valores[i])
            ind = i

        i += 1

    listaOrdenada.append(chaves[ind])
    chaves.remove(chaves[ind])
    valores.remove(valores[ind])
    z += 1

pilha = Pilha()
fila = Fila()

x = 0
while x < 4:
    pilha.push(listaOrdenada[x])
    x += 1

x = 1
while x <= 4:
    fila.enqueue(listaOrdenada[len(listaOrdenada) - x])
    x += 1

print(pilha.items())
print(fila.items())
