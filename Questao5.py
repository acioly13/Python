# João Pedro Fernandes Acioly - 201921070 - Maricá - 4 Periodo
# Entrada de dados
usuario_altura = float(input('Digite sua altura(metros): '))
usuario_sombra = float(input('Digite o tamanho da sua sombra(metros): '))
sombra_predio = float(input('Digite o tamaho da sombra do predio(metros): '))

# Processamento de dados
altura_predio = (sombra_predio * usuario_altura) / usuario_sombra

# Saida de dados
print(f'Altura do Predio: {altura_predio} metros')
