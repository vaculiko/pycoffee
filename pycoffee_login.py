import PySimpleGUI as sg
import hashlib

# GUI Settings
sg.theme('DarkAmber')
size = (20,1)
button_size = (17,1)
# Account username and password hashes are stored in dictionary
# TODO: store in separate file
accounts = {'Aestas' : '44213f9f4d59b557314fadcd233232eebcac8012'}
users = ['Aestas', 'Cruduk', 'Talon', 'Zorin']
login_password_hash = '44213f9f4d59b557314fadcd233232eebcac8012'  # coffee

def PasswordMatches(password, a_hash):
    '''Convert plaintext password to hashed one.'''
    password_utf = password.encode('utf-8')
    sha1hash = hashlib.sha1()
    sha1hash.update(password_utf)
    password_hash = sha1hash.hexdigest()
    return password_hash == a_hash

layout = [[sg.Frame('', layout=[
    [sg.Text('User', s=size)],
    [sg.Input(key='-user-', s=size)],
    [sg.Text('Password', s=size)],
    [sg.Input(key='-password-', s=size, password_char='\u2022')],
    [sg.Text('', key='-status-', s=size)],
    [sg.Button('Login', s=button_size)]], 
    element_justification = 'center', relief=None)
]]

window = sg.Window('Login', layout, #size=(200,200),
                    text_justification='center',
                    grab_anywhere=False)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    user = values['-user-']
    password = values['-password-']
    
    if user in accounts.keys():
        if password and PasswordMatches(password, accounts[user]):
            window.Element('-status-').Update('Login SUCCESSFUL')
        else:
            window.Element('-status-').Update('Login FAILED!!')
    else:
        window.Element('-status-').Update('Username not found.')
        # TODO: add new user

window.close()
        