# Manipulando arquivos

# Abrindo um arquivo
arquivo = open('arquivo.txt', 'w')

# Mensagem a ser escrita no arquivo
msg = """
Manipulando arquivos em Python
Aprendendo a manipular arquivos em Python
aaa
    """

# Escrevendo no arquivo
arquivo.write(msg)

# Fechando o arquivo
arquivo.close()

# Abrindo o arquivo para leitura
arquivo = open('arquivo.txt', 'r')

# Lendo o arquivo
print(''.join(linha for linha in arquivo.readlines()))

# Fechando o arquivo
arquivo.close()
