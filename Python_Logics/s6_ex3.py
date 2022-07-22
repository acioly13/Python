# Receber valor, se for impar armazenar em i, se for par armazenar em p
# Entrada
num = int(input("Digite um número: "))
p = 0
i = 0
# Processamento
if num % 2 == 0:
    p = num
else:
    i = num
# Saída
print(p)
print(i)