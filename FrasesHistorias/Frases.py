import telebot
from telebot import types
import random
from openpyxl import load_workbook
import os

CHAVE_API = "Sua chave api aqui"

bot = telebot.TeleBot(CHAVE_API)


def carregar_planilha(pasta):
    diretorio_atual = os.getcwd()
    dir_atual = diretorio_atual.split('\\')
    if dir_atual[-1] == 'FrasesHistorias':
        os.chdir(os.path.dirname(diretorio_atual))
    pasta_database = os.path.join(diretorio_atual, 'DataBase')
    caminho_arquivo = os.path.join(pasta_database, pasta)
    return caminho_arquivo


def responder(id, resposta, buttons, qtd):
    btn = []
    markup = types.InlineKeyboardMarkup(row_width=qtd)
    for bt in buttons:
        button = types.InlineKeyboardButton(bt[0], callback_data=bt[1])
        btn.append(button)

    markup.add(*btn)

    bot.send_message(id, resposta, reply_markup=markup)   


def receberFrases(nivel, choice, user):
    if nivel == None:
        nivel == 'Básico'

    if choice == 'Frase':
        caminho = carregar_planilha('Frases Ingles.xlsx')
        planilha = load_workbook(caminho)
        aba_ativa = planilha[nivel]

    
    elif choice == 'Historia':
        caminho = carregar_planilha('Historias Ingles.xlsx')
        planilha = load_workbook(caminho)
        aba_ativa = planilha[nivel]

    QtdFrases = len(aba_ativa['A'])
    number = random.randint(2, QtdFrases)
    user.set_frase(aba_ativa[f'B{number}'].value)
    user.set_traducao(aba_ativa[f'C{number}'].value)
    user.set_nivel(aba_ativa[f'D{number}'].value)


def exibirTraducao(user):
    traducao = user.get_traducao()
    id = user.get_id()
    resposta = f'Esta é a sua tradução, espero que tenha acertado! 😊 \n\n{traducao}'
    responder(id, resposta, [['Continuar','/OK']], 1)

def AlterarNivel(user, nivel):
    id = user.get_id()

    if nivel == 'Nivel':
        resposta = f'Escolha seu nível 🤗'
        responder(id, resposta, [['Nível Básico','/Basico'], ['Nível Básico Avançado', '/BasicoAvancado'], ['Nível Intermediário', '/Intermediario'], ['Nível Intermediário Avançado', '/IntermediarioAvancado'], ['Nível Fluente', '/Fluente']], 1)
    
    else:
        user.set_nivel(nivel)
        resposta = f'Seu nível foi alterado para {nivel} 😉'
        responder(id, resposta, [['Continuar','/OK']], 1)


def exibirHistoria(user):
    nivel = user.get_nivel()
    id = user.get_id()
    receberFrases(nivel, 'Historia', user)

    mensagem = user.get_frase()
    nivel = user.get_nivel()
    resposta = f'História de Nível: {nivel}🔥 \n\nEsta é a sua história, bons estudos! \n\n{mensagem}'
    responder(id, resposta, [['Continuar','/OK']], 1)

def exibirFrase(user):
    nivel = user.get_nivel()
    id = user.get_id()
    receberFrases(nivel, 'Frase', user)

    mensagem = user.get_frase()
    nivel = user.get_nivel()
    resposta = f'Frase de Nível: {nivel}🔥 \n\nEsta é a sua frase, bons estudos! \n\n{mensagem}'
    responder(id, resposta, [['Continuar','/OK']], 1)
