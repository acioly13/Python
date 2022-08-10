class Pilha:

    def __init__(self):
        self.pilha = []

    def push(self, e):
        self.pilha.append(e)

    def pop(self):
        if not self.empty():
            self.pilha.pop(len(self.pilha) - 1)

    def top(self):
        if not self.empty():
            return self.pilha[-1]
        else:
            return None

    def empty(self):
        if len(self.pilha) == 0:
            return True
        else:
            return False

    def length(self):
        return len(self.pilha)


s = Pilha()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
s.pop()
print(s.top())
s.pop()
print(s.length())
