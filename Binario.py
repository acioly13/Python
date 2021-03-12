n = 1
while n != 0:
    print('*** Menu ***')
    print('1)Binario para Decimal ')
    print('2)Decimal para Binario ')
    print('3)Hexadecimal para Decimal ')
    print('4)Hexadecimal para Binario ')
    print('5)Decimal para Hexadecimal ')
    print('0)Sair ')
    n = (int(input('\nEscolha a opção Desejada: ')))
    print("\n" * 130)

    if n == 1:
        n2 = 1
        while n2 != 0:
            print('*** Binario para Decimal ***')
            bina = int(input('Numero a ser convertido para Decimal: '))
            print("\n" * 130)
            bin2 = bina
            bina = list(str(bina))
            dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            dec = 0
            bina.reverse()
            for x, i in enumerate(bina):
                dec += dic.index(i) * 2 ** x
            dec = str(dec)
            print('Binario: ', bin2, ' Decimal: ', dec)
            n2 = int(input('\nDigite 0 Para Voltar: '))
            print("\n" * 130)

    elif n == 2:
        n2 = 1
        dic = ['0', '1']
        bina = []
        bina2 = ''
        while n2 != 0:
            print('*** Decimal Para Binario ***')
            dec = int(input('Numero a ser convertido para Binario: '))
            dec2 = dec
            print("\n" * 130)
            while True:
                N = dec % 2
                bina.append(N)
                if int(dec / 2) == 0:
                    break
                dec = int(dec / 2)
            bina.reverse()
            for i in bina:
                bina2 += dic[i]
            print('Decimal: ', dec2, 'Binario: ', bina2)
            n2 = int(input('\nDigite 0 Para Voltar: '))
            print("\n" * 130)

    elif n == 3:
        n2 = 1
        while n2 != 0:
            print('*** Hexadecimal para Decimal ***')
            hexx = (input('Numero a ser convertido para Decimal: '))
            print("\n" * 130)
            hex2 = hexx
            hexx = list(str(hexx))
            dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            dec = 0
            hexx.reverse()
            for x, i in enumerate(hexx):
                dec += dic.index(i) * 16 ** x
            dec = str(dec)
            print('Hexadecimal: ', hex2, ' Decimal: ', dec)
            n2 = int(input('\nDigite 0 Para Voltar: '))
            print("\n" * 130)

    elif n == 4:
        n2 = 1
        while n2 != 0:
            print('*** Hexadecimal para Binario ***')
            hexx = (input('Numero a ser convertido para Binario: '))
            dec2 = hexx
            print("\n" * 130)
            hex2 = hexx
            hexx = list(str(hexx))
            dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            dec = 0
            hexx.reverse()
            for x, i in enumerate(hexx):
                dec += dic.index(i) * 16 ** x
            n2 = 1
            dic = ['0', '1']
            bina = []
            bina2 = ''
            while True:
                N = dec % 2
                bina.append(N)
                if int(dec / 2) == 0:
                    break
                dec = int(dec / 2)
            bina.reverse()
            for i in bina:
                bina2 += dic[i]
            print('Hexadecimal: ', dec2, 'Binario: ', bina2)
            n2 = int(input('\nDigite 0 Para Voltar: '))
            print("\n" * 130)

    elif n == 5:
        n2 = 1
        dic = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        hexx = []
        hex2 = ''
        while n2 != 0:
            print('*** Decimal Para Hexadecimal ***')
            dec = int(input('Numero a ser convertido para Hexadecimal: '))
            dec2 = dec
            print("\n" * 130)
            while True:
                N = dec % 16
                hexx.append(N)
                if int(dec / 16) == 0:
                    break
                dec = int(dec / 16)
            hexx.reverse()
            for i in hexx:
                hex2 += dic[i]
            print('Decimal: ', dec2, 'Hexadecimal: ', hex2)
            n2 = int(input('\nDigite 0 Para Voltar: '))
            print("\n" * 130)

    else:
        pass
