#!/usr/bin/env python
# coding: UTF-8
#
## @package ouro.
#   Eis alguns CPF válidos que valem ouro:
#     1. 757.331.783-29
#     2. 841.315.629-79
#     3. 635.111.771-20
#     4. 348.536.715-01
#
#   Para exemplificar o processo de validação, serão
#   calculados os dígitos verificadores de um CPF hipotético, 111.444.777-XX. O dígito verificadores
#   são os dois últimos números do CPF (xx)
#
#   Calculando o Primeiro Dígito Verificador.
#
#   O primeiro dígito verificador do CPF é calculado utilizando-se o seguinte algoritmo:
#
#     1. Distribua os 9 primeiros dígitos em um quadro colocando os pesos 10, 9, 8, 7, 6, 5, 4, 3, 2
#        da esquerda para a direita, conforme indicado abaixo:
#     CPF:    1       1       1       4       4       4       7       7       7
#     Peso:   10      9       8       7       6       5       4       3       2
#   
#     2. Multiplique os valores da primeira linha com a segunda de cada coluna:
#     CPF:         1       1       1       4       4       4       7       7       7
#     Peso:        10      9       8       7       6       5       4       3       2
#     Resultado:   10      9       8       28      24      20      28      21      14
#   
#     3. Calcule o somatório dos resultados (10+9+8+28+24+20+28+21+14) = 162.
#     4. O resultado obtido (162) será divido por 11.
#        O resto da divisão indicará o primeiro dígito verificador: 162 % 11 = 8.
#
#   Se o resto da divisão for menor do que 2, o primeiro dígito verificador se torna zero. <br>
#   Caso contrário, subtraia o valor obtido de 11, para obter o primeiro dígito verificador: 11-8 = 3. <br>
#   Portanto, o CPF até agora está assim: 111.444.777-3X.
#
#   Calculando o Segundo Dígito Verificador
#
#   Para o cálculo do segundo dígito, será usado o primeiro dígito verificador já encontrado:
#
#     1. Monte uma tabela semelhante à anterior, só que desta vez usando na segunda linha os valores 
#     11,10,9,8,7,6,5,4,3,2, já que foi incorporado mais um algarismo ao cálculo. Repare que o primeiro
#     digito verificador (3) está na última posição.
#     CPF:    1       1       1       4       4       4       7       7       7       3
#     Peso:   11      10      9       8       7       6       5       4       3       2
#   
#     2. Multiplique os valores de cada coluna e efetue o somatório dos resultados obtidos: (11+10+...+21+6) = 204.
#   
#     CPF:          1       1       1       4       4       4       7       7       7       3
#     Peso:         11      10      9       8       7       6       5       4       3       2
#     Resultado:    11      10      9       32      28      24      35      28      21      6
#  
#     3. Calcule o somatório e ivida o total do somatório por 11 e considere o resto da divisão: 204 % 11 = 6.
#     4. Se o resto da divisão for menor do que 2, o segundo dígito verificador se torna zero. 
#        Caso contrário, é necessário subtrair o valor obtido de 11, para gerar o segundo dígito verificador: 11-6 = 5.
#
#   Ao final dos cálculos, descobre-se que os dígitos verificadores do CPF hipotético são os números 3 e 5.
#   Portanto, o CPF completo é: 111.444.777-35.
#
#   @author André Saraiva
#   @since 06/07/2022
#   @see http://www.geradorcpf.com/


#
#   Seu trabalho será criar x testes em um arquivo separado:
#   1o. Teste: Entrada com um CPF válido (1,0 pts)
#   2o. Teste: Entrada com um CPF inválido (1,5 pts)
#   3o. Teste: Entrada com um CPF sem pontos (111444777-35), sem traços (111.444.77735),
#              sem pontos e traços (11144477735) (5,0 pts)
#   4o. Teste: Entrada com um número que não seja um CPF (0123456) (1,5 pts)
#   5o. Teste: Verificar a saída CPF Inválido !!! (1,0 pts)
#
#   APROVAÇÃO SE DÁ COM 6,0 OU MAIS PONTOS!!!
#   ANTES DE COMEÇAR, FAÇA A ENTRADA DE TODOS OS TESTES PARA VERIFICAR AS SAÍDAS!!!
#

import sys
from operator import mul
from typing import List


##
#   Valida um CPF usando os dígitos de verificação (DV).
#
# @param cpf CPF.
# @param dv dígitos de verificação.
# @return True se o CPF for válido e False caso contrário.
# @see https://docs.python.org/3/library/operator.html
#
def areValidDigits(cpf: str, dv: int) -> bool:
    cpf2 = list(range(10, 1, -1))
    cpf1 = [11] + cpf2

    d = list(map(int, cpf))  # transforma uma string para uma lista de inteiros

    def dotProd(v1: List[int], v2: List[int]
                ) -> int: return sum(map(mul, v1, v2))

    def getDigit(n): return 0 if n <= 1 else 11 - n

    v2 = dotProd(cpf2, d)
    v2 = getDigit(v2 % 11)

    d.append(v2)

    v1 = dotProd(cpf1, d)
    v1 = getDigit(v1 % 11)

    return (v2 * 10 + v1) == dv


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if (len(argv) < 2):
        cpf = input("Entre com um número de CPF para ser testado: xxx.xxx.xxx-dv ")
    else:
        cpf = argv[1]

    dv = int(cpf[-2:])
    cpf = cpf[0:-2]
    cpf = cpf.replace(".", "").replace("-", "")
    if not (len(cpf) == 9 and cpf.isdigit()):
        sys.exit("CPF Invalido !!!")

    if areValidDigits(cpf, dv):
        resp = ""
    else:
        resp = " não"

    print("%s-%s %s é CPF válido! " % (cpf, dv, resp))
    print(dv)
    print(cpf)
    print(len(cpf))
    print(cpf.isdigit())
    print(resp)


if __name__ == "__main__":
    sys.exit(main())
