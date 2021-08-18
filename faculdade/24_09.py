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
    return fila[rpos-1]


def show():
    global spos, rpos, fila

    if rpos == spos:
        print('\nFila Vazia')
        return
    for i in range(rpos, spos):
        print(fila[i])

    return


def showp():
    global spos, rpos, fila
    print('rpos= ', rpos, '  spos= ', spos)
    return


push(10)
push(20)
push(30)
show()
pop()
show()
