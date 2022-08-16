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

    def remove(self, chave):
        """
            Caso 1: Nó a ser removido não tem filhos, basta setar a ligação do pai para none
            Caso 2: Nó a ser removido tem apenas 1 filho, basta colocar seu filho em seu lugar
            Caso 3: Nó a ser removido tem 2 filhos, basta pegar o menor elemento da sub-arvore a direita
        """
        # verifica se a árvore está vazia
        if self.empty():
            return None
        else:
            no_pai = None
            no_atual = self.raiz

            while no_atual is not None:
                # verifica se encontrou Nó a ser removido
                if no_atual.get_chave() == chave:
                    # Caso 1
                    if no_atual.get_esquerda() is None and no_atual.get_direita() is None:
                        # verifica se o nó a ser removido é a raiz
                        if no_pai is None:
                            self.raiz = None
                        else:
                            # verifica se o nó a ser removido é filho a esquerda ou direita
                            if no_atual == no_pai.get_esquerda():
                                no_pai.set_esquerda(None)
                            else:
                                no_pai.set_direita(None)

                    # Caso 2
                    elif no_atual.get_esquerda() is None and no_atual.get_direita() is not None or no_atual.get_esquerda() is not None and no_atual.get_direita() is None:
                        # verifica se o nó a ser removido é a raiz
                        if no_pai is None:
                            # se for a raiz, verifica se o nó a ser removido tem filho a esquerda ou direita
                            if no_atual.get_esquerda() is not None:
                                self.raiz = no_atual.get_esquerda()
                            else:
                                self.raiz = no_atual.get_direita()
                        else:
                            # verifica se o nó a ser removido é filho a esquerda
                            if no_atual.get_esquerda() is not None:
                                # verifica se o nó a ser removido é filho a esquerda
                                if no_pai.get_esquerda() and no_pai.get_esquerda().get_chave() == no_atual.get_chave():
                                    no_pai.set_esquerda(no_atual.get_esquerda())
                                else:  # se não for filho a esquerda, é filho a direita
                                    no_pai.set_direita(no_atual.get_esquerda())
                            else:  # se não o filho de  no_atual é filho a direita
                                # verifica se no_atual é filho a esquerda
                                if no_pai.get_esquerda() and no_pai.get_esquerda().get_chave() == no_atual.get_chave():
                                    no_pai.set_esquerda(no_atual.get_direita())
                                else:  # se não no_atual é filho a direita
                                    no_pai.set_direita(no_atual.get_direita())
                    # Caso 3
                    elif no_atual.get_esquerda() is not None and no_atual.get_direita() is not None:
                        # pega o menor elemento da subarvore a direita
                        pai_menor_no = no_atual
                        menor_no = no_atual.get_direita()
                        proximo_menor_no = no_atual.get_direita().get_esquerda()
                        while proximo_menor_no is not None:
                            pai_menor_no = menor_no
                            menor_no = proximo_menor_no
                            proximo_menor_no = menor_no.get_esquerda()
                        # verifica se o nó a ser removido é a raiz
                        if no_pai is None:
                            # Caso especial: o nó que vai ser a nova raiz é filho da raiz
                            if self.raiz.get_direita().get_chave() == menor_no.get_chave():
                                menor_no.set_esquerda(self.raiz.get_esquerda())
                            else:
                                if pai_menor_no.get_esquerda() and pai_menor_no.get_esquerda().get_chave() == menor_no.get_chave():
                                    pai_menor_no.set_esquerda(None)
                                else:
                                    pai_menor_no.set_direita(None)

                                # seta os filhos à direita e esquerda de menor_no
                                menor_no.set_esquerda(no_atual.get_esquerda())
                                menor_no.set_direita(no_atual.get_direita())
                            # faz a raiz ser o menor_no
                            self.raiz = menor_no

                        else:
                            # verifica se o nó atual é filho a esquerda ou direita
                            if no_pai.get_esquerda() and no_pai.get_esquerda().get_chave() == no_atual.get_chave():
                                no_pai.set_esquerda(menor_no)
                            else:
                                no_pai.set_direita(menor_no)

                            # verifica se no menor é filho a esquerda ou a direita
                            if pai_menor_no.get_esquerda() and pai_menor_no.get_esquerda().get_chave() == menor_no.get_chave():
                                pai_menor_no.set_esquerda(None)
                            else:
                                pai_menor_no.set_direita(None)
                            # seta os filhos à direita e esquerda de menor_no
                            menor_no.set_esquerda(no_atual.get_esquerda())
                            menor_no.set_direita(no_atual.get_direita())
                    break
                no_pai = no_atual
                # verifica se vai para a esquerda ou direita
                if chave < no_atual.get_chave():
                    no_atual = no_atual.get_esquerda()
                else:
                    no_atual = no_atual.get_direita()


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
t.inserir(9)
t.show(t.get_raiz())
print("")
t.remove(8)
t.show(t.get_raiz())
