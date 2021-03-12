global fila, spos, rpos, MAX


def __init__(maximo):
    global fila, spos, rpos, MAX
    MAX = maximo
    fila = []
    for i in range(0, MAX):
        fila.append(None)
    spos = 0
    rpos = 0


def push(valor):
    global fila, spos
    if (rpos == spos and fila[rpos] != None) or (spos+1 == MAX and rpos == 0):
        print(' FILA CHEIA ')
        return
    if spos+1 == MAX and rpos != 0:
        spos = 0
    fila[spos] = valor
    spos = spos + 1
    return


def pop():
    global fila, rpos
    if rpos == spos and fila[rpos] == None:
        print(' FILA VAZIA ')
        return
    if rpos + 1 == MAX:
        rpos = 0
    valor = fila[rpos]
    fila[rpos] = None
    rpos = rpos + 1
    return valor


def show():
    for i in range(0, MAX-1):
        print(fila[i])
    return None


def showp():
    print('Rpos: ', rpos, '   Spos: ', spos, '   MAX: ', MAX, '\n')
    return


push(10)
show()
showp()
input()
push(20)
show()
showp()
push(30)
push(40)
push(50)
show()
showp()
input()
push(60)
input()
pop()
show()
showp()