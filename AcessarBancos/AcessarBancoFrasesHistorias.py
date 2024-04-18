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


def acessar_planilha(aba, db, tabela):
    planilha = load_workbook('Historias Ingles.xlsx')
    aba_ativa = planilha[aba]
    for celula in aba_ativa['B']:
        linha = celula.row
        if linha != 1:
            ingles = aba_ativa[f'B{linha}'].value
            portugues = aba_ativa[f'C{linha}'].value
            nivel = aba_ativa[f'D{linha}'].value
            query = f'{tabela} (Ingles, Portugues, Nivel) VALUES ("{ingles}", "{portugues}", "{nivel}")'
            inserir_dados(query, db)


def criar_tabela(Tabela, campos):
    # Passar o nome da tabela e as colunas que serao criadas na tabela
    db = sqlite3.connect('Historias.db')
    Usuarios_db = db.cursor()
    query = f'CREATE TABLE {Tabela} {campos}'
    Usuarios_db.execute(query)
    print('Tabela criada com sucesso')
    db.close()

def inserir_dados(dados, db):
    # Passar uma string com o NomeTabela (coluna1, coluna2, coluna3 ...) VALUES (valor1, valor2, valo3...)
    db = sqlite3.connect(db)
    Usuarios_db = db.cursor()
    query = f'INSERT INTO {dados}'
    Usuarios_db.execute(query)
    db.commit()
    db.close()

def adicionar_colunas(Tabela, Coluna, tipoDado, db):
    db = sqlite3.connect(db)
    Usuarios_db = db.cursor()
    query = f'ALTER TABLE {Tabela} ADD COLUMN {Coluna} {tipoDado}'
    Usuarios_db.execute(query)
    print('Tabela Alterada com sucesso')
    db.close()

def receber_dados_FH(tabela, db_name):
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    if tabela == 'Basico':
        Usuarios_db.execute('SELECT * FROM Basico ORDER BY RANDOM() LIMIT 1')

    elif tabela == 'Basico Avancado':
        Usuarios_db.execute('SELECT * FROM Basico_Avancado ORDER BY RANDOM() LIMIT 1')

    elif tabela == 'Intermediario':
        Usuarios_db.execute('SELECT * FROM Intermediario ORDER BY RANDOM() LIMIT 1')

    elif tabela == 'Intermediario Avancado':
        Usuarios_db.execute('SELECT * FROM Intermediario_Avancado ORDER BY RANDOM() LIMIT 1')

    elif tabela == 'Fluente':
        Usuarios_db.execute('SELECT * FROM Fluente ORDER BY RANDOM() LIMIT 1')
    
    dados = Usuarios_db.fetchall()
    lista_dados = []
    for tupla in dados:
        lista_dados.extend(tupla)
    db.close()
    return lista_dados

def deletar_dados(tabela, db):
    try:
        db = sqlite3.connect(db)
        Usuarios_db = db.cursor()
        query = f'DELETE from {tabela}'
        Usuarios_db.execute(query)
        db.commit()
        db.close()
        
    except sqlite3.Error as error:
        print(f'Erro ao deletar os dados: {error}')


def alterar_dados(db_name):
    caminho = caminho_db(db_name)
    db = sqlite3.connect(caminho)
    Usuarios_db = db.cursor()
    Usuarios_db.execute('UPDATE Basico SET Nivel = ? ', ('Basico',))
    Usuarios_db.execute('UPDATE Basico_Avancado SET Nivel = ? ', ('Basico Avancado',))
    Usuarios_db.execute('UPDATE Intermediario SET Nivel = ? ', ('Intermediario',))
    Usuarios_db.execute('UPDATE Intermediario_Avancado SET Nivel = ? ', ('Intermediario Avancado',))
    Usuarios_db.execute('UPDATE Fluente SET Nivel = ? ', ('Fluente',))

    db.commit()
    db.close()


#acessar_planilha('Intermediário', 'Historias.db', 'Intermediario') # aba, NomeBanco, Nometabela
#criar_tabela('Basico', '(Ingles text, Portugues text, Nivel text)')
#deletar_dados('Basico', 'Frases.db')
#adicionar_colunas('Numeros', 'Conteudo', 'Text', 'Aprendendo.db')
