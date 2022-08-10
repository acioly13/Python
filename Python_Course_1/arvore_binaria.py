class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None

    def get_chave(self):
        return self.chave

    def set_chave(self, chave):
        self.chave = chave

    def get_esquerda(self):
        return self.esquerda

    def set_esquerda(self, esquerda):
        self.esquerda = esquerda

    def get_direita(self):
        return self.direita

    def set_direita(self, direita):
        self.direita = direita


class ArvoreBinaria:

    def __init__(self):
        self.raiz = None

    def empty(self):
        #  verifica se a árvore está vazia
        if self.raiz is None:
            return True
        else:
            return False

    def inserir(self, chave):
        #  Insere um novo nó na árvore
        novo_no = No(chave)

        #  verifica se a árvore está vazia
        if self.empty():
            self.raiz = novo_no
        else:
            # se não estiver vazia, insere o nó na árvore
            no_pai = None
            no_atual = self.raiz

            while True:
                if no_atual is not None:
                    no_pai = no_atual
                    # verifica se vai para a esquerda ou direita
                    if novo_no.get_chave() < no_atual.get_chave():
                        # vai para esquerda
                        no_atual = no_atual.get_esquerda()
                    else:
                        # vai para direita
                        no_atual = no_atual.get_direita()

                else:
                    # se o no atual é None, entao encontrou onde inserir o nó
                    if novo_no.get_chave() < no_pai.get_chave():
                        no_pai.set_esquerda(novo_no)
                    else:
                        no_pai.set_direita(novo_no)
                    break

    def show(self, no_atual):
        # mostra a pre ordem (raiz-esquerda-direita)
        if no_atual is not None:
            print('%d' % no_atual.get_chave(), end=' ')
            self.show(no_atual.get_esquerda())
            self.show(no_atual.get_direita())

    def get_raiz(self):
        return self.raiz


t = ArvoreBinaria()
t.inserir(8)
t.inserir(3)
t.inserir(1)
t.inserir(6)
t.inserir(4)
t.inserir(7)
t.inserir(10)
t.inserir(14)
t.inserir(13)

t.show(t.get_raiz())
