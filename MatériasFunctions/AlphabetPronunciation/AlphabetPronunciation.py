import telebot
from telebot import types
from openpyxl import load_workbook
import os
import random

CHAVE_API = "Sua chave API"

bot = telebot.TeleBot(CHAVE_API)


def carregar_planilha():
    diretorio_atual = os.getcwd()
    dir_atual = diretorio_atual.split('\\')
    if dir_atual[-1] == 'AlphabetPronunciation':
        os.chdir(os.path.dirname(os.path.dirname(diretorio_atual)))
    pasta_database = os.path.join(diretorio_atual, 'DataBase')
    caminho_arquivo = os.path.join(pasta_database, 'Pronuncia Alfabeto.xlsx')
    return caminho_arquivo

def carregar_audio(letra):
    diretorio_atual = os.getcwd()
    dir_atual = diretorio_atual.split('\\')
    if dir_atual[-1] == 'AlphabetPronunciation':
        os.chdir(os.path.dirname(os.path.dirname(diretorio_atual)))
    pasta_audios = os.path.join(diretorio_atual, 'Audios Alfabeto')
    caminho_arquivo = os.path.join(pasta_audios, f'{letra}.ogg')
    return caminho_arquivo

def responder(id, resposta, buttons, qtd):
    btn = []
    markup = types.InlineKeyboardMarkup(row_width=qtd)
    for bt in buttons:
        button = types.InlineKeyboardButton(bt[0], callback_data=bt[1])
        btn.append(button)

    markup.add(*btn)

    bot.send_message(id, resposta, reply_markup=markup)   


def enviar_audio(id, letra):
    caminho = carregar_audio(letra)
    bot.send_voice(id, open(caminho, 'rb'))

def menu_letras(user):
    id = user.get_id()
    resposta = f'Pronúncia do alfabeto em inglês! \n\nSelecione uma letra!'
    botoes = [['A', '/A'], ['B', '/B'], ['C', '/C'], ['D', '/D'], ['E', '/E'], ['F', '/F'], ['G', '/G'], ['H', '/H'], ['I', '/I'], ['J', '/J'], ['K', '/K'], ['L', '/L'], ['M', '/M'], ['N', '/N'], ['O', '/O'], ['P', '/P'], ['Q', '/Q'], ['R', '/R'], ['S', '/S'], ['T', '/T'], ['U', '/U'], ['V', '/V'], ['W', '/W'], ['X', '/X'], ['Y', '/Y'], ['Z', '/Z'], ['Matérias', '/Aprender'], ['Menu', '/OK']]
    responder(id, resposta, botoes , 4)

def exibir_audio(user, letra):
    id = user.get_id()
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if letra in alfabeto:
        enviar_audio(id, letra)
        caminho = carregar_planilha()
        planilha = load_workbook(caminho)
        aba_ativa = planilha.active
        indexLetra = alfabeto.index(letra) + 1
        pronuncia = aba_ativa[f'B{indexLetra}'].value
        resposta = f'Letra: {letra}   Pronúncia: {pronuncia}'
        responder(id, resposta, [['Alphabet Pronunciation', '/Alfabet'], ['Alphabet Training', '/TreinarAlfabeto'], ['Matérias', '/Aprender'], ['Menu', '/OK']] , 1)
    else:
        menu_letras(user)
        

def verificar_pronuncia(user, mensagem):
    letra = user.get_letra()
    id = user.get_id()
    if mensagem.upper() == letra:
                resposta = f'Você acertou!'
                user.set_ultimoComando('/Aprender')
                responder(id, resposta, [['Exibir Letra', '/TreinarAlfabeto'], ['Matérias', '/Aprender'], ['Menu','/OK']], 1)
    else:
        resposta = f'Você errou! a letra correta é: {letra}'
        user.set_ultimoComando('/Aprender')
        responder(id, resposta, [['Exibir Letra', '/TreinarAlfabeto'], ['Matérias', '/Aprender'], ['Menu','/OK']], 1)

def treinar_pronuncia(user):
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    id = user.get_id()
    letra = alfabeto[random.randint(0, 25)]
    user.set_letra(letra)
    enviar_audio(id, letra)
    resposta = f'Digite a letra exibida no audio: '
    responder(id, resposta, [['Voltar', '/Alfabeto']], 1)
    user.set_ultimoComando('/VerificarPronuncia')
    

def exibir_alfabeto(user, mensagem):
    try:
        alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        letra = mensagem.split('/')[1]
        if letra in alfabeto:
            exibir_audio(user, letra)
        
        else:
            menu_letras(user)
    except:
        menu_letras(user)


def alphabet(user, mensagem):
    id = user.get_id()
    if mensagem == '/Alfabeto':
        resposta = f'Selecione o que deseja!'
        responder(id, resposta, [['Alphabet Pronunciation', '/Alfabet'],['Alphabet Training', '/TreinarAlfabeto'], ['Matérias', '/Aprender'], ['Menu','/OK']], 1)
    
    elif mensagem == '/TreinarAlfabeto':
        treinar_pronuncia(user)
    
    elif mensagem == '/Alfabet':
        menu_letras(user)

    else:
        exibir_alfabeto(user, mensagem)