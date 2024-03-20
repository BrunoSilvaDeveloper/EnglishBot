import telebot
import random
from openpyxl import load_workbook

CHAVE_API = "7026978984:AAFxq_Qo4nuQG-J9B5yZYPbHGrQy8xMofnc"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

def receberFrases(nivel, choice):
    if nivel == None:
        nivel == 'Básico'

    if choice == 'Frase':
        planilha = load_workbook('Frases Ingles.xlsx')
        aba_ativa = planilha.get_sheet_by_name(nivel)

    
    elif choice == 'Historia':
        planilha = load_workbook('Historias Ingles.xlsx')
        aba_ativa = planilha.get_sheet_by_name(nivel)

    QtdFrases = len(aba_ativa['A'])
    number = random.randint(2, QtdFrases)
    frase = [aba_ativa[f'B{number}'].value, aba_ativa[f'C{number}'].value, aba_ativa[f'D{number}'].value]
    return frase
        
def exibirFrase(usuario):
    frase = receberFrases(usuario[3], 'Frase')
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

    responder(usuario[0], f'Frase de Nível {usuario[3]}: \n{usuario[1]}')
    return usuario

def exibirHistoria(usuario):
    frase = receberFrases(usuario[3],'Historia')
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

    responder(usuario[0], f'Frase de Nível {usuario[3]}: \n{usuario[1]}')
    return usuario

def exibirTraducao(usuario):
    resposta = usuario[2]
    responder(usuario[0], resposta)

def AlterarNivel(usuario, nivel):
    if nivel == 'Nivel':
        resposta = f'Escolha seu nível: \n/Basico \n/BasicoAvancado \n/Intermediario \n/IntermediarioAvancado \n/Fluente'
        responder(usuario[0], resposta)
    
    else:
        usuario[3] = nivel
        resposta = f'Seu nível foi alterado para: {nivel}'
        responder(usuario[0], resposta)

    return usuario

def exibirMenu(usuario):
    resposta = f'Menu \n/Frase \n/Historia \n/Traducao \n/Nivel'
    responder(usuario[0], resposta)

def verficarComando(mensagem, usuario):
    if mensagem == '/Frase':
        usuario = exibirFrase(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/Historia':
        usuario = exibirHistoria(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/Traducao':
        exibirTraducao(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/Nivel':
        nivel = 'Nivel'
        usuario = AlterarNivel(usuario, nivel)

    elif mensagem == '/Basico':
        nivel = 'Básico'
        usuario = AlterarNivel(usuario, nivel)
        exibirMenu(usuario)
    
    elif mensagem == '/BasicoAvancado':
        nivel = 'Básico Avançado'
        usuario = AlterarNivel(usuario, nivel)
        exibirMenu(usuario)
    
    elif mensagem == '/Intermediario':
        nivel = 'Intermediário'
        usuario = AlterarNivel(usuario, nivel)
        exibirMenu(usuario)
    
    elif mensagem == '/IntermediarioAvancado':
        nivel = 'Intermediário Avançado'
        usuario = AlterarNivel(usuario, nivel)
        exibirMenu(usuario)
    
    elif mensagem == '/Fluente':
        nivel = 'Fluente'
        usuario = AlterarNivel(usuario, nivel)
        exibirMenu(usuario)

    else:
        exibirMenu(usuario)

    return usuario

def verificarUsuario(id):
    listaUsersId = receberListaUser()
    if id in listaUsersId:
        return True
    else: return False

def receberListaUser():
    lista_id = []
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    for celula in aba_ativa['A']:
      if type(celula.value) == int :
        lista_id.append(celula.value)
    return lista_id

def UserInfo(id):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    for celula in aba_ativa['A']:
        if type(celula.value) == int :
            if celula.value == id:
                linha = celula.row
                frase = aba_ativa[f'B{linha}'].value
                traducao = aba_ativa[f'C{linha}'].value
                nivel = aba_ativa[f'D{linha}'].value
                return [id, frase, traducao, nivel], linha
        
def registrarUsuario(usuario):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    aba_ativa.append(usuario)
    planilha.save('Usuarios.xlsx')

def AlterarUsuario(usuario, linha):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    aba_ativa[f'A{linha}'] = usuario[0]
    aba_ativa[f'B{linha}'] = usuario[1]
    aba_ativa[f'C{linha}'] = usuario[2]
    aba_ativa[f'D{linha}'] = usuario[3]
    planilha.save('Usuarios.xlsx')

def responder(id, resposta):
    bot.send_message(id, resposta)

@bot.message_handler(func=verificar)
def receber(mensagem):

    id = mensagem.chat.id
    mensagemUser = mensagem.text

    if verificarUsuario(id):
        print('Usuario existente')
        usuario, linha = UserInfo(id)
    else:
        print('Usuario novo')
        usuario = [id, 'Não existem frases', 'Não existem frases para traduzir, peça uma!', 'Básico']
        registrarUsuario(usuario)
        usuario, linha = UserInfo(id)

    usuario = verficarComando(mensagemUser, usuario)
    AlterarUsuario(usuario, linha)
    
bot.polling()

