import PySimpleGUI as sg
import sqlite3 as bb
from designGrafico import TelaLogin as gtl, CadFuncionario as gcf, TelaADM as telaADM, consulFuncionario as cf, cadastrarProduto as cp


def loopLogin():
    # banco de dados

    conn = bb.connect('banco.db')
    c = conn.cursor()
    
    # Layout tela login
    layout = [[gtl()]]
    janelaLayout = sg.Window('Tela de login', layout, size=(600, 400), font='Arial 18', background_color='#87CEFA')

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
            janelaLayout.close()
            
            def loop():
                # tela do ADM
                layoutInicialAdm = [[telaADM()]]
                janelaLayoutInicial = sg.Window('Tela inicial', layoutInicialAdm, size=(600, 600))

                while True:
                    event, values = janelaLayoutInicial.read()

                    # Fecha o sistema
                    if event == sg.WINDOW_CLOSED or event == 'Logout':
                        janelaLayoutInicial.close()
                        break
                    
                    # Volta a tela de login
                    if event == 'Trocar usuário':
                        janelaLayoutInicial.close()
                        loopLogin()

                    # Tela de cadastro de funcionários
                    if event == 'Cadastrar funcionários':
                        janelaLayoutInicial.close()

                        layoutCadFuncionario = [[gcf()]]

                        janelaCadastro = sg.Window('Cadastro', layoutCadFuncionario, size=(600, 600))

                        while True:

                            event, values = janelaCadastro.read()

                            if event == sg.WINDOW_CLOSED:
                                janelaCadastro.close()
                                break
                            if event == 'Voltar':
                                janelaCadastro.close()
                                loop()
                            if event == 'Logout':
                                janelaCadastro.close()
                                break

                            # Confirmar cadastro de funcionário preenchido nos inputs
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

                            # Consultar funcionários cadastrados
                            if event == 'Lista de funcionários':
                                janelaCadastro.close()

                                def deleteFunc(nameDelete):
                                    c.execute('DELETE FROM funcionarios WHERE UPPER(Nome) =?', (nameDelete,))
                                    conn.commit()

                                layoutConsulta = [
                                    [cf()],
                                    [sg.Table(values=[values['nome']], headings=['NOME', 'CPF', 'DN', 'CARGO', 'SALÁRIO', 'RUA', 'NÚMERO', 'BAIRRO', 'CIDADE', 'UF'], 
                                            key='table', expand_x=True, justification='c')],
                                    [sg.Button('Excluir')]
                                ]

                                janelaConsulta = sg.Window('Tela de Consulta', layoutConsulta, size=(800, 800), resizable=True)

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

                                    elif event == 'Excluir':
                                        selected_row = values['table']
                                        if selected_row:
                                            selected_row_index = selected_row[0]
                                            row_data = res[selected_row_index]
                                            if sg.popup_yes_no('Tem certeza que deseja excluir este registro?', title='Confirmação') == 'Yes':
                                                nameDelete = row_data[0]
                                                deleteFunc(nameDelete)
                                                res.pop(selected_row_index)
                                                janelaConsulta['table'].update(values=res)
                                                sg.popup('Excluido !', title='Confirmação')
                    
                    if event == 'Cadastrar produto':
                    
                        layoutCadastro = [
                            [cp()]
                        ]

                        janelaCadastro = sg.Window('Tela de Cadastro', layoutCadastro, size=(800, 800), background_color='#94B1B6', font='Arial 16')

                        while True:
                            janelaLayoutInicial.close()
                            event, values = janelaCadastro.read()

                            if event == sg.WINDOW_CLOSED:
                                janelaCadastro.close()
                                break

                            if event == 'Voltar':
                                janelaCadastro.close()
                                loop()

                            if event == 'Cadastrar':

                                c.execute('INSERT INTO medicamento(nome, preço, quantidade, fórmula) VALUES(?, ?, ?, ?)', (values['nome'], values['preco'], values['qtd'], values['formula']))
                                conn.commit()

                                sg.popup('Cadastro realizado !', title='Confirmação')
                                print(f'''{values['nome']}, {values['preco']}, {values['qtd']} ''')

                            if event == 'Consultar':

                                layoutConsulta = [
                                    [sg.Text('Código do produto: ', sg.InputText(key='id'))],
                                    [sg.Table(values=[values['id']], headings=['Código', 'Nome', 'Preço', 'Quantidade'])]
                                ]      

                                janelaConsulta = sg.Window('Consulta de produtos', layoutConsulta)     

                                while True:
                                    event, values = janelaConsulta.read()

                                    if event == sg.WINDOW_CLOSED:
                                        janelaConsulta.close()
                                        break

            loop()
   
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
    conn.close()

loopLogin()