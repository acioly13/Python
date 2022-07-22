# Entradas
nivel_poluicao = float(input("Digite o nivel de poluição: "))
# Processamento
if (nivel_poluicao >= 0.3) and (nivel_poluicao < 0.4):
    print(" Grupo 1 suspender atividades")
elif (nivel_poluicao >= 0.4) and (nivel_poluicao < 0.5):
    print(" Grupo 1 e 2 suspender atividades")
elif nivel_poluicao >= 0.5:
    print(" Todos Suspender atividades")
else:
    print("Niveis aceitaveis")

