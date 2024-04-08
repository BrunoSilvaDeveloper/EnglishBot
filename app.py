import telebot
from telebot import types
import random
from openpyxl import load_workbook


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



def AlterarUsuario(user, linha):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    aba_ativa[f'A{linha}'] = user.get_id()
    aba_ativa[f'B{linha}'] = user.get_frase()
    aba_ativa[f'C{linha}'] = user.get_traducao()
    aba_ativa[f'D{linha}'] = user.get_nivel()
    aba_ativa[f'E{linha}'] = user.get_number()
    aba_ativa[f'F{linha}'] = user.get_ultimoComando()
    aba_ativa[f'G{linha}'] = user.get_fraseOrAprender()
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
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 30 and numero < 40:
        ab1 = aba_ativa['A22'].value
        ab2 = f'A{numero-29}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 40 and numero < 50:
        ab1 = aba_ativa['A23'].value
        ab2 = f'A{numero-39}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 50 and numero < 60:
        ab1 = aba_ativa['A24'].value
        ab2 = f'A{numero-49}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 60 and numero < 70:
        ab1 = aba_ativa['A25'].value
        ab2 = f'A{numero-59}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 70 and numero < 80:
        ab1 = aba_ativa['A26'].value
        ab2 = f'A{numero-69}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 80 and numero < 90:
        ab1 = aba_ativa['A27'].value
        ab2 = f'A{numero-79}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel

    elif numero > 90 and numero < 100:
        ab1 = aba_ativa['A28'].value
        ab2 = f'A{numero-89}'
        ab21 = aba_ativa[ab2].value
        cel = f'{ab1} {ab21}'
        return cel
    
