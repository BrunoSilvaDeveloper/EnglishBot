
import re
import requests
import json

class TelegramBot:
  def __init__(self):
    token = '7026978984:AAFxq_Qo4nuQG-J9B5yZYPbHGrQy8xMofnc'
    self.url_base = f'https://api.telegram.org/bot{token}/'

  #iniciar o bot
  def Iniciar(self, update_id, chat_id):
    while True: 
        atualizacao = self.obter_mensagens(update_id)
        mensagens = atualizacao['result']
        if mensagens:
            for mensagem in mensagens:
                update_id = mensagem['update_id']
                chat_id = mensagem['message']['from']['id']
                mensagembot = mensagem['message']['text']
            return mensagembot, chat_id, update_id
          
  #obter mensagens
  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}' 
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

#criar resposta

  def responder(self, resposta, chat_id):
     #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

user = TelegramBot()
update_id = None
chat_id = None
lista_chat_id = ['425']

while True:
    mensagem, chat_id, update_id = user.Iniciar(update_id, chat_id)
    for id in lista_chat_id:
        if id == chat_id:
            print('ja tem')
        else:
            resposta = 'Ola'
    lista_chat_id.append(id)
    user.responder(resposta, chat_id)