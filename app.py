import PySimpleGUI as sg # type: ignore
from time import sleep

sg.theme('reddit')

# layout

tela_login = [

    [sg.Text('User')],
    # key � o que permite receber informa��o/texto do usu�rio
    [sg.Input(key='user')],
    [sg.Text('Password')],
    # usamos password_char e '*' para o campo de senha n�o aparecer oq o usu�rio digitou
    [sg.Input(password_char='*', key='password')],
    [sg.Button('Submit')],
    [sg.Output(size = (43, 10))]
]

# criar as janelas
janela = sg.Window('Login', layout=tela_login)

# ler os eventos

while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Submit':
        user_u = values['user']
        password_u = values['password']

        print('step 1...done')
        sleep(5)
        print('step 2...done')
        sleep(5)
        print('step 3...done')

