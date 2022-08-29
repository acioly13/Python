class HashTable:

    def __init__(self,table_size):

        if table_size < 1:
            raise ValueError("Tabela deve ter pelo menos 1 elemento")
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)]

    def hash_function(self, key):
        return key % self.table_size

    def insert(self, key):
        self.table[self.hash_function(key)].append(key)

    def show(self):
        for linked_list in self.table:
            if linked_list:
                for key in linked_list:
                    print('%d' % key, end=' ')
                print(' ')

    def search(self, key):
        if key in self.table[self.hash_function(key)]:
            return True
        return False


d = HashTable(9)
d.insert(19)
d.insert(28)
d.insert(20)
d.insert(5)
d.insert(33)
d.insert(15)

d.show()