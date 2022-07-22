# Receber 4 valores, quadrado de cada um, se o quadrado do terceiro >= 1000, imprimao e finalize, senao imprima os quadrados
# Entradas
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
n4 = int(input("Digite um valor: "))
# Processamento
q1 = n1 * n1
q2 = n2 * n2
q3 = n3 * n3
q4 = n4 * n4
if q3 >= 1000:
    # Saida
    print(f"Quadrado de {n3}: {q3}")
else:
    # Saida
    print(f"Quadrado de {n1}: {q1}")
    print(f"Quadrado de {n2}: {q2}")
    print(f"Quadrado de {n3}: {q3}")
    print(f"Quadrado de {n4}: {q4}")