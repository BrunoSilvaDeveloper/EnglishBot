import telebot
from telebot import types
from openpyxl import load_workbook
from AcessarBancos.AcessarBancoFrasesHistorias import receber_dados_FH
import os

CHAVE_API = "Sua chave API"

bot = telebot.TeleBot(CHAVE_API)

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
        nivel == 'Basico'

    if choice == 'Frase':
        frase, traducao, nivel = receber_dados_FH(nivel, 'Frases.db')

    
    elif choice == 'Historia':
        frase, traducao, nivel = receber_dados_FH(nivel, 'Historias.db')

    user.set_frase(frase)
    user.set_traducao(traducao)
    user.set_nivel(nivel)

def exibirTraducao(user):
    traducao = user.get_traducao()
    id = user.get_id()
    resposta = f'Esta é a sua tradução, espero que tenha acertado! 😊 \n\n{traducao}'
    responder(id, resposta, [['Continuar','/Menu']], 1)

def AlterarNivel(user, nivel):
    id = user.get_id()

    if nivel == 'Nivel':
        resposta = f'Escolha seu nível 🤗'
        responder(id, resposta, [['Nível Básico','/Basico'], ['Nível Básico Avançado', '/BasicoAvancado'], ['Nível Intermediário', '/Intermediario'], ['Nível Intermediário Avançado', '/IntermediarioAvancado'], ['Nível Fluente', '/Fluente']], 1)
    
    else:
        user.set_nivel(nivel)
        resposta = f'Seu nível foi alterado para {nivel} 😉'
        responder(id, resposta, [['Continuar','/Menu']], 1)

def exibirHistoria(user):
    nivel = user.get_nivel()
    id = user.get_id()
    receberFrases(nivel, 'Historia', user)

    mensagem = user.get_frase()
    nivel = user.get_nivel()
    resposta = f'História de Nível: {nivel}🔥 \n\nEsta é a sua história, bons estudos! \n\n{mensagem}'
    responder(id, resposta, [['Continuar','/Menu']], 1)

def exibirFrase(user):
    nivel = user.get_nivel()
    id = user.get_id()
    receberFrases(nivel, 'Frase', user)

    mensagem = user.get_frase()
    nivel = user.get_nivel()
    resposta = f'Frase de Nível: {nivel}🔥 \n\nEsta é a sua frase, bons estudos! \n\n{mensagem}'
    responder(id, resposta, [['Continuar','/Menu']], 1)
