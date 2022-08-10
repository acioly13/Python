class Pilha:

    def __init__(self):
        self.pilha = []
        self.len_pilha = 0

    def push(self, e):
        self.pilha.append(e)
        self.len_pilha += 1

    def pop(self):
        if not self.empty():
            self.pilha.pop(self.len_pilha - 1)
            self.len_pilha -= 1

    def top(self):
        if not self.empty():
            return self.pilha[-1]
        else:
            return None

    def empty(self):
        if self.len_pilha == 0:
            return True
        else:
            return False

    def length(self):
        return self.len_pilha


s = Pilha()
s.push(1)
s.push(2)
s.push(3)
print(s.top())
