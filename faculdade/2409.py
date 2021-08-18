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
        del(pilha[ponteiro])
        ponteiro -= 1
        return valor


def show():
    global pilha
    print(pilha)


inicializa()
push(10)
push(20)
push(30)
push(40)
show()
print(pop())
show()
print(pop())
show()
print(pop())
print(pop())
pop()
