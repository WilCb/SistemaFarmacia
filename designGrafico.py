import PySimpleGUI as sg
from lista import listaUf as estados, listaCidades as cidades, listaCargos as cargos

# Layout tela login

def graficoTelaLogin():

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


# Tela gráfica de cadastro de funcionários

# def graficoNome():
#     formularioNome = [

#         [sg.Text('Dados pessoais', font='Arial 30')],
#         [sg.Text('Nome: ')],
#         [sg.Input(key='nome')]
    
#     ]

#     return formularioNome

# def graficoCPF():
#     formularioCPF = [
#         [sg.Text('CPF')],
#         [sg.Input(key='cpf', size=(13))]
#     ]

#     return formularioCPF

# def graficoDN():
#     formularioDNascimento = [
#         [sg.Text('Data de Nascimento: ')],
#         [sg.CalendarButton('Escolher data', font='Arial 10', format='%d/%m/%y'), 
#         sg.InputText(key='dn', size=(8, 20))]
#     ]

#     return formularioDNascimento

# def graficoEndereco():
#     endereco = [
#         [sg.Text('Endereço', font='Arial 30')],
#         [sg.Text('Rua')],
#         [sg.Input(key='rua'), sg.Text('Número: '), 
#          sg.Input(key='numero', size=(8, 20))],
#         [sg.Text('Bairro')],
#         [sg.Input(key='bairro')],
#         [sg.Text('Cidade: '),
#          sg.OptionMenu(cidades(), ['Selecione'], key='cidade', size=(8, 20)),
#          sg.Text('UF: '),
#          sg.OptionMenu(estados(), ['Selecione'], key='uf', size=(8, 20))]
#     ]
    
#     return endereco

# def GraficoRegistroFuncionario():
#     registro = [
#         [sg.Text('Registro do funcionário', font='Arial 30')],
#         [sg.Text('Cargo: '),
#          sg.OptionMenu(cargos(), ['Selecione'], key='cargo', size=(15, 20)), 
#          sg.Text('Salário: '), sg.InputText(key='salario', size=(15, 20))]
#     ]
    
#     return registro

def GraficoCadFuncionario():

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


# Layout tela ADM

def graficoTelaADM():
    
    layoutInicialAdm = [
        [sg.Button('Cadastrar funcionários'),
        sg.Button('Consulta de funcionários'),
        sg.Button('Deletar de funcionários')],
        [sg.Button('Cadastro de produto'),
        sg.Button('Consulta de produto'),
        sg.Button('Deletar de produto')]        
    ]

    return layoutInicialAdm
