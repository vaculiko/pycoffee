import PySimpleGUI as sg
import hashlib

sg.theme('DarkAmber')
size = (20,1)
users = ['Aestas', 'Cruduk', 'Talon', 'Zorin']
login_password_hash = '44213f9f4d59b557314fadcd233232eebcac8012'  # coffee

def PasswordMatches(password, a_hash):
    password_utf = password.encode('utf-8')
    sha1hash = hashlib.sha1()
    sha1hash.update(password_utf)
    password_hash = sha1hash.hexdigest()
    return password_hash == a_hash

layout = [
    [sg.Text('User', key='-usertext-', s=size)],
    [sg.Input(key='-user-', s=size)],
    [sg.Text('Password', s=size)],
    [sg.Input(key='-password-', s=size, password_char='\u2022')],
    [sg.Button('Login')]
]


window = sg.Window('Login', layout, size=(200,200),
                    text_justification='center',
                    grab_anywhere=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    user = values['-user-']
    password = values['-password-']
    
    if user in users:
        if password and PasswordMatches(password, login_password_hash):
            print('Login SUCCESSFUL')
        else:
            print('Login FAILED!!')
    else:
        window.Element('-usertext-').Update('Username not found.')

window.close()
        