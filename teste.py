import PySimpleGUI as sg
import sqlite3 as bb
from designGrafico import GraficoCadFuncionario as gcf

# banco de dados

conn = bb.connect('banco.db')

c = conn.cursor()

# Layout

fonte = 'Arial 18'

layoutCadFuncionario = [
    [gcf()]                 
]

janelaCadastro = sg.Window('Cadastro', layoutCadFuncionario, size=(600, 600))

while True:

    event, values = janelaCadastro.read()

    if event == sg.WINDOW_CLOSED or event == 'Voltar':
        janelaCadastro.close()
        break
    if event == 'Cadastrar':

        valores = ( values['nome'], values['cpf'], values['dn'], values['rua'], values['numero'], values['bairro'], values['cidade'], values['uf'],)

        c.execute('''INSERT INTO funcionarios(Nome, CPF, Data_de_nascimento, Rua, Número, Bairro, Cidade, UF) VALUES(? ,? ,? ,? ,? ,? ,? ,? )''', valores)
        conn.commit()

        sg.popup('Cadastro efetuado', title='Confirmação')

        janelaCadastro['nome'].update('')
        janelaCadastro['cpf'].update('')
        janelaCadastro['dn'].update('')
        janelaCadastro['rua'].update('')
        janelaCadastro['numero'].update('')
        janelaCadastro['bairro'].update('')
        janelaCadastro['cidade'].update('')
        janelaCadastro['uf'].update('')

    if event == 'Lista de funcionários':

        layoutCosulta = [
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Button('Buscar')],
            [sg.Table(values=[values['nome']], headings=['NOME', 'CPF', 'DN', 'RUA', 'NÚMERO', 'BAIRRO', 'CIDADE', 'UF']
                      , key='table', expand_x=True, justification='c')]
        ]

        janelaConsulta = sg.Window('Tela de Consulta', layoutCosulta, size=(800, 800))

        while True:
            
            event, values = janelaConsulta.read()

            if event == sg.WINDOW_CLOSED:
                janelaConsulta.close()
                break
            
            if event == 'Buscar':
                
                buscaFuncionario = values['nome'].upper()

                c.execute('SELECT Nome, CPF, Data_de_nascimento, Rua, Número, Bairro, Cidade, UF FROM funcionarios WHERE UPPER(Nome) = ?', (buscaFuncionario,)) 

                res = c.fetchall()
                
                janelaConsulta['table'].update(values=res)

                
                

        