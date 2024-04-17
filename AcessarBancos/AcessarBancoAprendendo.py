from openpyxl import load_workbook
import sqlite3

def acessar_planilha(aba, db, tabela):
    planilha = load_workbook('Aprendendo.xlsx')
    aba_ativa = planilha[aba]
    for celula in aba_ativa['A']:
        linha = celula.row
        numero = int(linha) -1
        string = aba_ativa[f'A{linha}'].value
        conteudo = aba_ativa[f'D{linha}'].value
        query = f'{tabela} (Numero, String, Conteudo) VALUES ({numero}, "{string}", "{conteudo}")'
        inserir_dados(query, db)


def criar_tabela(Tabela, campos):
    # Passar o nome da tabela e as colunas que serao criadas na tabela
    db = sqlite3.connect('Aprendendo.db')
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

def receber_dados(tabela):
    db = sqlite3.connect('Usuarios.db')
    Usuarios_db = db.cursor()
    if tabela == 'DadosFrases':
        Usuarios_db.execute('SELECT * FROM DadosFrases')

    elif tabela == 'DadosAprender':
        Usuarios_db.execute('SELECT * FROM DadosAprender')

    elif tabela == 'Todas':
        Usuarios_db.execute('SELECT df.Id, df.Frase, df.Traducao, df.Nivel, da.UltimoComando, da.FrasesAprender, da.Letra, da.Number FROM DadosFrases as df INNER JOIN DadosAprender as da ON df.Id = da.Id')

    dados = Usuarios_db.fetchall()
    db.close()
    return dados

def receber_lista_id(tabela):
    lista_id = []
    db = sqlite3.connect('Usuarios.db')
    Usuarios_db = db.cursor()
    Usuarios_db.execute('SELECT id FROM DadosFrases')
    for x in Usuarios_db.fetchall():
        lista_id.append(x[0])
    db.close()
    return lista_id

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


def alterar_dados(dados, user):
    frase, traducao, nivel, ultimoComando, frasesAprender, letra, number = dados
    db = sqlite3.connect('Usuarios.db')
    Usuarios_db = db.cursor()
    Usuarios_db.execute('UPDATE DadosFrases SET Frase = ?, Traducao = ?, Nivel = ? WHERE id = ? ', (frase, traducao, nivel, user))
    Usuarios_db.execute('UPDATE DadosAprender SET UltimoComando = ?, FrasesAprender = ?, Letra = ?, Number = ? WHERE id = ? ', (ultimoComando, frasesAprender, letra, number, user))
    db.commit()
    db.close()


#acessar_planilha('Numeros', 'Aprendendo.db', 'Numeros') # aba, NomeBanco, Nometabela
#criar_tabela('Alphabet', '(Letra text, Pronuncia text)')
#deletar_dados('Numeros', 'Aprendendo.db')
#adicionar_colunas('Numeros', 'Conteudo', 'Text', 'Aprendendo.db')
