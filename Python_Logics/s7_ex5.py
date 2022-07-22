# Receber nome e senha e verificar se são iguais
nome = input("Digite seu nome: ")
senha = input("Digite sua senha: ")
while nome == senha:
    print("Nome e senha devem ser diferentes")
    nome = input("Digite seu nome: ")
    senha = input("Digite sua senha: ")