import telebot
from telebot import types
from openpyxl import load_workbook
from MatériasFunctions.Numbers.Numbers import Numbers, VerificarNumberExtenso
from FrasesHistorias.Frases import exibirFrase, exibirHistoria, exibirTraducao, AlterarNivel
import os

CHAVE_API = "Sua chave API"

bot = telebot.TeleBot(CHAVE_API)


class User():
    def __init__(self, id, frase, traducao, nivel, number, ultimoComando, fraseOrAprender):
        self.__id = id
        self.__frase = frase
        self.__traducao = traducao
        self.__nivel = nivel
        self.__number = number
        self.__ultimoComando = ultimoComando
        self.__fraseOrAprender = fraseOrAprender

    def get_id(self):
        return self.__id
    
    def get_frase(self):
        return self.__frase
    
    def get_traducao(self):
        return self.__traducao
    
    def get_nivel(self):
        return self.__nivel
    
    def get_number(self):
        return self.__number
    
    def get_ultimoComando(self):
        return self.__ultimoComando
    
    def get_fraseOrAprender(self):
        return self.__fraseOrAprender
    
    def set_id(self, id):
        self.__id = id

    def set_frase(self, frase):
        self.__frase = frase

    def set_traducao(self, traducao):
        self.__traducao = traducao

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def set_number(self, number):
        self.__number = number

    def set_ultimoComando(self, ultimoComando):
        self.__ultimoComando = ultimoComando

    def set_fraseOrAprender(self, fraseOrAprender):
        self.__fraseOrAprender = fraseOrAprender

def carregar_planilha(pasta):
    diretorio_atual = os.getcwd()
    pasta_database = os.path.join(diretorio_atual, 'DataBase')
    caminho_arquivo = os.path.join(pasta_database, pasta)
    return caminho_arquivo

def AlterarUsuario(user, linha):
    caminho = carregar_planilha('Usuarios.xlsx')
    planilha = load_workbook(caminho)
    aba_ativa = planilha.active
    aba_ativa[f'A{linha}'] = user.get_id()
    aba_ativa[f'B{linha}'] = user.get_frase()
    aba_ativa[f'C{linha}'] = user.get_traducao()
    aba_ativa[f'D{linha}'] = user.get_nivel()
    aba_ativa[f'E{linha}'] = user.get_number()
    aba_ativa[f'F{linha}'] = user.get_ultimoComando()
    aba_ativa[f'G{linha}'] = user.get_fraseOrAprender()
    planilha.save(caminho)

def responder(id, resposta, buttons, qtd):
    btn = []
    markup = types.InlineKeyboardMarkup(row_width=qtd)
    for bt in buttons:
        button = types.InlineKeyboardButton(bt[0], callback_data=bt[1])
        btn.append(button)

    markup.add(*btn)

    bot.send_message(id, resposta, reply_markup=markup)   

def responder_sem_button(id, resposta):
    bot.send_message(id, resposta)   


def exibirMenu(user):
    id = user.get_id()
    resposta = f'Olá, seja muito bem vindo! 👋 \n\nEste é o nosso Menu 🏠'
    responder(id, resposta, [['Frases ou Histórias', '/FraseHistoria'], ['Aprender Inglês', '/Aprender'], ['Nosso Propósito', '/Proposito']], 1)


def Frases(mensagem, user):
    id = user.get_id()
    if mensagem == '/Frase':
        exibirFrase(user)
    
    elif mensagem == '/Historia':
        exibirHistoria(user)
    
    elif mensagem == '/Traducao':
        exibirTraducao(user)
    
    elif mensagem == '/Nivel':
        nivel = 'Nivel'
        AlterarNivel(user, nivel)

    elif mensagem == '/Basico':
        nivel = 'Básico'
        AlterarNivel(user, nivel)
    
    elif mensagem == '/BasicoAvancado':
        nivel = 'Básico Avançado'
        AlterarNivel(user, nivel)
    
    elif mensagem == '/Intermediario':
        nivel = 'Intermediário'
        AlterarNivel(user, nivel)
    
    elif mensagem == '/IntermediarioAvancado':
        nivel = 'Intermediário Avançado'
        AlterarNivel(user, nivel)
    
    elif mensagem == '/Fluente':
        nivel = 'Fluente'
        AlterarNivel(user, nivel)

    elif mensagem == '/Aprender':
        user.set_fraseOrAprender('Aprender')
        verificarComandoAprender(mensagem, user)
        
    elif mensagem == '/Proposito':
        resposta = f'Olá, que bom que queira saber mais de nós 😊 \n\nNosso propósito é ajudar você a treinar e colocar em prática seus estudos de inglês. Eu forneço frases e histórias com o objetivo de você tentar traduzi-las. Depois, você pode verificar se acertou solicitando a tradução da frase ou história. \n\nNós surgimos da necessidade de um lugar onde pudéssemos treinar nossos aprendizados de forma prática, traduzindo pequenos textos ou frases, mas que estes estivessem no nosso nível de aprendizado. Muitas das vezes, outros lugares que tinham essas frases e histórias, não possuíam um nível equivalente ao nosso aprendizado. Dai eu surgi, com o objetivo de te ajudar a aprender cada vez mais. \n\nFico muito feliz de tê-lo por aqui! 😊😊'
        responder(id, resposta, [['Continuar','/OK']], 1)

    else:
        exibirMenu(user)

