from openpyxl import load_workbook
import sqlite3
import os

def caminho_db(db_name):
    diretorio_atual = os.getcwd()
    dir_atual = diretorio_atual.split('\\')
    if dir_atual[-1] == 'AcessarBancos':
        os.chdir(os.path.dirname(diretorio_atual))
    pasta_database = os.path.join(diretorio_atual, 'DataBase')
    caminho_arquivo = os.path.join(pasta_database, db_name)
    return caminho_arquivo

def inserir_dados_user(db_name, user):
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    Usuarios_db.execute('INSERT INTO DadosFrases (Id, Frase, Traducao, Nivel) VALUES (?, ?, ?, ?)', (user.get_id(), user.get_frase(), user.get_traducao(),user.get_nivel()))
    Usuarios_db.execute('INSERT INTO DadosAprender (Id, UltimoComando, FrasesAprender, Letra, Number) VALUES (?, ?, ?, ?, ?)', (user.get_id(), user.get_ultimoComando(), user.get_fraseOrAprender(), user.get_letra(), user.get_number()))
    db.commit()
    db.close()

def receber_dados_user(db_name, id):
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    query = f'SELECT df.Id, df.Frase, df.Traducao, df.Nivel, da.UltimoComando, da.FrasesAprender, da.Letra, da.Number FROM DadosFrases as df INNER JOIN DadosAprender as da ON df.Id = da.Id WHERE df.Id == {id}'
    Usuarios_db.execute(query)
    dados = Usuarios_db.fetchall()
    lista_dados = []
    for tupla in dados:
        lista_dados.extend(tupla)
    db.close()
    return lista_dados

def receber_lista_id(db_name):
    lista_id = []
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    query = f'SELECT id FROM DadosAprender'
    Usuarios_db.execute(query)
    for x in Usuarios_db.fetchall():
        lista_id.append(x[0])
    db.close()
    return lista_id

def alterar_dados_user(user, db_name):
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    Usuarios_db.execute('UPDATE DadosFrases SET Frase = ?, Traducao = ?, Nivel = ? WHERE id = ? ', (user.get_frase(), user.get_traducao(), user.get_nivel(), user.get_id()))
    Usuarios_db.execute('UPDATE DadosAprender SET UltimoComando = ?, FrasesAprender = ?, Letra = ?, Number = ? WHERE id = ? ', (user.get_ultimoComando(), user.get_fraseOrAprender(), user.get_letra(), user.get_number(), user.get_id()))
    db.commit()
    db.close()



def acessar_planilha():
    planilha = load_workbook('Usuarios.xlsx')
    aba_ativa = planilha.active
    for celula in aba_ativa['A']:
        if type(celula.value) == int :
            linha = celula.row
            id = aba_ativa[f'A{linha}'].value
            frase = aba_ativa[f'B{linha}'].value
            traducao = aba_ativa[f'C{linha}'].value
            nivel = aba_ativa[f'D{linha}'].value
            number = aba_ativa[f'E{linha}'].value
            UltimoComando = aba_ativa[f'F{linha}'].value
            frasesAprender = aba_ativa[f'G{linha}'].value
            letra = aba_ativa[f'H{linha}'].value
            inserir_dados_user([id, frase, traducao, nivel, UltimoComando, frasesAprender, letra, number])

def criar_tabela(db_name):
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    Usuarios_db.execute('CREATE TABLE DadosFrases (Id integer, Frase text, Traducao text, Nivel text)')
    Usuarios_db.execute('CREATE TABLE DadosAprender (Id integer, UltimoComando text, FrasesAprender text, Letra text, Number integer)')
    print('Tabela criada com sucesso')
    db.close()

def deletar_dados(db_name):
    try:
        caminho = caminho_db(db_name)
        db = sqlite3.connect(caminho)
        Usuarios_db = db.cursor()
        Usuarios_db.execute('DELETE from DadosFrases')
        Usuarios_db.execute('DELETE from DadosAprender')
        db.commit()
        db.close()
        
    except sqlite3.Error as error:
        print(f'Erro ao deletar os dados: {error}')

