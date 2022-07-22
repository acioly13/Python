from random import *
# levantamento dos mouses
# Declaração de variáveis
quantidade_mouses = 0
necessita_esfera = 0
necessita_limpeza = 0
necessita_cabo = 0
quebrado = 0
# Entrada de dados
identificacao = int(input("Digite o id do mouse: "))
while identificacao != 0:
    print("Identifique o defeito: ")
    print("1 - Esfera")
    print("2 - Limpeza")
    print("3 - Cabo")
    print("4 - Quebrado")
    defeito = randint(1, 4)
    if defeito == 1:
        necessita_esfera += 1
    elif defeito == 2:
        necessita_limpeza += 1
    elif defeito == 3:
        necessita_cabo += 1
    elif defeito == 4:
        quebrado += 1
    quantidade_mouses += 1
    identificacao = int(input("Digite o id do mouse: "))
p1 = necessita_esfera / quantidade_mouses * 100
p2 = necessita_limpeza / quantidade_mouses * 100
p3 = necessita_cabo / quantidade_mouses * 100
p4 = quebrado / quantidade_mouses * 100
print("Situação           Quantidade   Percentual")
print(f"1)Troca de Esfera       {necessita_esfera}        {p1:.2f}%")
print(f"2)Necessita Limpeza     {necessita_limpeza}        {p2:.2f}%")
print(f"3)Troca de Cabo         {necessita_cabo}        {p3:.2f}%")
print(f"4)Quebrado              {quebrado}        {p4:.2f}%")