def verificar_centena(numero):

    planilha = load_workbook('Aprendendo.xlsx')
    aba_ativa = planilha['Numeros']

    if numero == 100:
        ab1 = aba_ativa['A2'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 200:
        ab1 = aba_ativa['A3'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 300:
        ab1 = aba_ativa['A4'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 400:
        ab1 = aba_ativa['A5'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 500:
        ab1 = aba_ativa['A6'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 600:
        ab1 = aba_ativa['A7'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel 
    
    if numero == 700:
        ab1 = aba_ativa['A8'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 800:
        ab1 = aba_ativa['A9'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
    
    if numero == 900:
        ab1 = aba_ativa['A10'].value
        ab2 = aba_ativa['A29'].value
        cel = f'{ab1} {ab2}'
        return cel
        
    elif numero > 100 and numero < 200:
        ab1 = aba_ativa['A2'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-100)
        cel = f'{ab1} {ab2} {ab3}'
        return cel

    elif numero > 200 and numero < 300:
        ab1 = aba_ativa['A3'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-200)
        cel = f'{ab1} {ab2} {ab3}'
        return cel
    
    elif numero > 300 and numero < 400:
        ab1 = aba_ativa['A4'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-300)
        cel = f'{ab1} {ab2} {ab3}'
        return cel

    elif numero > 400 and numero < 500:
        ab1 = aba_ativa['A5'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-400)
        cel = f'{ab1} {ab2} {ab3}'
        return cel
    
    elif numero > 500 and numero < 600:
        ab1 = aba_ativa['A6'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-500)
        cel = f'{ab1} {ab2} {ab3}'
        return cel
    
    elif numero > 600 and numero < 700:
        ab1 = aba_ativa['A7'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-600)
        cel = f'{ab1} {ab2} {ab3}'
        return cel
    
    elif numero > 700 and numero < 800:
        ab1 = aba_ativa['A8'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-700)
        cel = f'{ab1} {ab2} {ab3}'
        return cel

    elif numero > 800 and numero < 900:
        ab1 = aba_ativa['A9'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-800)
        cel = f'{ab1} {ab2} {ab3}'
        return cel

    elif numero > 900 and numero < 1000:
        ab1 = aba_ativa['A10'].value
        ab2 = aba_ativa['A29'].value
        ab3 = verificar_dezena(numero-900)
        cel = f'{ab1} {ab2} {ab3}'
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
            cel = f'{ab1} thousand {ab3}'
            return cel
        else:
            ab1 = verificar_dezena(milhar)
            ab2 = verificar_centena(centena)
            ab3 = verificar_dezena(dezena)
            cel = f'{ab1} thousand {ab2} {ab3}'
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


def receberFrases(nivel, choice, user):
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
    user.set_frase(aba_ativa[f'B{number}'].value)
    user.set_traducao(aba_ativa[f'C{number}'].value)
    user.set_nivel(aba_ativa[f'D{number}'].value)

def exibirMenu(user):
    id = user.get_id()
    resposta = f'Olá, seja muito bem vindo! 👋 \n\nEste é o nosso Menu 🏠'
    responder(id, resposta, [['Exibir Frase', '/Frase'], ['Exibir História', '/Historia'], ['Traduzir Frase/História', '/Traducao'], ['Alterar Nível', '/Nivel'], ['Aprender Inglês', '/Aprender'], ['Nosso Propósito', '/Proposito']], 1)

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

def Numbers(mensagem, user):
    id = user.get_id()
    number = user.get_number()

    if mensagem == '/Numbers':
        resposta = f'Você quer aprender sobre números?! 👋 \n\nSelecione o que deseja!'
        responder(id, resposta, [['Conteúdo sobre Numbers', '/ConteudoNumbers'], ['Exibir Number', '/ExibirNumber']], 1)
        

    elif mensagem == '/ConteudoNumbers':
        planilha = load_workbook('Aprendendo.xlsx')
        aba_ativa = planilha['Numeros']
        resposta = aba_ativa['D1'].value
        responder(id, resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)

    elif mensagem == '/ExibirNumber':
        numero = gerar_numero()
        user.set_number(numero)
        resposta = f'O número escolhido foi {numero} '
        responder(id, resposta, [['Escrever por extenso', '/ExtensoNumbers'], ['Exibir Número Extenso', '/ExibirNumberExtenso'], ['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)
    
    elif mensagem == '/ExtensoNumbers':
        user.set_ultimoComando('/ExtensoNumbers')
        resposta = f'Digite o número informado por extenso: '
        responder_sem_button(id, resposta)

    elif mensagem == '/ExibirNumberExtenso':
        extenso = decidir_verificacao_number(int(number))
        resposta = f'\nO número {number} por extenso é: \n\n{extenso}'
        responder(id, resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)

    

def VerificarNumberExtenso(mensagem, user):
    number = user.get_number()
    id = user.get_id()

    if mensagem.capitalize() == decidir_verificacao_number(int(number)):
                resposta = f'Você acertou!'
                user.set_ultimoComando('/Aprender')
                responder(id, resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)
    else:
        extenso = decidir_verificacao_number(int(number)).capitalize()
        resposta = f'Você errou! a traducao correta é: \n\n{extenso}'
        user.set_ultimoComando('/Aprender')
        responder(id, resposta, [['Exibir Number', '/ExibirNumber'], ['Continuar','/OK']], 1)


def verificarComandoFrases(mensagem, user):
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
        resposta = f'Que bom que você queira aprender! 👋 \n\nSelecione a materia que deseja aprender!'
        responder(id, resposta, [['Numbers', '/Numbers']], 1)
        
    elif mensagem == '/Proposito':
        resposta = f'Olá, que bom que queira saber mais de nós 😊 \n\nNosso propósito é ajudar você a treinar e colocar em prática seus estudos de inglês. Eu forneço frases e histórias com o objetivo de você tentar traduzi-las. Depois, você pode verificar se acertou solicitando a tradução da frase ou história. \n\nNós surgimos da necessidade de um lugar onde pudéssemos treinar nossos aprendizados de forma prática, traduzindo pequenos textos ou frases, mas que estes estivessem no nosso nível de aprendizado. Muitas das vezes, outros lugares que tinham essas frases e histórias, não possuíam um nível equivalente ao nosso aprendizado. Dai eu surgi, com o objetivo de te ajudar a aprender cada vez mais. \n\nFico muito feliz de tê-lo por aqui! 😊😊'
        responder(id, resposta, [['Continuar','/OK']], 1)

    else:
        exibirMenu(user)

def verificarComandoAprender(mensagem,user):
    id = user.get_id()
    ultimoComando = user.get_ultimoComando()

    if mensagem == '/Frase':
        user.set_fraseOrAprender('Frase')
        exibirFrase(user)
    
    elif mensagem == '/Historia':
        user.set_fraseOrAprender('Frase')
        exibirHistoria(user)
    
    elif mensagem == '/Traducao':
        user.set_fraseOrAprender('Frase')
        exibirTraducao(user)
    
    elif mensagem == '/Nivel':
        nivel = 'Nivel'
        user.set_fraseOrAprender('Frase')
        AlterarNivel(user, nivel)

    elif mensagem == '/Aprender':
        user.set_ultimoComando('/Aprender')
        resposta =  f'Que bom que você queira aprender! 👋 \n\nSelecione a materia que deseja aprender!'
        responder(id, resposta, [['Numbers', '/Numbers']], 1)

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

   

def Section(mensagem, user):
    usuario = user.get_fraseOrAprender()
    if usuario == 'Frase':
        verificarComandoFrases(mensagem, user)
    elif usuario == 'Aprender':
        verificarComandoAprender(mensagem, user)


def registrarUsuario(user):
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    usuario = [user.get_id(), user.get_frase(), user.get_traducao(), user.get_nivel(), user.get_number(), user.get_ultimoComando(), user.get_fraseOrAprender()]
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
                UltimaComando = aba_ativa[f'F{linha}'].value
                comando = aba_ativa[f'G{linha}'].value
                return [id, frase, traducao, nivel, number, UltimaComando, comando], linha
   
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

