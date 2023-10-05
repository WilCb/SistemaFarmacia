import PySimpleGUI as sg
from lista import listaUf as estados, listaCidades as cidades, listaCargos as cargos

# Estilo

corDefundo = '#94B1B6'
corFontePadrao = 'black'
corBotaoPadrao = '#0097B2'


# Layout tela login
def TelaLogin():

    titulo = [
        [sg.Text('Bem vindo', font='Arial 30', text_color=corFontePadrao, background_color=corDefundo)],
        [sg.Text('', background_color=corDefundo)]
    ]

    formularioLogin = [
        [sg.Text('Usuário: ', font='arial 13', text_color=corFontePadrao, background_color=corDefundo)],
        [sg.InputText(key='usuario', size=(10))],
        [sg.Text('Senha: ', font='arial 13', text_color=corFontePadrao, background_color=corDefundo)],
        [sg.InputText(key='senha', password_char='*', size=(10))],
        [sg.Button('Entrar', font='arial 13', button_color=corBotaoPadrao, size=(7)), sg.Button('Sair', font='arial 13', button_color=corBotaoPadrao, size=(5))]
    ]

    layout = [
        [sg.Column(titulo, justification='c', background_color=corDefundo)],
        [sg.Column(formularioLogin, justification='c', background_color=corDefundo)]
    ]

    return layout

# Layout tela ADM
def TelaADM():

    menu = [
            ['Menu',['Trocar usuário', 'Logout']]
        ]
    
    titulo = [
        [sg.Text('Tela ADM', font=(corFontePadrao, 25), background_color=corDefundo)],
        [sg.Text('', background_color=corDefundo)]
    ]
    btns = [
        [sg.Menu(menu)],
        [sg.Column(titulo, justification='c', background_color=corDefundo)],
        [sg.Button('Funcionários', button_color=corBotaoPadrao, size=(20, 5)), sg.Button('Produtos', button_color=corBotaoPadrao, size=(20, 5))],
        [sg.Button('Relatório', button_color=corBotaoPadrao, size=(20, 5)), sg.Button('Gráfico', button_color=corBotaoPadrao, size=(20, 5))]
    ]

    centroLayout = [
        [sg.Column(btns, justification='c', background_color=corDefundo)]
    ]

    return centroLayout

# Tela gráfica de cadastro de funcionários
def CadFuncionario():
    # Menu para troca de usuário e logout para fechar o sistema
    menu = [
            ['Menu',['Trocar usuário', 'Logout']]
        ]
    # Parte dos dados pessoais
    tituloDadosPessoais = [
        [sg.Text('Dados pessoais', font='Arial 30', background_color=corDefundo)],
        [sg.Text('', background_color=corDefundo)]
    ]
    formularioNome = [

        [sg.Column(tituloDadosPessoais, justification='c', background_color=corDefundo)],
        [sg.Text('Nome: ', background_color=corDefundo)],
        [sg.Input(key='nome')]
    
    ]

    formularioCPF = [
        [sg.Text('CPF', background_color=corDefundo)],
        [sg.Input(key='cpf', size=(13))]
    ]

    formularioDNascimento = [
        [sg.Text('Data de Nascimento: ', background_color=corDefundo)],
        [sg.CalendarButton('Escolher data', font='Arial 10', format='%d/%m/%y', button_color=corBotaoPadrao, size=(20)),
         sg.InputText(key='dn', size=(8, 20))]
    ]
    # informações do endereço

    tituloEndereco = [
        [sg.Text('Endereço', font='Arial 30', background_color=corDefundo)],
        [sg.Text('', background_color=corDefundo)]
    ]
    endereco = [
        [sg.Column(tituloEndereco, justification='c', background_color=corDefundo)],
        [sg.Text('Rua', background_color=corDefundo)],
        [sg.Input(key='rua'), sg.Text('Número: ', background_color=corDefundo), 
         sg.Input(key='numero', size=(8, 20))],
        [sg.Text('Bairro', background_color=corDefundo)],
        [sg.Input(key='bairro')],
        [sg.Text('Cidade: ', background_color=corDefundo),
         sg.OptionMenu(cidades(), ['Selecione'], key='cidade', size=(8, 20)),
         sg.Text('UF: ', background_color=corDefundo),
         sg.OptionMenu(estados(), ['Selecione'], key='uf', size=(8, 20))]
    ]

    # informações do cargo

    tituloCargo = [
        [sg.Text('Informações do cargo', font='Arial 30', background_color=corDefundo)],
        [sg.Text('', background_color=corDefundo)]
    ]

    registro = [
        [sg.Column(tituloCargo, justification='c', background_color=corDefundo)],
        [sg.Text('Cargo: ', background_color=corDefundo),
         sg.OptionMenu(cargos(), ['Selecione'], key='cargo', size=(15, 20)), 
         sg.Text('Salário: ', background_color=corDefundo), sg.InputText(key='salario', size=(15, 20))]
    ]
    
    btns = [
        [sg.Text('', background_color=corDefundo)],
        [sg.Button('Cadastrar', button_color=corBotaoPadrao, size=(20)),
         sg.Button('Lista de funcionários', button_color=corBotaoPadrao, size=(20)),
         sg.Button('Voltar', button_color=corBotaoPadrao, size=(20))]
    ]

    layoutCadFuncionario = [
        
        [sg.Menu(menu)],
        [formularioNome],
        [sg.Column(formularioCPF, background_color=corDefundo),
         sg.Column(formularioDNascimento, background_color=corDefundo)],
        [endereco],
        [registro],
        [sg.Column(btns, justification='c', background_color=corDefundo)]
                    
    ]

    return layoutCadFuncionario



def consulFuncionario():

    layoutCosulta = [
        [sg.Text('Nome'), sg.InputText(key='nome')],
        [sg.Button('Buscar')]
    ]

    return layoutCosulta

#Cadastrar produto
def cadastrarProduto():

    titulo = [
        [sg.Text('Cadastro de Produtos', background_color=corDefundo, text_color=corFontePadrao, font='Arial 32')]
    ]
    formularioCadastro = [
        [sg.Text('Nome:  ', background_color=corDefundo, text_color=corFontePadrao), sg.InputText(key='nome', size=(20))],
        [sg.Text('Preço:  ', background_color=corDefundo, text_color=corFontePadrao), sg.InputText(key='preco', size=(20))],
        [sg.Text('Qtd.:     ', background_color=corDefundo, text_color=corFontePadrao), sg.InputText(key='qtd', size=(20))],
        [sg.Text('Fórmula:', background_color=corDefundo, text_color=corFontePadrao),sg.OptionMenu(['Original', 'Genérico'], '', key='formula')]
    ]
    btn = [
        [sg.Button('Cadastrar', button_color=corBotaoPadrao, size=(8, 0)), sg.Button('Consultar', button_color=corBotaoPadrao), sg.Button('Voltar', button_color=corBotaoPadrao)]
    ]

    layoutCadastro = [
        [sg.Column(titulo, justification='c', background_color=corDefundo)],
        [sg.Column(formularioCadastro, justification='c', background_color=corDefundo)],
        [sg.Column(btn, justification='c', background_color=corDefundo)]
    ]

    return layoutCadastro