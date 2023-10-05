import PySimpleGUI as sg
import sqlite3 as bb
from lista import listaUf as estados, listaCidades as cidades

# banco de dados

conn = bb.connect('banco.db')
c = conn.cursor()

# Layout

fonte = 'Arial 18'

titulo = [
    [sg.Text('Bem vindo ao WL Farmácia', font='Arial 30', text_color='black', background_color='#87CEFA')],
    [sg.Text('', background_color='#87CEFA')]
]

formularioLogin = [
    [sg.Text('Usuário: ', font='arial 13', text_color='black', background_color='#00BFFF')],
    [sg.InputText(key='usuario', size=(10))],
    [sg.Text('Senha: ', font='arial 13', text_color='black', background_color='#00BFFF')],
    [sg.InputText(key='senha', password_char='*', size=(10))],
    [sg.Button('Entrar', font='arial 13', size=(7)), sg.Button('Sair', font='arial 13', size=(5))]
]

layout = [
    [sg.Column(titulo, justification='c', background_color='#87CEFA')],
    [sg.Column(formularioLogin, justification='c', background_color='#00BFFF')]
]

janelaLayout = sg.Window('Tela de login', layout, size=(600, 400), font=fonte, background_color='#87CEFA')

while True:
    event, values = janelaLayout.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    

    # Usuário para entrar no acesso exclusivo de adm
    # Somente no usuário ADM terá acesso a cadastro de usuários, consulta, e exclusão
    # Além de cadastro de produto e exclusão do estoque
    if event == 'Entrar' and values['usuario'] == 'adm' and values['senha'] == 'adm':
        
        layoutInicialAdm = [
            [sg.Button('Cadastrar funcionários'), sg.Button('Consulta de funcionários'), sg.Button('Deletar de funcionários')],
            [sg.Button('Cadastro de produto'), sg.Button('Consulta de produto'), sg.Button('Deletar de produto')]        
        ]

        janelaLayoutInicial = sg.Window('Tela inicial', layoutInicialAdm, size=(600, 600))

        while True:
            event, values = janelaLayoutInicial.read()

            if event == sg.WINDOW_CLOSED:
                janelaLayoutInicial.close()
                break
            
            if event == 'Cadastrar funcionários':

                layoutCadFuncionario = [
                    [sg.Text('Dados pessoais', font='Arial 30')],
                    [sg.Text('Nome: ')],
                    [sg.Input(key='nome')],
                    [sg.Text('CPF')],
                    [sg.Input(key='cpf', size=(13))],
                    [sg.Text('Data de Nascimento: ')],
                    [sg.CalendarButton('Escolher data', font='Arial 10', format='%d/%m/%y'), 
                     sg.InputText(key='dn', size=(8, 20))],
                    [sg.Text('Endereço', font='Arial 30')],
                    [sg.Text('Rua')],
                    [sg.Input(key='rua'),
                     sg.Text('Número: '), sg.Input(key='numero', size=(8, 20))],
                    [sg.Text('Bairro')],
                    [sg.Input(key='bairro')],
                    [sg.Text('Cidade: '),
                     sg.OptionMenu(cidades(), ['selecione'], key='cidade', size=(8, 20)), 
                     sg.Text('UF: '),
                     sg.OptionMenu(estados(), ['selecione'], key='uf', size=(8, 20))],
                    [sg.Button('Cadastrar'), sg.Button('Lista de funcionários'), sg.Button('Voltar')]
                    
                ]

                janelaCadastro = sg.Window('Cadastro', layoutCadFuncionario, size=(800, 800))

                while True:

                    event, values = janelaCadastro.read()

                    if event == sg.WINDOW_CLOSED or event == 'Voltar':
                        janelaCadastro.close()
                        break
                    if event == 'Cadastrar':

                        c.execute('''INSERT INTO funcionarios(
                                Nome,
                                CPF,
                                Data_de_nascimento,
                                Rua,
                                Número,
                                Bairro,
                                Cidade,
                                UF
                                )
                                
                                VALUES(? ,? ,? ,? ,? ,? ,? ,? )''', (
                                    values['nome'],
                                    values['cpf'],
                                    values['dn'],
                                    values['rua'],
                                    values['numero'],
                                    values['bairro'],
                                    values['cidade'],
                                    values['uf'],
                                ))
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
                            [sg.Text('Nome'), sg.InputText(key='nome')]
                        ]

                        janelaConsulta = sg.Window('Tela de Consulta', layoutCosulta)

                        while True:
                            
                            event, values = janelaConsulta.read()

                            if event == sg.WINDOW_CLOSED:
                                janelaConsulta.close()
                                break                       
        
    elif event == 'Entrar' and values['usuario'] == 'caixa' and values['senha'] == 'caixa':
        
        LayoutCaixa = [
            [sg.Text('Sistema de Caixa')],
            [sg.Text('Código Produto: ')],
            [sg.InputText(key='produto')],
            [sg.Table(values, headings=(['Produto'], ['Valor']), expand_x=True)]
        ]

        janelaCaixa = sg.Window('Caixa 1.0', LayoutCaixa, size=(600, 600))

        while True:
            event, values = janelaCaixa.read()

            if event == sg.WINDOW_CLOSED:
                janelaCaixa.close()
                break
    
    vazio = ''
    login = ['adm', 'caixa']

    # Valida se o campos de login foram preenchidos corretamente
    # if event == 'Entrar' and values['usuario'] == '' or values['senha'] == '':
    if event == 'Entrar' and values['usuario'] != login or values['senha'] != login:
        sg.popup(
            'Usuário ou senha inválido',
            title='Usuário inválido',
            button_color='yellowgreen',
            background_color='red',
            text_color='black'
            )
    

janelaLayout.close()

    