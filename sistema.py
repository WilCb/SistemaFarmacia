import PySimpleGUI as sg
import sqlite3 as bb
from designGrafico import TelaLogin as gtl, CadFuncionario as gcf, TelaADM as telaADM, consulFuncionario as cf, cadastrarProduto as cp
import aspose.words as aw

# Estilo

corDefundo = '#94B1B6'
corFontePadrao = 'black'
corBotaoPadrao = '#0097B2'

def loopLogin():
    # banco de dados

    conn = bb.connect('banco.db')
    c = conn.cursor()
    
    # Layout tela login
    layout = [[gtl()]]
    janelaLayout = sg.Window('Tela de login', layout, size=(600, 400), font='Arial 18', background_color=corDefundo)

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
            
            def loopADM():
                # tela do ADM
                layoutInicialAdm = [[telaADM()]]
                janelaLayoutInicial = sg.Window('Tela inicial', layoutInicialAdm, size=(600, 600), background_color=corDefundo)

                while True:
                    event, values = janelaLayoutInicial.read()

                    if event == sg.WINDOW_CLOSED:
                        janelaLayoutInicial.close()
                        break

                    # Tela de cadastro de funcionários
                    if event == 'Funcionários':
                        janelaLayoutInicial.close()

                        layoutCadFuncionario = [[gcf()]]

                        janelaCadastro = sg.Window('Cadastro', layoutCadFuncionario, size=(800, 800), background_color=corDefundo)

                        while True:

                            event, values = janelaCadastro.read()

                            if event == sg.WINDOW_CLOSED:
                                janelaCadastro.close()
                                break
                            if event == 'Voltar':
                                janelaCadastro.close()
                                loopADM()
                            if event == 'Logout':
                                janelaCadastro.close()
                                loopLogin()

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
                                    c.execute('DELETE FROM funcionarios WHERE Nome = ?', (nameDelete,))
                                    conn.commit()

                                layoutConsulta = [
                                    [cf()],
                                    [sg.Table(values=[values['nome']], headings=['NOME', 'CPF', 'DN', 'CARGO', 'SALÁRIO', 'RUA', 'NÚMERO', 'BAIRRO', 'CIDADE', 'UF'], 
                                            key='table', expand_x=True, justification='c')],
                                    [sg.Button('Excluir'), sg.Button('Voltar')]
                                ]

                                janelaConsulta = sg.Window('Tela de Consulta', layoutConsulta, size=(800, 800), resizable=True)

                                while True:
                                    
                                    event, values = janelaConsulta.read()

                                    if event == sg.WINDOW_CLOSED:
                                        janelaConsulta.close()
                                        break
                                    if event == 'Voltar':
                                        janelaConsulta.close()
                                        loopADM()
                                    
                                    if event == 'Buscar':
                                        
                                        buscaFuncionario = values['nome'].upper()

                                        c.execute('SELECT Nome, CPF, Data_de_nascimento, Cargo, Salário, Rua, Número, Bairro, Cidade, UF FROM funcionarios WHERE UPPER(Nome) = ?', (buscaFuncionario,)) 

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

                    if event == 'Produtos':

                        def deleteFunc(nameDelete):
                            c.execute('DELETE FROM produtos WHERE nome = ?', (nameDelete,))
                            conn.commit()
                    
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
                                loopADM()

                            if event == 'Cadastrar':

                                c.execute('INSERT INTO produtos(nome, preço, quantidade, fórmula) VALUES(?, ?, ?, ?)', (values['nome'], values['preco'], values['qtd'], values['formula']))
                                conn.commit()

                                sg.popup('Cadastro realizado !', title='Confirmação')
                                print(f'''{values['nome']}, {values['preco']}, {values['qtd']} ''')

                            if event == 'Consultar':
                                layout = [
                                    [sg.Text('Consulta')],
                                    [sg.Input(key='nome'), sg.Button('Buscar'), sg.Button('Todos')],
                                    [sg.Table(values=[values['nome']], headings=[['Nome'], ['Preço'], ['Quantidade'], ['Fórmula']], expand_x=True, key='Table', justification='c')],
                                    [sg.Button('Excluir')]
                                ]

                                janela = sg.Window('Tela de consulta', layout, size=(600, 600))

                                while True:
                                    event, values = janela.read()

                                    if event == sg.WIN_CLOSED:
                                        janela.close()
                                        break
                                    if event == 'Buscar':
                                        buscarProduto = values['nome'].upper()
                                        c.execute('SELECT nome, preço, quantidade, fórmula FROM produtos WHERE UPPER(nome) = ?', (buscarProduto,))
                                        res = c.fetchall()
                                        janela['Table'].update(values=res)

                                    if event == 'Todos':
                                        buscarProduto = values['nome'].upper()
                                        c.execute('SELECT nome, preço, quantidade, fórmula FROM produtos')
                                        res = c.fetchall()
                                        janela['Table'].update(values=res)

                                    elif event == 'Excluir':
                                        selected_row = values['Table']
                                        if selected_row:
                                            selected_row_index = selected_row[0]
                                            row_data = res[selected_row_index]
                                            if sg.popup_yes_no('Tem certeza que deseja excluir este registro?', title='Confirmação') == 'Yes':
                                                nameDelete = row_data[0]
                                                deleteFunc(nameDelete)
                                                res.pop(selected_row_index)
                                                janela['Table'].update(values=res)
                                                sg.popup('Excluido !', title='Confirmação')

                    # Gerar relatório
                    if event == 'Relatório':
                        # cria layout da janela de relatorio
                        layoutTexto = [
                            [sg.Text('Deseja gerar relátorio dos produtos?'), sg.InputText(key='nome', visible=False)]
                        ]

                        layoutButton = [
                            [sg.Button('Sim'), sg.Button('Não')]
                        ]

                        layoutRelatorioCentralizado = [
                            [sg.Column(layoutTexto, justification='c')],
                            [sg.Column(layoutButton, justification='c')]
                        ]

                        janelaRelatorio = sg.Window('Relatório de produtos', layoutRelatorioCentralizado, size=(400, 100))

                        while True:
                            event, values = janelaRelatorio.read()

                            if event == sg.WINDOW_CLOSED or event == 'Não':
                                janelaRelatorio.close()
                                break

                            buscarProdutos = values['nome'].upper()
                            c.execute('SELECT * FROM produtos')
                            registro = c.fetchall()

                            if registro:
                                with open('relatório.html', 'w', encoding='utf-8') as f:
                                    f.write("<html><head><meta charset='UTF-8'><style> * {"
                                            "margin: 0;"
                                            "padding: 0;"
                                            "}"
                                            "body {"
                                            "background-color: white;}"
                                            "h1 {"
                                            "text-align: center;"
                                            "}"
                                            ".container {"
                                            "display: flex;"
                                            "justify-content: center;"
                                            "flex-direction: column;"
                                            "}"
                                            "td {"
                                            "padding: 5px;"
                                            "text-align: center;"
                                            "}"
                                            "</style></head><body>")
                                    f.write("<section class='container'><h1>Relatório</h1><table border='1'><tr><th>Nome</th><th>Preço</th><th>Quantidade</th><th>Fórmula</th></tr>")

                                    for row in registro:
                                        f.write(f'<tr><td>{row[1]}</td><td>R$ {row[2]}</td><td>{row[3]}</td><td>{row[4]}</td></tr>')
                                    f.write('</table></section></body></html>')

                                sg.popup('Relatório gerado com sucesso!', title='Relatório de Produtos')
                            else:
                                sg.popup('Produto não encontrado no banco de dados!', title='Relatório de Produtos')

                            buscarProdutos = values['nome'].upper()
                            c.execute('SELECT * FROM produtos WHERE UPPER(nome) = ?', (buscarProdutos,))
                            registro = c.fetchall()

                            if event == 'Sim':
                                doc = aw.Document('relatório.html')
                                doc.save('relatório.pdf')

                                janelaRelatorio.close()
                                break


            loopADM()
   
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