from openpyxl import load_workbook
import sqlite3

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
            inserir_dados([id, frase, traducao, nivel, UltimoComando, frasesAprender, letra, number])

def criar_tabela():
    db = sqlite3.connect('Usuarios.db')
    Usuarios_db = db.cursor()
    Usuarios_db.execute('CREATE TABLE DadosFrases (Id integer, Frase text, Traducao text, Nivel text)')
    Usuarios_db.execute('CREATE TABLE DadosAprender (Id integer, UltimoComando text, FrasesAprender text, Letra text, Number integer)')
    print('Tabela criada com sucesso')
    db.close()

def inserir_dados(dados):
    db = sqlite3.connect('Usuarios.db')
    Usuarios_db = db.cursor()
    id, frase, traducao, nivel, ultimoComando, frasesAprender, letra, number = dados
    Usuarios_db.execute('INSERT INTO DadosFrases (Id, Frase, Traducao, Nivel) VALUES (?, ?, ?, ?)', (id, frase, traducao, nivel))
    Usuarios_db.execute('INSERT INTO DadosAprender (Id, UltimoComando, FrasesAprender, Letra, Number) VALUES (?, ?, ?, ?, ?)', (id, ultimoComando, frasesAprender, letra, number))
    db.commit()
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

def deletar_dados():
    try:
        db = sqlite3.connect('Usuarios.db')
        Usuarios_db = db.cursor()
        Usuarios_db.execute('DELETE from DadosFrases')
        Usuarios_db.execute('DELETE from DadosAprender')
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
