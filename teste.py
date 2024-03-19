from openpyxl import load_workbook
import random

planilha = load_workbook('Usuarios.xlsx')
aba_ativa = planilha.active
'''
for celula in aba_ativa['A']:
    if celula.value.isnumeric():
        print('existem usuarios')
        if celula.value == '356':
            linha = celula.row
            aba_ativa[f'B{linha}'] = 'What time is it?'
            aba_ativa[f'C{linha}'] = 'Que horas são?'
            aba_ativa[f'D{linha}'] = 'Basico'
    else: 
        print('nao existem usuarios')

linha = len(aba_ativa['A'])+1
aba_ativa[f'A{linha}'] = '356'
aba_ativa[f'B{linha}'] = 'usuario novo'
aba_ativa[f'C{linha}'] = 'Que horas são?'
aba_ativa[f'D{linha}'] = 'Basico'

planilha.save('Usuarios.xlsx')
'''

def receberFrases():
    planilha = load_workbook('Frases Ingles.xlsx')
    aba_ativa = planilha.active
    QtdFrases = len(aba_ativa['A'])
    number = random.randint(0, QtdFrases+1)
    frase = [aba_ativa[f'B{number}'].value, aba_ativa[f'C{number}'].value, aba_ativa[f'D{number}'].value]
    return frase

frase = receberFrases()
print(frase[0])