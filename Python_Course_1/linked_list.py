class Node:

    def __init__(self, label):
        self.label = label
        self.next = None

    def get_label(self):
        return self.label

    def set_label(self, label):
        self.label = label

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class LinkedList:

    def __init__(self):
        self.first = None
        self.last = None
        self.len_list = 0

    def push(self, label, index):

        if index >= 0:

            # cria o novo nó
            node = Node(label)

            # verifica se a lista está vazia
            if self.empty():
                self.first = node
                self.last = node
            else:

                if index == 0:
                    # inserção no início
                    node.set_next(self.first)
                    self.first = node
                elif index >= self.len_list:
                    # inserção ao final
                    self.last.set_next(node)
                    self.last = node
                else:
                    # inserção no meio
                    prev_node = self.first
                    curr_node = self.first.get_next()
                    curr_index = 1

                    while curr_node is not None:

                        if curr_index == index:
                            # seta o curr_node como o próximo do nó
                            node.set_next(curr_node)
                            # seta o node como o próximo do prev_nodes
                            prev_node.set_next(node)

                        prev_node = curr_node
                        curr_node = curr_node.get_next()
                        curr_index += 1

            # atualiza o tamanho da lista
            self.len_list += 1

    def pop(self, index):

        if not self.empty() and 0 <= index < self.len_list:

            flag_remove = False

            if self.first.get_next() is None:
                # possui apenas 1 elemento
                self.first = None
                self.last = None
                flag_remove = True
            elif index == 0:
                # remove do início, mas possui mais de 1 elemento
                self.first = self.first.get_next()
                flag_remove = True
            else:
                '''
                    Se chegou aqui é porque a lista possui mais
                    de 1 elemento e a remoção não é no início
                '''

                prev_node = self.first
                curr_node = self.first.get_next()
                curr_index = 1

                while curr_node is not None:

                    if index == curr_index:
                        # o próximo do anterior aponta para o próximo do nó corrente
                        prev_node.set_next(curr_node.get_next())
                        curr_node.set_next(None)
                        flag_remove = True
                        break

                    prev_node = curr_node
                    curr_node = curr_node.get_next()
                    curr_index += 1

            if flag_remove:
                # atualiza o tamanho da lista
                self.len_list -= 1

    def empty(self):
        if self.first is None:
            return True
        return False

    def length(self):
        return self.len_list

    def show(self):

        curr_node = self.first

        while curr_node is not None:
            print(curr_node.get_label(), end=' ')
            curr_node = curr_node.get_next()
        print('')


lista = LinkedList()

# teste inserção
lista.push('Marcos', 0)  # inserção no início
lista.show()
lista.push('Maria', 1)  # inserção no final
lista.show()
lista.push('Yankee', 0)  # inserção no início
lista.show()
lista.push('Catarina', 2)  # inserção no meio
lista.show()
lista.push('Lilica', 4)  # inserção no final
lista.show()
lista.push('Sara', 2)  # inserção no meio
lista.show()
print('Tamanho da lista: %d\n' % lista.length())

# teste remoção
lista.pop(0)  # remoção do início
lista.show()
lista.pop(2)  # remoção do meio
lista.show()
lista.pop(3)  # remoção do final
lista.show()
print('Tamanho da lista: %d\n' % lista.length())
