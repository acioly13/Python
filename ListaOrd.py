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


class ListaOrd:
    def __init__(self):
        self.inicio = None

    def Vazia(self):
        return self.inicio == None

    def Inserir(self, valor):
        atual = self.inicio
        previo = None
        encontrou = False

        while atual != None and encontrou == False:
            if atual.pegaValor() > valor:
                encontrou = True
            else:
                previo = atual
                atual = atual.pegaProximo()

        temp = No(valor)
        if previo == None:
            temp.insereProximo(self.inicio)
            self.inicio = temp
        else:
            temp.insereProximo(atual)
            previo.insereProximo(temp)
        return

    def Buscar(self, valor):
        atual = self.inicio
        encontrou = False

        while atual != None and encontrou == False:
            if atual.pegaValor() == valor:
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


list01 = ListaOrd()
list01.Inserir(10)
list01.Inserir(20)
list01.Inserir(30)
list01.Show()
print('\n\n')
list01.Inserir(25)
list01.Show()
print('\n\n')
list01.Excluir(20)
list01.Show()
list01.Inserir(15)
list01.Show()