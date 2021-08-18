class No:
    def __init__(self, chave=None, esquerda=None, direita=None):
        self.chave = chave
        self.esquerda = esquerda
        self.direita = direita

    def __repr__(self):
        return "%s <- %s -> %s" % (self.esquerda and self.esquerda.chave,
                                   self.chave,
                                   self.direita and self.direita.chave)


def visita_ordem(raiz):
    # ponto de parada da funçao
    if not raiz:
        return

    # Visitar, primeiramente o nó-filho da esquerda
    visita_ordem(raiz.esquerda)
    # visita o nó corrente (nó pai ou nó raiz)
    print(raiz)
    # visita, por ultimo o nó filho da direita
    visita_ordem(raiz.direita)


def insere(raiz, no):
    # o no deve ser inserido na raiz
    if raiz is None:
        raiz = no

    # se o valor do nó tiver
    elif raiz.chave < no.chave:


# Testando a classe No
raiz = No(40)
raiz.esquerda = No(20)
raiz.direita = No(60)

raiz.direita.esquerda = No(50)
raiz.direita.direita = No(70)

raiz.esquerda.esquerda = No(10)
raiz.esquerda.direita = No(30)

visita_ordem(raiz)
"""
print('Arvore Binaria: ', raiz)
print('Arvore Binaria: ', raiz.esquerda)
print('Arvore Binaria: ', raiz.direita)
"""
