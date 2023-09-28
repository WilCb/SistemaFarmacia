import PySimpleGUI as sg
import sqlite3 as bb
from designGrafico import graficoTelaLogin as gtl, GraficoCadFuncionario as gcf, graficoTelaADM as telaADM


# banco de dados

conn = bb.connect('banco.db')
c = conn.cursor()

# Layout tela login

fonte = 'Arial 18'

layout = [[gtl()]]

janelaLayout = sg.Window('Tela de login', layout, size=(600, 400), font=fonte, background_color='#87CEFA')

while True:
    event, values = janelaLayout.read()

    if event == sg.WINDOW_CLOSED or event == 'Sair':
        break
    
    # Valida se o campos de login foram preenchidos corretamente
    if event == 'Entrar' and values['usuario'] == '' or values['senha'] == '':

        sg.popup(
            'Informe usuário e senha corretamente',
            title='Usuário inválido',
            button_color='yellowgreen',
            background_color='red',
            text_color='black'
            )

    # Usuário para entrar no acesso exclusivo de adm
    # Somente no usuário ADM terá acesso a cadastro de usuários, consulta, e exclusão
    # Além de cadastro de produto e exclusão do estoque
    if event == 'Entrar' and values['usuario'] == 'adm' and values['senha'] == 'adm':
        
        # tela do ADM

        layoutInicialAdm = [[telaADM()]]

        janelaLayoutInicial = sg.Window('Tela inicial', layoutInicialAdm, size=(600, 600))

        while True:
            event, values = janelaLayoutInicial.read()

            if event == sg.WINDOW_CLOSED:
                janelaLayoutInicial.close()
                break
            
            if event == 'Cadastrar funcionários':

                layoutCadFuncionario = [[gcf()]]

            janelaCadastro = sg.Window('Cadastro', layoutCadFuncionario, size=(600, 600))

            while True:

                event, values = janelaCadastro.read()

                if event == sg.WINDOW_CLOSED or event == 'Voltar':
                    janelaCadastro.close()
                    break
                if event == 'Cadastrar':

                    valores = (
                        values['nome'], values['cpf'], values['dn'], values['cargo'], values['salario'], values['rua'], values['numero'], values['bairro'], values['cidade'], values['uf'],
                        )

                    c.execute('''INSERT INTO funcionarios(Nome, CPF, Data_de_nascimento, Cargo, Salário, Rua, Número, Bairro, Cidade, UF) VALUES(? ,? ,? ,? ,? ,? ,? ,?, ?, ? )''', valores)
                    conn.commit()

                    sg.popup('Cadastro efetuado', title='Confirmação')

                    janelaCadastro['nome'].update('')
                    janelaCadastro['cpf'].update('')
                    janelaCadastro['dn'].update('')
                    janelaCadastro['cargo'].update('')
                    janelaCadastro['salario'].update('')
                    janelaCadastro['rua'].update('')
                    janelaCadastro['numero'].update('')
                    janelaCadastro['bairro'].update('')
                    janelaCadastro['cidade'].update('')
                    janelaCadastro['uf'].update('')

                if event == 'Lista de funcionários':

                    layoutCosulta = [
                        [sg.Text('Nome'), sg.InputText(key='nome')],
                        [sg.Button('Buscar')],
                        [sg.Table(values=[values['nome']], headings=['NOME', 'CPF', 'DN', 'CARGO', 'SALÁRIO', 'RUA', 'NÚMERO', 'BAIRRO', 'CIDADE', 'UF']
                                , key='table', expand_x=True, justification='c')]
                    ]

                    janelaConsulta = sg.Window('Tela de Consulta', layoutCosulta, size=(800, 800), resizable=True)

                    while True:
                        
                        event, values = janelaConsulta.read()

                        if event == sg.WINDOW_CLOSED:
                            janelaConsulta.close()
                            break
                        
                        if event == 'Buscar':
                            
                            buscaFuncionario = values['nome'].upper()

                            c.execute('SELECT Nome, CPF, Data_de_nascimento,Cargo, Salário, Rua, Número, Bairro, Cidade, UF FROM funcionarios WHERE UPPER(Nome) = ?', (buscaFuncionario,)) 

                            res = c.fetchall()
                            
                            janelaConsulta['table'].update(values=res)


                        
        
    if event == 'Entrar' and values['usuario'] == 'caixa' and values['senha'] == 'caixa':
        
        layoutCaixa = [
            [sg.Text('Sistema de Caixa')],
            [sg.Text('Código Produto: ')],
            [sg.InputText(key='produto')],
            [sg.Table(values, headings=(['Produto'], ['Valor']), expand_x=True)]
        ]

        janelaCaixa = sg.Window('Caixa 1.0', layoutCaixa, size=(600, 600))

        while True:
            event, values = janelaCaixa.read()

            if event == sg.WINDOW_CLOSED:
                janelaCaixa.close()
                break

janelaLayout.close()