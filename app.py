import telebot
import random
from openpyxl import load_workbook

CHAVE_API = "Sua chave API aqui"

bot = telebot.TeleBot(CHAVE_API)

def AlterarUsuario(usuario, linha):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    aba_ativa[f'A{linha}'] = usuario[0]
    aba_ativa[f'B{linha}'] = usuario[1]
    aba_ativa[f'C{linha}'] = usuario[2]
    aba_ativa[f'D{linha}'] = usuario[3]
    planilha.save('Usuarios.xlsx')

def responder(id, resposta):
    bot.send_message(id, resposta, parse_mode="MarkdownV2")   

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

def exibirMenu(usuario):
    resposta = f'Olá, seja muito bem vindo\! 👋 \n\n_Este é o nosso Menu 🏠_ \n\nExibir uma *frase*, clique aqui 👉 _/Frase_ \nExibir uma *história*, clique aqui 👉 _/Historia_ \nExibir a *tradução*, clique aqui 👉 _/Traducao_ \nAlterar o seu *nível*, clique aqui 👉 _/Nivel_ \n\nPara entender nosso *Propósito* \nClique aqui 👉 _/Proposito_'
    responder(usuario[0], resposta)

def exibirTraducao(usuario):
    mensagem = usuario[2].replace('.', '\.')
    mensagem = mensagem.replace('!', '\!')
    mensagem = mensagem.replace('-', '\-')
    responder(usuario[0], f'_Esta é a sua tradução, espero que tenha acertado\! 😊_ \n\n{mensagem} \n\n*_Clique aqui para continuar\.\.\. 👉 /OK_*')

def AlterarNivel(usuario, nivel):
    if nivel == 'Nivel':
        resposta = f'Escolha seu nível 🤗 \n\n*Nível Básico* \nClique aqui 👉 _/Basico_ \n\n*Nível Básico Avançado* \nClique aqui 👉 _/BasicoAvancado_ \n\n*Nível Intemediário* \nClique aqui 👉 _/Intermediario_ \n\n*Nível Intermediário Avançado* \nClique aqui 👉 _/IntermediarioAvancado_ \n\n*Nível Fluente* \nClique aqui 👉 _/Fluente_'
        responder(usuario[0], resposta)
    
    else:
        usuario[3] = nivel
        resposta = f'Seu nível foi alterado para _*{nivel}*_ 😉 \n\n*_Clique aqui para continuar\.\.\. 👉 /OK_*'
        responder(usuario[0], resposta)

    return usuario

def exibirHistoria(usuario):
    frase = receberFrases(usuario[3],'Historia')
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

    mensagem = usuario[1].replace('.', '\.')
    mensagem = mensagem.replace('!', '\!')
    mensagem = mensagem.replace('-', '\-')
    responder(usuario[0], f'*História de Nível:   {usuario[3]}*🔥 \n\n_Esta é a sua história, bons estudos\!_\n\n{mensagem} \n\n*_Clique aqui para continuar\.\.\. 👉 /OK_*')
    return usuario

def exibirFrase(usuario):
    frase = receberFrases(usuario[3], 'Frase')
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

 
    mensagem = usuario[1].replace('.', '\.')
    mensagem = mensagem.replace('!', '\!')
    mensagem = mensagem.replace('-', '\-')
    responder(usuario[0], f'*Frase de Nível:   {usuario[3]}*🔥 \n\n_Esta é a sua frase, bons estudos\!_\n\n{mensagem} \n\n*_Clique aqui para continuar\.\.\. 👉 /OK_*')
    return usuario

def verficarComando(mensagem, usuario):
    if mensagem == '/Frase':
        usuario = exibirFrase(usuario)
    
    elif mensagem == '/Historia':
        usuario = exibirHistoria(usuario)
    
    elif mensagem == '/Traducao':
        exibirTraducao(usuario)
    
    elif mensagem == '/Nivel':
        nivel = 'Nivel'
        usuario = AlterarNivel(usuario, nivel)

    elif mensagem == '/Basico':
        nivel = 'Básico'
        usuario = AlterarNivel(usuario, nivel)
    
    elif mensagem == '/BasicoAvancado':
        nivel = 'Básico Avançado'
        usuario = AlterarNivel(usuario, nivel)
    
    elif mensagem == '/Intermediario':
        nivel = 'Intermediário'
        usuario = AlterarNivel(usuario, nivel)
    
    elif mensagem == '/IntermediarioAvancado':
        nivel = 'Intermediário Avançado'
        usuario = AlterarNivel(usuario, nivel)
    
    elif mensagem == '/Fluente':
        nivel = 'Fluente'
        usuario = AlterarNivel(usuario, nivel)
    
    elif mensagem == '/Proposito':
        resposta = f'*Olá, que bom que queira saber mais de nós 😊 \n\n_Nosso propósito é ajudar você a treinar e colocar em prática seus estudos de inglês. Eu forneço frases e histórias com o objetivo de você tentar traduzi-las. Depois, você pode verificar se acertou solicitando a tradução da frase ou história. \n\nNós surgimos da necessidade de um lugar onde pudéssemos treinar nossos aprendizados de forma prática, traduzindo pequenos textos ou frases, mas que estes estivessem no nosso nível de aprendizado. Muitas das vezes, outros lugares que tinham essas frases e histórias, não possuíam um nível equivalente ao nosso aprendizado. Dai eu surgi, com o objetivo de te ajudar a aprender cada vez mais. \n\nFico muito feliz de tê-lo por aqui! 😊😊_* \n\n*_Clique aqui para continuar... 👉 /OK_*'
        resposta = resposta.replace('.', '\.')
        resposta = resposta.replace('!', '\!')
        resposta = resposta.replace('-', '\-')
        responder(usuario[0], resposta)

    else:
        exibirMenu(usuario)

    return usuario

def registrarUsuario(usuario):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    aba_ativa.append(usuario)
    planilha.save('Usuarios.xlsx')

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
   
def receberListaUser():
    lista_id = []
    planilha = load_workbook('Usuarios.xlsx')
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
    else:
        print('Usuario novo')
        usuario = [id, 'Não existem frases', 'Não existem frases para traduzir, peça uma!', 'Básico']
        registrarUsuario(usuario)
        usuario, linha = UserInfo(id)

    usuario = verficarComando(mensagemUser, usuario)
    AlterarUsuario(usuario, linha)

bot.polling()

