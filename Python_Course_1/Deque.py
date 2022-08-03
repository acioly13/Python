class Deque:

    def __init__(self):
        self.len = 0
        self.deque = []

    def empty(self):
        if self.len == 0:
            return True
        else:
            return False

    def push_front(self, value):
        self.deque.insert(0, value)
        self.len += 1

    def push_back(self, value):
        self.deque.insert(self.len, value)
        self.len += 1

    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len -= 1

    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len - 1)
            self.len -= 1

    def front(self):
        if not self.empty():
            return self.deque[0]
        else:
            return None

    def back(self):
        if not self.empty():
            return self.deque[self.len - 1]
        else:
            return None

    def show(self):
        for i in self.deque:
            print(i, end=' ')


d = Deque()
d.push_front(10)  # d = [10]
d.push_front(5)  # d = [5, 10]
d.push_back(20)  # d = [5, 10, 20]
d.push_front(7)  # d = [7, 5, 10, 20]
d.push_back(40)  # d = [7, 5, 10, 20, 40]

d.show()
print(f'\nFront: {d.front()}')
print(f'Back: {d.back()}')


d.pop_back()  # d = [7, 5, 10, 20]
d.pop_front()  # d = [5, 10, 20]
d.show()
