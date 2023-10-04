import PySimpleGUI as sg
from lista import listaUf as estados, listaCidades as cidades, listaCargos as cargos

# Estilo

corDefundo = '#94B1B6'
corFontePadrao = 'black'
corBotaoPadrao = '#dbacac'


# Layout tela login
def TelaLogin():

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

    return layout

# Layout tela ADM
def TelaADM():

    menu = [
            ['Menu',['Trocar usuário', 'Logout']]
        ]
    
    layoutInicialAdm = [
        [sg.Menu(menu)],
        [sg.Button('Cadastrar funcionários', size=(20, 5)),
        sg.Button('Lista de funcionários', size=(20, 5)),
        sg.Button('Deletar funcionário', size=(20, 5))],
        [sg.Button('Cadastrar produto', size=(20, 5)),
        sg.Button('Lista de produtos', size=(20, 5)),
        sg.Button('Deletar produto', size=(20, 5))]        
    ]

    centroLayout = [
        [sg.Column(layoutInicialAdm, justification='c')]
    ]

    return centroLayout

# Tela gráfica de cadastro de funcionários
def CadFuncionario():
    # Menu para troca de usuário e logout para fechar o sistema
    menu = [
            ['Menu',['Trocar usuário', 'Logout']]
        ]

    formularioNome = [

        [sg.Text('Dados pessoais', font='Arial 30')],
        [sg.Text('Nome: ')],
        [sg.Input(key='nome')]
    
    ]

    formularioCPF = [
        [sg.Text('CPF')],
        [sg.Input(key='cpf', size=(13))]
    ]

    formularioDNascimento = [
        [sg.Text('Data de Nascimento: ')],
        [sg.CalendarButton('Escolher data', font='Arial 10', format='%d/%m/%y'),
         sg.InputText(key='dn', size=(8, 20))]
    ]

    endereco = [
        [sg.Text('Endereço', font='Arial 30')],
        [sg.Text('Rua')],
        [sg.Input(key='rua'), sg.Text('Número: '), 
         sg.Input(key='numero', size=(8, 20))],
        [sg.Text('Bairro')],
        [sg.Input(key='bairro')],
        [sg.Text('Cidade: '),
         sg.OptionMenu(cidades(), ['Selecione'], key='cidade', size=(8, 20)),
         sg.Text('UF: '),
         sg.OptionMenu(estados(), ['Selecione'], key='uf', size=(8, 20))]
    ]

    registro = [
        [sg.Text('Registro do funcionário', font='Arial 30')],
        [sg.Text('Cargo: '),
         sg.OptionMenu(cargos(), ['Selecione'], key='cargo', size=(15, 20)), 
         sg.Text('Salário: '), sg.InputText(key='salario', size=(15, 20))]
    ]
    
    layoutCadFuncionario = [
        
        [sg.Menu(menu)],
        [formularioNome],
        [sg.Column(formularioCPF),
         sg.Column(formularioDNascimento)],
        [endereco],
        [registro],
        [sg.Button('Cadastrar'),
         sg.Button('Lista de funcionários'),
         sg.Button('Voltar')]
                    
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