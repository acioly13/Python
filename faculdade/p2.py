entrada = [5,7,9,8,6,1,4,2,3,6,8,9,9,9,8,7,0,2,1,5,6,7,82,3,4,5,6,7,8,9,0,8,9,7,4,5,6,1,2,3,4,7,8,9,5,4,1,1,1,2,0,0,0,2,3,6]
refer = [0,1,2,3,4,5,6,7,8,9]
saida = []

for c in refer:
    for i in entrada:
        if c == i:
            saida.append(i)

print('Saida: ',saida)
print(refer)
print(entrada)
print('Aluno: João Pedro Fernandes Acioly  Matricula: 201921070')