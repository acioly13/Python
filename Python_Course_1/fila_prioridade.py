# Implementação de Fila com prioridade com lista ordenada
class Pessoa:
    """
    nome = nome da pessoa
    prioridade = prioridade da pessoa
    """

    def __init__(self, nome, prioridade):
        self.nome = nome
        self.prioridade = prioridade

    def get_nome(self):
        return self.nome

    def get_prioridade(self):
        return self.prioridade


class FilaPrioridade:
    """
    fila = lista de pessoas
    """

    def __init__(self):
        self.fila = []  # fila de prioridade
        self.len = 0  # tamanho da fila

    def inserir(self, pessoa):
        """
        Insere uma pessoa na fila de acordo com a prioridade
        """
        if self.empty():
            self.fila.append(pessoa)
        else:
            flagpush = False
            for i in range(self.len):
                if self.fila[i].get_prioridade() < pessoa.get_prioridade():
                    self.fila.insert(i, pessoa)
                    flagpush = True
                    break
            if not flagpush:
                # se não encontrou nenhuma pessoa com prioridade menor, insere no final
                self.fila.insert(self.len, pessoa)

        self.len += 1

    def remover(self):
        """
        Remove a primeira pessoa da fila
        """
        if not self.empty():
            self.fila.pop(0)
            self.len -= 1

    def empty(self):
        """
        Verifica se a fila está vazia
        """
        if self.len == 0:
            return True
        else:
            return False

    def show(self):
        """
        Mostra a fila de prioridade
        """
        for p in self.fila:
            print(f'Nome: {p.get_nome()}')
            print(f'Prioridade: {p.get_prioridade()}\n')


# Criando os objetos pessoa
p1 = Pessoa('Marcos', 28)
p2 = Pessoa('Catarina', 3)
p3 = Pessoa('Pedro', 20)
p4 = Pessoa('João', 35)

# Criando a fila de prioridade
fila = FilaPrioridade()
fila.inserir(p1)
fila.inserir(p2)
fila.inserir(p3)
fila.inserir(p4)

# Mostrando a fila de prioridade
fila.show()

# Removendo a primeira pessoa da fila
fila.remover()
fila.remover()
print('Removendo elementos')
fila.show()

# Inserindo novo elemento na fila
fila.inserir(Pessoa('Goku', 30))
print('Inserindo novo elemento')
fila.show()


