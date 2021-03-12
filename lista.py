class No:
    def __init__(self, valini):
        self.valor = valini
        self.proximo = None

    def pegaValor(self):
        return self.valor

    def pegaProximo(self):
        return self.proximo

    def insereValor(self, novovalor):
        self.valor = novovalor

    def insereProximo(self, novoproximo):
        self.proximo = novoproximo


class ListaNOrd:
    def __init__(self):
        self.inicio = None

    def Vazia(self):
        return self.inicio == None

    def Inserir(self, item):
        temp = No(item)
        temp.insereProximo(self.inicio)
        self.inicio = temp

    def Buscar(self, item):
        atual = self.inicio
        encontrou = False

        while atual != None and encontrou == False:
            if atual.pegaValor() == item:
                encontrou = True
            else:
                atual = atual.pegaProximo()

        return encontrou

    def Tamanho(self):
        atual = self.inicio
        conta = 0

        while atual != None:
            conta += 1
            atual = atual.pegaProximo()
        return conta

    def Show(self):
        atual = self.inicio

        while atual != None:
            print(atual.pegaValor(), end=' ')
            atual = atual.pegaProximo()
        print(' ')

    def Excluir(self, valor):
        atual = self.inicio
        previo = None
        encontrou = False
        while atual != None and encontrou == False:
            if atual.pegaValor() == valor:
                encontrou = True
            else:
                previo = atual
                atual = atual.pegaProximo()
        if previo == None:
            self.inicio = atual.pegaProximo()
        elif atual != None:
            previo.insereProximo(atual.pegaProximo())
        return encontrou


lista01 = ListaNOrd()
lista01.Inserir(10)
lista01.Inserir(20)
lista01.Inserir(30)
lista01.Show()
lista01.Inserir(15)
lista01.Inserir(25)
lista01.Show()
lista01.Excluir(20)
lista01.Excluir(30)
lista01.Show()
