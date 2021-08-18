class Deque:
    def __init__(self):
        self.items = []

    def pushRigth(self, item): #insere elemento a direita
        self.items.append(item) #[a, b, c, d] ->

    def pushLeft(self, item): #insere elemento a esquerda
        self.items.insert(0,item) #<-
    #['a', 'b', 'c', 'd']
    #pushLeft('z')
    #['z', 'a', 'b', 'c', 'd']

    def popRight(self):
        return self.items.pop()
    # ['a', 'b', 'c', 'd']
    # popRight()
    # ['a', 'b', 'c']

    def popLeft(self):
        return self.items.pop(0)
    # ['a', 'b', 'c', 'd']
    # popLeft()
    # ['b', 'c', 'd']

    def peekRight(self): #Retorna o elemento da direita
        return self.items[len(self.items) - 1]
    # ['a', 'b', 'c', 'd']
    #peekRight()
    #'d'

    def peekLeft(self):
        return self.items[0]
    # ['a', 'b', 'c', 'd']
    # peekLeft()
    # 'a'

    def show(self):
        return self.items

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []