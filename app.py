import telebot
from telebot import types
import random
from openpyxl import load_workbook

CHAVE_API = ""

bot = telebot.TeleBot(CHAVE_API)

def AlterarUsuario(usuario, linha):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    aba_ativa[f'A{linha}'] = usuario[0]
    aba_ativa[f'B{linha}'] = usuario[1]
    aba_ativa[f'C{linha}'] = usuario[2]
    aba_ativa[f'D{linha}'] = usuario[3]
    aba_ativa[f'E{linha}'] = usuario[4]
    aba_ativa[f'F{linha}'] = usuario[5]
    aba_ativa[f'G{linha}'] = usuario[6]
    planilha.save('Usuarios.xlsx')

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

def gerar_numero():
    probabilidade = random.random() 
    
    if probabilidade < 0.4:
        return random.randint(0, 100) 
    elif probabilidade < 0.7:
        return random.randint(101, 500) 
    elif probabilidade < 0.9:
        return random.randint(501, 3000) 
    else:
        return random.randint(3001, 99999)
    
def verificar_dezena(numero):
    planilha = load_workbook('Aprendendo.xlsx')
    aba_ativa = planilha['Numeros']

    if numero >= 0 and numero < 21:
        cel = f'A{numero+1}'
        return aba_ativa[cel].value

    elif numero == 30:
        cel = aba_ativa['A22'].value
        return cel

    elif numero == 40:
        cel = aba_ativa['A23'].value
        return cel

    elif numero == 50:
        cel = aba_ativa['A24'].value
        return cel

    elif numero == 60:
        cel = aba_ativa['A25'].value
        return cel

    elif numero == 70:
        cel = aba_ativa['A26'].value
        return cel

    elif numero == 80:
        cel = aba_ativa['A27'].value
        return cel

    elif numero == 90:
        cel = aba_ativa['A28'].value
        return cel
        
    elif numero > 20 and numero < 30:
        ab1 = aba_ativa['A21'].value
        ab2 = f'A{numero-19}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 30 and numero < 40:
        ab1 = aba_ativa['A22'].value
        ab2 = f'A{numero-29}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 40 and numero < 50:
        ab1 = aba_ativa['A23'].value
        ab2 = f'A{numero-39}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 50 and numero < 60:
        ab1 = aba_ativa['A24'].value
        ab2 = f'A{numero-49}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 60 and numero < 70:
        ab1 = aba_ativa['A25'].value
        ab2 = f'A{numero-59}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 70 and numero < 80:
        ab1 = aba_ativa['A26'].value
        ab2 = f'A{numero-69}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 80 and numero < 90:
        ab1 = aba_ativa['A27'].value
        ab2 = f'A{numero-79}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel

    elif numero > 90 and numero < 100:
        ab1 = aba_ativa['A28'].value
        ab2 = f'A{numero-89}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1}-{ab21}'
        return cel
    
def verificar_centena(numero):

    planilha = load_workbook('Aprendendo.xlsx')
    aba_ativa = planilha['Numeros']

    if numero == 100:
        ab1 = aba_ativa['A2'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 200:
        ab1 = aba_ativa['A3'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 300:
        ab1 = aba_ativa['A4'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 400:
        ab1 = aba_ativa['A5'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 500:
        ab1 = aba_ativa['A6'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 600:
        ab1 = aba_ativa['A7'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel 
    
    if numero == 700:
        ab1 = aba_ativa['A8'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 800:
        ab1 = aba_ativa['A9'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
    
    if numero == 900:
        ab1 = aba_ativa['A10'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1}-{ab2}'
        return cel
        
    elif numero > 100 and numero < 200:
        ab1 = aba_ativa['A2'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-100)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel

    elif numero > 200 and numero < 300:
        ab1 = aba_ativa['A3'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-200)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel
    
    elif numero > 300 and numero < 400:
        ab1 = aba_ativa['A4'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-300)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel

    elif numero > 400 and numero < 500:
        ab1 = aba_ativa['A5'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-400)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel
    
    elif numero > 500 and numero < 600:
        ab1 = aba_ativa['A6'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-500)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel
    
    elif numero > 600 and numero < 700:
        ab1 = aba_ativa['A7'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-600)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel
    
    elif numero > 700 and numero < 800:
        ab1 = aba_ativa['A8'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-700)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel

    elif numero > 800 and numero < 900:
        ab1 = aba_ativa['A9'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-800)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel

    elif numero > 900 and numero < 1000:
        ab1 = aba_ativa['A10'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-900)
        cel = f'{ab1}-{ab2} and {ab3}'
        return cel

def verificar_milhar(numero):
    n = str(numero)
    if len(n) == 4:
        milhar = int(n[0])
        centena = int(n[-3])*100
        dezena = int(n[-2]+n[-1])
    elif len(n) == 5:
        milhar = int(n[0]+n[1])
        centena = int(n[-3])*100
        dezena = int(n[-2]+n[-1])

    if numero > 999 and numero < 100000:
        if centena == 0:
            ab1 = verificar_dezena(milhar)
            ab3 = verificar_dezena(dezena)
            cel = f'{ab1}-thousand and {ab3}'
            return cel
        else:
            ab1 = verificar_dezena(milhar)
            ab2 = verificar_centena(centena)
            ab3 = verificar_dezena(dezena)
            cel = f'{ab1}-thousand and {ab2} and {ab3}'
            return cel
        
def decidir_verificacao_number(numero):
    if numero < 100:
        cel = verificar_dezena(numero).capitalize()
        return cel

    elif numero >=100 and numero < 1000:
        cel = verificar_centena(numero).capitalize()
        return cel

    elif numero >=1000:
        cel = verificar_milhar(numero).capitalize()
        return cel


def receberFrases(nivel, choice):
    if nivel == None:
        nivel == 'Básico'

    if choice == 'Frase':
        planilha = load_workbook('Frases Ingles.xlsx')
        aba_ativa = planilha[nivel]

    
    elif choice == 'Historia':
        planilha = load_workbook('Historias Ingles.xlsx')
        aba_ativa = planilha[nivel]

    QtdFrases = len(aba_ativa['A'])
    number = random.randint(2, QtdFrases)
    frase = [aba_ativa[f'B{number}'].value, aba_ativa[f'C{number}'].value, aba_ativa[f'D{number}'].value]
    return frase

def exibirMenu(usuario):
    resposta = f'Olá, seja muito bem vindo! 👋 \n\nEste é o nosso Menu 🏠'
    responder(usuario[0], resposta, [['Exibir Frase', '/Frase'], ['Exibir História', '/Historia'], ['Traduzir Frase/História', '/Traducao'], ['Alterar Nível', '/Nivel'], ['Aprender Inglês', '/Aprender'], ['Nosso Propósito', '/Proposito']], 1)

def exibirTraducao(usuario):
    mensagem = usuario[2]
    resposta = f'Esta é a sua tradução, espero que tenha acertado! 😊 \n\n{mensagem}'
    responder(usuario[0], resposta, [['Continuar','/OK']], 1)

def AlterarNivel(usuario, nivel):
    if nivel == 'Nivel':
        resposta = f'Escolha seu nível 🤗'
        responder(usuario[0], resposta, [['Nível Básico','/Basico'], ['Nível Básico Avançado', '/BasicoAvancado'], ['Nível Intermediário', '/Intermediario'], ['Nível Intermediário Avançado', '/IntermediarioAvancado'], ['Nível Fluente', '/Fluente']], 1)
    
    else:
        usuario[3] = nivel
        resposta = f'Seu nível foi alterado para {nivel} 😉'
        responder(usuario[0], resposta, [['Continuar','/OK']], 1)

    return usuario

def exibirHistoria(usuario):
    frase = receberFrases(usuario[3],'Historia')
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

    mensagem = usuario[1]
    mensagem = usuario[1]
    resposta = f'História de Nível: {usuario[3]}🔥 \n\nEsta é a sua frase, bons estudos! \n\n{mensagem}'
    responder(usuario[0], resposta, [['Continuar','/OK']], 1)
    return usuario

def exibirFrase(usuario):
    frase = receberFrases(usuario[3], 'Frase')
    usuario[1] = frase[0]
    usuario[2] = frase[1]
    usuario[3] = frase[2]

 
    mensagem = usuario[1]
    resposta = f'Frase de Nível: {usuario[3]}🔥 \n\nEsta é a sua frase, bons estudos! \n\n{mensagem}'
    responder(usuario[0], resposta, [['Continuar','/OK']], 1)
    return usuario

def Numbers(mensagem, usuario):
    if mensagem == '/Numbers':
        resposta = f'Você quer aprender sobre números?! 👋 \n\nSelecione o que deseja!'
        responder(usuario[0], resposta, [['Conteúdo sobre Numbers', '/ConteudoNumbers'], ['Exibir Number', '/ExibirNumber']], 1)
        

    elif mensagem == '/ConteudoNumbers':
        planilha = load_workbook('Aprendendo.xlsx')
        aba_ativa = planilha['Numeros']
        resposta = aba_ativa['D1'].value
        responder(usuario[0], resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)

    elif mensagem == '/ExibirNumber':
        numero = gerar_numero()
        usuario[4] = numero
        resposta = f'O número escolhido foi {numero} '
        responder(usuario[0], resposta, [['Escrever por extenso', '/ExtensoNumbers'], ['Exibir Número Extenso', '/ExibirNumberExtenso'], ['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)
    
    elif mensagem == '/ExtensoNumbers':
        usuario[5] = '/ExtensoNumbers'
        resposta = f'Digite o número informado por extenso: '
        responder_sem_button(usuario[0], resposta)

    elif mensagem == '/ExibirNumberExtenso':
        extenso = decidir_verificacao_number(int(usuario[4]))
        resposta = f'\nO número {usuario[4]} por extenso é: \n\n{extenso}'
        responder(usuario[0], resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)

    

    return usuario

def VerificarNumberExtenso(mensagem, usuario):
    if mensagem == decidir_verificacao_number(int(usuario[4])):
                resposta = f'Você acertou!'
                usuario[5] = '/Aprender'
                responder(usuario[0], resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)
    else:
        extenso = decidir_verificacao_number(int(usuario[4]))
        resposta = f'Você errou! a traducao correta é: \n\n{extenso}'
        usuario[5] = '/Aprender'
        responder(usuario[0], resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)

    return usuario

def verificarComandoFrases(mensagem, usuario):
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

    elif mensagem == '/Aprender':
        usuario[6] = 'Aprender'
        resposta = f'Que bom que você queira aprender! 👋 \n\nSelecione a materia que deseja aprender!'
        responder(usuario[0], resposta, [['Numbers', '/Numbers']], 1)
        
    elif mensagem == '/Proposito':
        resposta = f'Olá, que bom que queira saber mais de nós 😊 \n\nNosso propósito é ajudar você a treinar e colocar em prática seus estudos de inglês. Eu forneço frases e histórias com o objetivo de você tentar traduzi-las. Depois, você pode verificar se acertou solicitando a tradução da frase ou história. \n\nNós surgimos da necessidade de um lugar onde pudéssemos treinar nossos aprendizados de forma prática, traduzindo pequenos textos ou frases, mas que estes estivessem no nosso nível de aprendizado. Muitas das vezes, outros lugares que tinham essas frases e histórias, não possuíam um nível equivalente ao nosso aprendizado. Dai eu surgi, com o objetivo de te ajudar a aprender cada vez mais. \n\nFico muito feliz de tê-lo por aqui! 😊😊'
        responder(usuario[0], resposta, [['Continuar','/OK']], 1)

    else:
        exibirMenu(usuario)

    return usuario

def verificarComandoAprender(mensagem, usuario):
    if mensagem == '/Frase':
        usuario[6] = 'Frase'
        usuario = exibirFrase(usuario)
    
    elif mensagem == '/Historia':
        usuario[6] = 'Frase'
        usuario = exibirHistoria(usuario)
    
    elif mensagem == '/Traducao':
        usuario[6] = 'Frase'
        exibirTraducao(usuario)
    
    elif mensagem == '/Nivel':
        nivel = 'Nivel'
        usuario[6] = 'Frase'
        usuario = AlterarNivel(usuario, nivel)

    elif mensagem == '/Aprender':
        usuario[5] = '/Aprender'
        resposta =  f'Que bom que você queira aprender! 👋 \n\nSelecione a materia que deseja aprender!'
        responder(usuario[0], resposta, [['Numbers', '/Numbers']], 1)

    elif usuario[5] == '/Aprender':
        if mensagem == '/Numbers' or mensagem == '/ConteudoNumbers' or mensagem == '/ExibirNumber' or mensagem == '/ExtensoNumbers' or mensagem == '/ExibirNumberExtenso':
            usuario = Numbers(mensagem, usuario)
        else:
            usuario[5] == '/OK'
            exibirMenu(usuario)
        
    elif mensagem == '/Proposito':
        resposta = f'Olá, que bom que queira saber mais de nós 😊 \n\nNosso propósito é ajudar você a treinar e colocar em prática seus estudos de inglês. Eu forneço frases e histórias com o objetivo de você tentar traduzi-las. Depois, você pode verificar se acertou solicitando a tradução da frase ou história. \n\nNós surgimos da necessidade de um lugar onde pudéssemos treinar nossos aprendizados de forma prática, traduzindo pequenos textos ou frases, mas que estes estivessem no nosso nível de aprendizado. Muitas das vezes, outros lugares que tinham essas frases e histórias, não possuíam um nível equivalente ao nosso aprendizado. Dai eu surgi, com o objetivo de te ajudar a aprender cada vez mais. \n\nFico muito feliz de tê-lo por aqui! 😊😊'
        responder(usuario[0], resposta, [['Continuar','/OK']], 1)

    else:
        if usuario[5] == '/ExtensoNumbers':
            usuario = VerificarNumberExtenso(mensagem, usuario)
        else:
            exibirMenu(usuario)

    return usuario

def Section(mensagem, usuario):
    if usuario[6] == 'Frase':
        usuario = verificarComandoFrases(mensagem, usuario)
    elif usuario[6] == 'Aprender':
        usuario = verificarComandoAprender(mensagem, usuario)

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
                number = aba_ativa[f'E{linha}'].value
                UltimaMensagem = aba_ativa[f'F{linha}'].value
                comando = aba_ativa[f'G{linha}'].value
                return [id, frase, traducao, nivel, number, UltimaMensagem, comando], linha
   
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
        usuario = [id, 'Não existem frases', 'Não existem frases para traduzir, peça uma!', 'Básico', 0, '/OK', 'Frase']
        registrarUsuario(usuario)
        usuario, linha = UserInfo(id)

    
    usuario = Section(mensagemUser, usuario)
    AlterarUsuario(usuario, linha)

@bot.callback_query_handler(func=lambda call:True)
def receber_btn(callback):
    id = callback.message.chat.id
    mensagemUser = callback.data

    if verificarUsuario(id):
        print('Usuario existente')
        usuario, linha = UserInfo(id)
    else:
        print('Usuario novo')
        usuario = [id, 'Não existem frases', 'Não existem frases para traduzir, peça uma!', 'Básico', 0, '/OK', 'Frases']
        registrarUsuario(usuario)
        usuario, linha = UserInfo(id)

    usuario = Section(mensagemUser, usuario)
    AlterarUsuario(usuario, linha)


bot.polling()