def verificarComandoAprender(mensagem,user):
    id = user.get_id()
    ultimoComando = user.get_ultimoComando()

    if mensagem == '/FraseHistoria':
        user.set_fraseOrAprender('Frase')
        verificarComandoFrases(mensagem, user)

    elif mensagem == '/Frase' or mensagem == '/Historia' or mensagem == '/Traducao' or mensagem == '/Nivel':
        user.set_fraseOrAprender('Frase')
        Frases(mensagem, user)
    
    elif mensagem == '/Aprender':
        user.set_ultimoComando('/Aprender')
        resposta =  f'Que bom que você queira aprender! 👋 \n\nSelecione a materia que deseja aprender!'
        responder(id, resposta, [['Numbers', '/Numbers'], ['Menu', '/OK']], 1)

    elif ultimoComando == '/Aprender':
        if mensagem == '/Numbers' or mensagem == '/ConteudoNumbers' or mensagem == '/ExibirNumber' or mensagem == '/ExtensoNumbers' or mensagem == '/ExibirNumberExtenso':
            Numbers(mensagem, user)
        else:  
            user.set_ultimoComando('/OK') 
            exibirMenu(user)
        
    elif mensagem == '/Proposito':
        resposta = f'Olá, que bom que queira saber mais de nós 😊 \n\nNosso propósito é ajudar você a treinar e colocar em prática seus estudos de inglês. Eu forneço frases e histórias com o objetivo de você tentar traduzi-las. Depois, você pode verificar se acertou solicitando a tradução da frase ou história. \n\nNós surgimos da necessidade de um lugar onde pudéssemos treinar nossos aprendizados de forma prática, traduzindo pequenos textos ou frases, mas que estes estivessem no nosso nível de aprendizado. Muitas das vezes, outros lugares que tinham essas frases e histórias, não possuíam um nível equivalente ao nosso aprendizado. Dai eu surgi, com o objetivo de te ajudar a aprender cada vez mais. \n\nFico muito feliz de tê-lo por aqui! 😊😊'
        responder(id, resposta, [['Continuar','/OK']], 1)

    else:
        if ultimoComando == '/ExtensoNumbers':
            VerificarNumberExtenso(mensagem, user)
        else:
            exibirMenu(user)

def verificarComandoFrases(mensagem,user):
    id = user.get_id()
    if mensagem == '/FraseHistoria' or mensagem == '/Menu':
        resposta = f'Este é o nosso Menu de Frases e Histórias 🏠'
        responder(id, resposta, [['Exibir Frase', '/Frase'], ['Exibir História', '/Historia'], ['Traduzir Frase/História', '/Traducao'], ['Alterar Nível', '/Nivel'], ['Nosso Propósito', '/Proposito'], ['Menu', '/OK']], 1)

    else:
        Frases(mensagem, user)
   

def Section(mensagem, user):
    usuario = user.get_fraseOrAprender()
    if usuario == 'Frase':
        verificarComandoFrases(mensagem, user)
    elif usuario == 'Aprender':
        verificarComandoAprender(mensagem, user)


def registrarUsuario(user):
    caminho = carregar_planilha('Usuarios.xlsx')
    planilha = load_workbook(caminho)
    aba_ativa = planilha.active
    usuario = [user.get_id(), user.get_frase(), user.get_traducao(), user.get_nivel(), user.get_number(), user.get_ultimoComando(), user.get_fraseOrAprender()]
    aba_ativa.append(usuario)
    planilha.save(caminho)

def UserInfo(id):
    caminho = carregar_planilha('Usuarios.xlsx')
    planilha = load_workbook(caminho)
    aba_ativa = planilha.active
    for celula in aba_ativa['A']:
        if type(celula.value) == int :
            if celula.value == id:
                linha = celula.row
                frase = aba_ativa[f'B{linha}'].value
                traducao = aba_ativa[f'C{linha}'].value
                nivel = aba_ativa[f'D{linha}'].value
                number = aba_ativa[f'E{linha}'].value
                UltimaComando = aba_ativa[f'F{linha}'].value
                comando = aba_ativa[f'G{linha}'].value
                return [id, frase, traducao, nivel, number, UltimaComando, comando], linha
   
def receberListaUser():
    lista_id = []
    caminho = carregar_planilha('Usuarios.xlsx')
    planilha = load_workbook(caminho)
    aba_ativa = planilha.active
    for celula in aba_ativa['A']:
      if type(celula.value) == int :
        lista_id.append(celula.value)
    return lista_id

def verificarUsuario(id):
    listaUsersId = receberListaUser()
    if id in listaUsersId:
        return True
    else: return False

def verificar(mensagem):
    return True


@bot.message_handler(func=verificar)
def receber(mensagem):

    id = mensagem.chat.id
    mensagemUser = mensagem.text

    if verificarUsuario(id):
        print('Usuario existente')
        usuario, linha = UserInfo(id)
        user = User(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
    else:
        print('Usuario novo')
        user = User(id, 'Não existem frases', 'Não existem frases para traduzir, peça uma!', 'Básico', 0, '/OK', 'Frase')
        registrarUsuario(user)
        usuario, linha = UserInfo(id)


    
    Section(mensagemUser, user)
    AlterarUsuario(user, linha)

@bot.callback_query_handler(func=lambda call:True)
def receber_btn(callback):
    id = callback.message.chat.id
    mensagemUser = callback.data

    if verificarUsuario(id):
        print('Usuario existente')
        usuario, linha = UserInfo(id)
        user = User(usuario[0], usuario[1], usuario[2], usuario[3], usuario[4], usuario[5], usuario[6])
    else:
        print('Usuario novo')
        user = User(id, 'Não existem frases', 'Não existem frases para traduzir, peça uma!', 'Básico', 0, '/OK', 'Frase')
        registrarUsuario(user)
        usuario, linha = UserInfo(id)

    Section(mensagemUser, user)
    AlterarUsuario(user, linha)


bot.polling()

