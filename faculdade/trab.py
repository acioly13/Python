n = 1
while n != 9:
    print('*** Estrutura de Dados ***')
    print('1)Lista Não Ordenada ')
    print('2)Pilha ')
    print('3)Fila ')
    print('4)Fila Circular ')
    print('5)Lista Ordenada ')
    print('9)Sair ')
    n = (int(input('\nEscolha a opção Desejada: ')))
    print("\n" * 130)

    if n == 1:
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

        x = 0
        while x != 9:
            print('*** Menu Lista Não Ordenada ***')
            print('0)Iniciar/Limpar')
            print('1)Armazenar Valor ')
            print('2)Excluir Valor ')
            print('3)Buscar Valor ')
            print('4)Mostar Lista ')
            print('5)Descrição ')
            print('9)Sair ')
            x = (int(input('\nEscolha: ')))
            print("\n" * 130)

            if x == 0:
                lista01 = ListaNOrd()

            elif x == 1:
                num = int(input('Digite o Valor a ser adicionado: '))
                lista01.Inserir(num)
                print("\n" * 130)

            elif x == 2:
                num = int(input('Digite o Valor a ser excluido: '))
                lista01.Excluir(num)
                print("\n" * 130)

            elif x == 3:
                z0 = 1
                while z0 == 1:
                    num = int(input('Digite o Valor a ser Buscado: '))
                    lista01.Buscar(num)
                    print("\n" * 130)
                    if lista01.Buscar(num):
                        print('O valor ', num, ' se encontra na lista')
                        print(' ')
                        z0 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)
                    else:
                        print('O valor ', num, ' não se encontra na lista')
                        print(' ')
                        z0 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)

            elif x == 4:
                z = 1
                while z == 1:
                    print("\n" * 130)
                    print('*** Lista Atualmente ***\n')
                    lista01.Show()
                    print(' ')
                    z = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

            elif x == 5:
                z = 1
                while z == 1:
                    print("\n" * 130)
                    print('*** Descrição Lista Não Ordenada ***\n')
                    print('Na lista Não ordenada os valores ficam na ordem em que são colocados, '
                          'não tendo prioridade para exclusão')
                    print(' ')
                    z = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

    elif n == 2:
        global pilha, ponteiro


        def inicializa():
            global pilha, ponteiro
            pilha = []
            ponteiro = -1
            return


        def push(valor):
            global pilha, ponteiro
            pilha.append(valor)
            ponteiro += 1
            return


        def pop():
            global pilha, ponteiro
            if ponteiro < 0:
                print('\n Pilha vazia ')
                return
            else:
                valor = pilha[ponteiro]
                del (pilha[ponteiro])
                ponteiro -= 1
                return valor


        def show():
            global pilha
            print(pilha)


        x0 = 0
        while x0 != 9:
            print('*** Menu Pilha ***')
            print('0)Iniciar/Limpar')
            print('1)Armazenar Valor ')
            print('2)Remover Valor ')
            print('3)Mostar Pilha ')
            print('4)Descrição ')
            print('9)Sair ')
            x0 = (int(input('\nEscolha: ')))
            print("\n" * 130)

            if x0 == 0:
                inicializa()

            elif x0 == 1:
                num = int(input('Digite o Valor a ser adicionado: '))
                push(num)
                print("\n" * 130)

            elif x0 == 2:
                z1 = 1
                while z1 != 0:
                    if ponteiro < 0:
                        print('\nPilha ja esta vazia!! ')
                        print(' ')
                        z1 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)

                    else:
                        print('Voce escolheu retirar o valor ', pilha[ponteiro])
                        pop()
                        print(' ')
                        print('*** Pilha Atualmente ***\n')
                        show()
                        print(' ')
                        z1 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)

            elif x0 == 3:
                z2 = 1
                while z2 == 1:
                    print("\n" * 130)
                    print('*** Pilha Atualmente ***\n')
                    show()
                    print(' ')
                    z2 = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

            elif x0 == 4:
                z3 = 1
                while z3 == 1:
                    print("\n" * 130)
                    print('*** Descrição Pilha ***\n')
                    print('Na pilha os valores formam uma pilha, o primeiro a ser colocado é o ultimo a sair.')
                    print(' ')
                    z3 = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

    elif n == 3:
        global fila, spos, rpos, MAX

        MAX = 5
        fila = []
        spos = 0
        rpos = 0


        def push(valor):
            global spos, rpos, fila

            if spos == MAX:
                print('\n Fila Cheia')
                return
            fila.append(valor)
            spos += 1
            return


        def pop():
            global spos, rpos, fila

            if rpos == spos:
                print('\n Fila Vazia')
                return None
            rpos += 1
            return fila[rpos - 1]


        def show():
            global spos, rpos, fila

            if rpos == spos:
                print('\nFila Vazia')
                return
            for i in range(rpos, spos):
                print(fila[i], end=' ')

            return


        def showp():
            global spos, rpos, fila
            print('rpos= ', rpos, '  spos= ', spos)
            return


        x1 = 0
        while x1 != 9:
            print('*** Menu Fila ***')
            print('0)Iniciar/Limpar')
            print('1)Armazenar Valor ')
            print('2)Remover Valor ')
            print('3)Mostar Fila ')
            print('4)Descrição ')
            print('9)Sair ')
            x1 = (int(input('\nEscolha: ')))
            print("\n" * 130)

            if x1 == 0:
                MAX = int(input('Escolha o tamanho da Fila: '))

            elif x1 == 1:
                num = int(input('Digite o Valor a ser adicionado: '))
                push(num)
                print("\n" * 130)

            elif x1 == 2:
                z2 = 1
                while z2 != 0:
                    if rpos == spos:
                        print('\nFila ja esta vazia!! ')
                        print(' ')
                        z2 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)
                    else:
                        print('Voce escolheu retirar o valor ', fila[0])
                        pop()
                        print(' ')
                        print('*** Fila Atualmente ***\n')
                        show()
                        print(' ')
                        z2 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)

            elif x1 == 3:
                z2 = 1
                while z2 == 1:
                    print("\n" * 130)
                    print('*** Fila Atualmente ***\n')
                    show()
                    print(' ')
                    z2 = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

            elif x1 == 4:
                z3 = 1
                while z3 == 1:
                    print("\n" * 130)
                    print('*** Descrição Fila ***\n')
                    print('Na Fila os valores formam uma fila, o primeiro a ser colocado é o primeiro a sair,'
                          'ela tendo um limite para ficar cheia.')
                    print(' ')
                    z3 = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

    elif n == 4:
        global filac, sposc, rposc, MAXc


        def init(maximo):
            global filac, sposc, rposc, MAXc
            MAXc = maximo
            filac = []
            for i in range(0, MAXc):
                filac.append(None)
            sposc = 0
            rposc = 0


        def push(valor):
            global filac, sposc
            if (rposc == sposc and filac[rposc] != None) or (sposc + 1 == MAXc and rposc == 0):
                print(' FILA CHEIA ')
                return
            if sposc + 1 == MAXc and rposc != 0:
                sposc = 0
            filac[sposc] = valor
            sposc = sposc + 1
            return


        def pop():
            global filac, rposc
            if rposc == sposc and filac[rposc] == None:
                print(' FILA VAZIA ')
                return
            if rposc + 1 == MAXc:
                rposc = 0
            valor = filac[rposc]
            filac[rposc] = None
            rposc = rposc + 1
            return valor


        def show():
            for i in range(0, MAXc - 1):
                print(filac[i])
            return None


        def showp():
            print('Rpos: ', rposc, '   Spos: ', sposc, '   MAX: ', MAXc, '\n')
            return


        x1 = 0
        while x1 != 9:
            print('*** Menu Fila Circular ***')
            print('0)Iniciar/Limpar')
            print('1)Armazenar Valor ')
            print('2)Remover Valor ')
            print('3)Mostar Fila Circular ')
            print('4)Descrição ')
            print('9)Sair ')
            x1 = (int(input('\nEscolha: ')))
            print("\n" * 130)

            if x1 == 0:
                init(int(input('Escolha o tamanho da Fila Circular: ')))

            elif x1 == 1:
                num = int(input('Digite o Valor a ser adicionado: '))
                push(num)
                print("\n" * 130)

            elif x1 == 2:
                z2 = 1
                while z2 != 0:
                    if rposc == sposc:
                        print('\nFila Circular ja esta vazia!! ')
                        print(' ')
                        z2 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)
                    else:
                        print('Voce escolheu retirar o valor ', filac[0])
                        pop()
                        print(' ')
                        print('*** Fila Atualmente ***\n')
                        show()
                        print(' ')
                        z2 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)

            elif x1 == 3:
                z2 = 1
                while z2 == 1:
                    print("\n" * 130)
                    print('*** Fila Circular Atualmente ***\n')
                    show()
                    print(' ')
                    z2 = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

            elif x1 == 4:
                z3 = 1
                while z3 == 1:
                    print("\n" * 130)
                    print('*** Descrição Fila Circular ***\n')
                    print(
                        'Na Fila Circular os valores formam de fato uma fila sendo que os valores circulam dentro dela')
                    print(' ')
                    z3 = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

    elif n == 5:
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


        x = 0
        while x != 9:
            print('*** Menu Lista Ordenada ***')
            print('0)Iniciar/Limpar')
            print('1)Armazenar Valor ')
            print('2)Excluir Valor ')
            print('3)Buscar Valor ')
            print('4)Mostar Lista ')
            print('5)Descrição ')
            print('9)Sair ')
            x = (int(input('\nEscolha: ')))
            print("\n" * 130)

            if x == 0:
                lista0 = ListaOrd()

            elif x == 1:
                num = int(input('Digite o Valor a ser adicionado: '))
                lista0.Inserir(num)
                print("\n" * 130)

            elif x == 2:
                num = int(input('Digite o Valor a ser excluido: '))
                lista0.Excluir(num)
                print("\n" * 130)

            elif x == 3:
                z0 = 1
                while z0 == 1:
                    num = int(input('Digite o Valor a ser Buscado: '))
                    lista0.Buscar(num)
                    print("\n" * 130)
                    if lista0.Buscar(num):
                        print('O valor ', num, ' se encontra na lista')
                        print(' ')
                        z0 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)
                    else:
                        print('O valor ', num, ' não se encontra na lista')
                        print(' ')
                        z0 = int(input('Digite 0 Para Voltar: '))
                        print("\n" * 130)

            elif x == 4:
                z = 1
                while z == 1:
                    print("\n" * 130)
                    print('*** Lista Atualmente ***\n')
                    lista0.Show()
                    print(' ')
                    z = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

            elif x == 5:
                z = 1
                while z == 1:
                    print("\n" * 130)
                    print('*** Descrição Lista Ordenada ***\n')
                    print(
                        'Na lista ordenada os valores entram em ordem sutomaticamente')
                    print(' ')
                    z = int(input('Digite 0 Para Voltar: '))
                    print("\n" * 130)

    else:
        pass
