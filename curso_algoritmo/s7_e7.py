id_mouse = int(input('Digite o id do mouse: '))
quantidade = 0
necessita_esfera = 0
necessita_limpeza = 0
necessita_cabo = 0
quebrado = 0
while id_mouse != 0:
    print('\n-- Identifique o Defeito --')
    print('1) Necessita da Esfera ')
    print('2) Necessita de Limpeza ')
    print('3) Necessita do Cabo ')
    print('4) Quebrado ')
    defeito = int(input('Digite o Defeito: '))
    if defeito == 1:
        necessita_esfera = necessita_esfera + 1
    if defeito == 2:
        necessita_limpeza = necessita_limpeza + 1
    if defeito == 3:
        necessita_cabo = necessita_cabo + 1
    if defeito == 4:
        quebrado = quebrado + 1
    quantidade = quantidade + 1
    id_mouse = int(input('\nDigite o id do mouse: '))

perc_esfera = necessita_esfera / quantidade * 100.0
perc_limpeza = necessita_limpeza / quantidade * 100.0
perc_cabo = necessita_cabo / quantidade * 100.0
perc_quebrado = quebrado / quantidade * 100.0

print(f'\n\n\nTotal de mouses: {quantidade}')
print('Situação                       Quantidade          Percentual')
print('1)Necessita da Esfera             {0}                 {1:.2f}%'.format(necessita_esfera, perc_esfera))
print('2)Necessita de Limpeza            {0}                 {1:.2f}%'.format(necessita_limpeza, perc_limpeza))
print('3)Necessita do Cabo               {0}                 {1:.2f}%'.format(necessita_cabo, perc_cabo))
print('4)Quebrado                        {0}                 {1:.2f}%'.format(quebrado, perc_quebrado))

