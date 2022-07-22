# Gerador tabuada
# numero = int(input("Digite um número: "))
# while numero > 10 or numero < 1:
#     print("Número inválido")
#     numero = int(input("Digite um número: "))
# for i in range(1, 11):
#     print(f"{numero} x {i} = {numero * i}")

lista_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input("Digite um número: "))
if numero not in lista_num:
    print("Número inválido")
    numero = int(input("Digite um número: "))
for i in lista_num:
    print(f"{numero} x {i} = {numero * i}")
