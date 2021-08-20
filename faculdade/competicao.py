corrida = {}
dardos = {}
z = 0
escolha = int(input('Qual competição quer criar Dardos(1) ou Corrida(2): '))

if escolha == 1:
    distancia = []
    print('--- Competição Dardos ---')
    while z == 0:
        competidor = input('Digite o competidor: ')
        n = 0
        while n < 3:
            distancia_dardo = float(input('Digite a distancia do dardo: '))
            distancia.append(distancia_dardo)
            n += 1
        melhor_dardo = max(distancia, key=float)
        dardos.update({competidor: melhor_dardo})
        z = int(input('Adicionar mais competidores(0)  Voltar(1): '))
elif escolha == 2:
    print('--- Competição Corrida ---')
    while z == 0:
        competidor = input('Digite o competidor: ')
        tempo = float(input('Digite o tempo em segundos: '))
        corrida.update({competidor: tempo})
        z = int(input('Adicionar mais competidores(0)  Voltar(1): '))

print(corrida)
for competidor, tempo in corrida.items():
    print(competidor + ': ' + str(tempo))
