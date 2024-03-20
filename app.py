import telebot
import random
from openpyxl import load_workbook

CHAVE_API = "7026978984:AAFxq_Qo4nuQG-J9B5yZYPbHGrQy8xMofnc"

bot = telebot.TeleBot(CHAVE_API)

def verificar(mensagem):
    return True

def receberFrases():
    planilha = load_workbook('Frases Ingles.xlsx')
    aba_ativa = planilha.active
    QtdFrases = len(aba_ativa['A'])
    number = random.randint(0, QtdFrases+1)
    frase = [aba_ativa[f'B{number}'].value, aba_ativa[f'C{number}'].value, aba_ativa[f'D{number}'].value]
    return frase
        

def exibirFrase(usuario):
    frase = receberFrases()
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

    responder(usuario[0], f'Frase de Nível {usuario[3]}: \n{usuario[1]}')
    return usuario

def exibirTraducao(usuario):
    resposta = usuario[2]
    responder(usuario[0], resposta)
    return usuario

def AlterarNivel(usuario):
    pass

def exibirMenu(usuario):
    resposta = f'Menu \n/Exibir \n/Traducao'
    responder(usuario[0], resposta)

def verficarComando(mensagem, usuario):
    if mensagem == '/Exibir':
        usuario = exibirFrase(usuario)
        exibirMenu(usuario)
        return usuario
    
    elif mensagem == '/Traducao':
        exibirTraducao(usuario)
        exibirMenu(usuario)
        return usuario
    
    elif mensagem == '/Nivel':
        AlterarNivel(usuario)
        exibirMenu(usuario)

    elif mensagem == '/Basico':
        AlterarNivel(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/BasicoAvancado':
        AlterarNivel(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/Intermediario':
        AlterarNivel(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/IntermediarioAvancado':
        AlterarNivel(usuario)
        exibirMenu(usuario)
    
    elif mensagem == '/Fluente':
        AlterarNivel(usuario)
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
    linha = len(aba_ativa['A'])+1
    aba_ativa[f'A{linha}'] = usuario[0]
    aba_ativa[f'B{linha}'] = usuario[1]
    aba_ativa[f'C{linha}'] = usuario[2]
    aba_ativa[f'D{linha}'] = usuario[3]
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
        usuario = [id, None, None, None]
        registrarUsuario(usuario)
        usuario, linha = UserInfo(id)

    usuario = verficarComando(mensagemUser, usuario)
    AlterarUsuario(usuario, linha)
    print(usuario)
    

bot.polling()

