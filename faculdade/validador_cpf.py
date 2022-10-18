# Validador CPF
# Fazendo as importações necessarias, Precisa do PySimpleGUI, tkinter
import PySimpleGUI as sg
import sys

if sys.version_info[0] == 3:
    import tkinter as tk
else:
    import Tkinter as tk


# Classe para validar CPF
class CPF:
    # contrutor do cpf
    def __init__(self, cpf):
        self.cpf = cpf

    # metodo para validar tamanho do cpf
    def valida_tamanho_cpf(self):
        if len(self.cpf) == 11:
            return True
        else:
            return False

    # metodo que verifica se o cpf só tem numeros
    def valida_caracteres_cpf(self):
        if self.cpf.isnumeric():
            return True
        else:
            return False

    # metodo para validar os digitos verificadores do cpf
    def valida_digito_cpf(self):
        soma_digito_1, soma_digito_2 = 0, 0
        lista = list(self.cpf)
        if lista[0] == lista[1] == lista[2] == lista[3] == lista[4] == lista[5] == lista[6] == lista[7] == lista[8] == \
                lista[9] == lista[10]:
            return False
        else:
            for i in range(0, 9):
                soma_digito_1 += int(lista[i]) * (10 - i)
            resto1 = int(soma_digito_1 * 10) % 11
            if resto1 == 10:
                resto1 = 0

            for i in range(0, 10):
                soma_digito_2 += int(lista[i]) * (11 - i)
            resto2 = int(soma_digito_2 * 10) % 11
            if resto2 == 10:
                resto2 = 0

            if resto1 == int(lista[9]) and resto2 == int(lista[10]):
                return True
            else:
                return False

    # Função para validar o CPF
    def valida_cpf(self):
        if self.valida_tamanho_cpf() and self.valida_caracteres_cpf() and self.valida_digito_cpf():
            return True
        else:
            return False


# Usando a biblioteca de interface  PySimpleGUI
sg.theme('DarkTanBlue')
layout = [
    [sg.Text('Validador de CPF', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Digite apenas os numeros')],
    [sg.Text('Digite seu CPF'), sg.InputText(), sg.Button('Validar')]]

# Criando a janela
janela = sg.Window('Validador CPF', layout)
# Evento loop para pegar os valores e rodar os eventos
while True:
    event, values = janela.read()
    # Fechar a janela
    if event == sg.WIN_CLOSED:
        break
    # Se o usuário clicar no botão Validar vai verificar se está correto
    if event == 'Validar':
        cpf = CPF(values[0])
        if cpf.valida_cpf():
            sg.popup('CPF Válido',
                     'Você digitou os numeros corretamente')
        else:
            sg.popup('CPF Inválido',
                     'Verifique se Digitou apenas os numeros corretamente')

janela.close()
