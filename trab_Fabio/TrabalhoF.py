from bubble_sort import *
from insertion_sort import *
from selection_sort import *
from quick_sort import *
from merge_sort import *

n = 1
while n != 9:
    print("\n" * 130)
    print('*** Menu Principal ***')
    print('\n1) Criar Arquivo ')
    print('2) Mostrar Arquivo')
    print('3) Bubble Sort ')
    print('4) Insertion Sort ')
    print('5) Selection Sort ')
    print('6) Quick Sort ')
    print('7) Merge Sort ')
    print('9) Finalizar Programa ')
    n = (int(input('\nEscolha a opção Desejada: ')))
    print("\n" * 130)

    if n == 1:
        print('*** Menu Criação Arquivo ***\n')
        nome_arq = (input('Nome do Arquivo: '))
        nome_arq = nome_arq + '.txt'
        arquivo = open(nome_arq, "a")
        frases = list()
        x = 0
        while x != 9:
            print("\n" * 130)
            print('*** Menu Adicionar Valor ***\n')
            num = (input('Adicionar Valor ao Arquivo: '))
            frases.append(num)
            frases.append('\n')
            print("\n" * 130)
            x = int(input('\n\n0)Para Adicionar Mais valores\n9)Para Voltar\nEscolha:  '))

        arquivo.writelines(frases)
        arquivo.close()

    elif n == 2:
        print('*** Mostar Arquivo ***\n')
        try:
            nome_arq = input('Nome do arquivo a ser Mostrado: ')
            nome_arq = nome_arq + '.txt'
            arquivo = open(nome_arq, 'r')
            x1 = 0
            while x1 != 9:
                print('Arquivo: ', nome_arq, ' é composto por: ')
                arquivo = open(nome_arq, 'r')
                lista = arquivo.readlines()
                for index in range(len(lista)):
                    lista[index] = lista[index].rstrip('\n')
                    lista[index] = int(lista[index])
                print(lista)
                x1 = int(input('\n\n Aperte 9 Para Voltar: '))

        except FileNotFoundError:
            print('Arquivo não Foi encontrado ')
            print('Erros Provaveis: Nome errado ')
            n = int(input('\n\n Aperte 0 Para Voltar: '))

    elif n == 3:
        print("\n" * 130)
        print('*** Bubble Sort ***\n')
        try:
            nome_arq = input('Nome do arquivo a ser Aplicado Bubble Sort: ')
            nome_arq = nome_arq + '.txt'
            arquivo = open(nome_arq, 'r')
            lista = arquivo.readlines()
            x2 = 0
            while x2 != 9:
                for index in range(len(lista)):
                    lista[index] = lista[index].rstrip('\n')
                    lista[index] = int(lista[index])
                bubble_sort(lista)
                n_lista = lista
                print('*** Aplicado o Bubble Sort ***\n')
                print(lista)
                arquivo = open(nome_arq, "w")
                frases = list()
                for i in range(len(n_lista)):
                    frases.append(str(n_lista[i]))
                    frases.append('\n')
                arquivo.writelines(frases)
                arquivo.close()
                x2 = int(input('\n\n Aperte 9 Para Voltar: '))

        except FileNotFoundError:
            print('Arquivo não Foi encontrado ')
            print('Erros Provaveis: Nome errado ')
            n = int(input('\n\n Aperte 0 Para Voltar: '))

    elif n == 4:
        print("\n" * 130)
        print('*** Insertion Sort ***\n')
        try:
            nome_arq = input('Nome do arquivo a ser Aplicado Insertion Sort: ')
            nome_arq = nome_arq + '.txt'
            arquivo = open(nome_arq, 'r')
            lista = arquivo.readlines()
            x3 = 0
            while x3 != 9:
                for index in range(len(lista)):
                    lista[index] = lista[index].rstrip('\n')
                    lista[index] = int(lista[index])
                insertion_sort(lista)
                n_lista = lista
                print('*** Aplicado o Insertion Sort ***\n')
                print(lista)
                arquivo = open(nome_arq, "w")
                frases = list()
                for i in range(len(n_lista)):
                    frases.append(str(n_lista[i]))
                    frases.append('\n')
                arquivo.writelines(frases)
                arquivo.close()
                x3 = int(input('\n\n Aperte 9 Para Voltar: '))

        except FileNotFoundError:
            print('Arquivo não Foi encontrado ')
            print('Erros Provaveis: Nome errado')
            n = int(input('\n\n Aperte 0 Para Voltar: '))

    elif n == 5:
        print("\n" * 130)
        print('*** Selection Sort ***\n')
        try:
            nome_arq = input('Nome do arquivo a ser Aplicado Selection Sort: ')
            nome_arq = nome_arq + '.txt'
            arquivo = open(nome_arq, 'r')
            lista = arquivo.readlines()
            x4 = 0
            while x4 != 9:
                for index in range(len(lista)):
                    lista[index] = lista[index].rstrip('\n')
                    lista[index] = int(lista[index])
                selection_sort(lista)
                n_lista = lista
                print('*** Aplicado o Selection Sort ***\n')
                print(lista)
                arquivo = open(nome_arq, "w")
                frases = list()
                for i in range(len(n_lista)):
                    frases.append(str(n_lista[i]))
                    frases.append('\n')
                arquivo.writelines(frases)
                arquivo.close()
                x4 = int(input('\n\n Aperte 9 Para Voltar: '))

        except FileNotFoundError:
            print('Arquivo não Foi encontrado ')
            print('Erros Provaveis: Nome errado')
            n = int(input('\n\n Aperte 0 Para Voltar: '))

    elif n == 6:
        print("\n" * 130)
        print('*** Quick Sort ***\n')
        try:
            nome_arq = input('Nome do arquivo a ser Aplicado Quick Sort: ')
            nome_arq = nome_arq + '.txt'
            arquivo = open(nome_arq, 'r')
            lista = arquivo.readlines()
            x5 = 0
            while x5 != 9:
                for index in range(len(lista)):
                    lista[index] = lista[index].rstrip('\n')
                    lista[index] = int(lista[index])
                quick_sort(lista, 0, len(lista) - 1)
                n_lista = lista
                print('*** Aplicado o Quick Sort ***\n')
                print(lista)
                arquivo = open(nome_arq, "w")
                frases = list()
                for i in range(len(n_lista)):
                    frases.append(str(n_lista[i]))
                    frases.append('\n')
                arquivo.writelines(frases)
                arquivo.close()
                x5 = int(input('\n\n Aperte 9 Para Voltar: '))

        except FileNotFoundError:
            print('Arquivo não Foi encontrado ')
            print('Erros Provaveis: Nome errado')
            n = int(input('\n\n Aperte 0 Para Voltar: '))

    elif n == 7:
        print("\n" * 130)
        print('*** Merge Sort ***\n')
        try:
            nome_arq = input('Nome do arquivo a ser Aplicado Merge Sort: ')
            nome_arq = nome_arq + '.txt'
            arquivo = open(nome_arq, 'r')
            lista = arquivo.readlines()
            x6 = 0
            while x6 != 9:
                for index in range(len(lista)):
                    lista[index] = lista[index].rstrip('\n')
                    lista[index] = int(lista[index])
                mergeSort(lista)
                n_lista = lista
                print('*** Aplicado o Merge Sort ***\n')
                print(lista)
                arquivo = open(nome_arq, "w")
                frases = list()
                for i in range(len(n_lista)):
                    frases.append(str(n_lista[i]))
                    frases.append('\n')
                arquivo.writelines(frases)
                arquivo.close()
                x6 = int(input('\n\n Aperte 9 Para Voltar: '))

        except FileNotFoundError:
            print('Arquivo não Foi encontrado ')
            print('Erros Provaveis: Nome errado')
            n = int(input('\n\n Aperte 0 Para Voltar: '))
