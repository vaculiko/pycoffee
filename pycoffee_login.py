import PySimpleGUI as sg
import pandas as pd
import hashlib

def main(screen_size=(300, 600)):
    # GUI Settings
    sg.theme('DarkAmber')
    base_font = ('Any 15')
    size = (20, 1)
    button_size = (17, 1)
    # Account username and password hashes are stored in csv file
    # csv is imported and converted to dictionary, where
    # key = user, value = hash
    accounts = pd.read_csv('data/accounts.csv', header=0,
                        index_col=0, squeeze=True).to_dict()
    # Limiting attempts for user login
    attempts = 0
    limit = 3


    def PasswordMatches(password, a_hash):
        '''Convert plaintext password to hashed one.'''
        password_utf = password.encode('utf-8')
        sha1hash = hashlib.sha1()
        sha1hash.update(password_utf)
        password_hash = sha1hash.hexdigest()
        return password_hash == a_hash


    layout = [[sg.Column(layout=[
        [sg.Text('User', size=size, font=base_font)],
        [sg.Input(key='-user-', size=size, font=base_font)],
        [sg.Text('Password', size=size, font=base_font)],
        [sg.Input(key='-password-', size=size,
                font=base_font, password_char='\u2022')],
        [sg.Text('', key='-status-', size=size, font=base_font)],
        [sg.Button('Login', size=button_size, font=base_font, bind_return_key=True)]],
        element_justification='center')
    ]]

    window = sg.Window('Login', layout,
                    text_justification='center',
                    element_justification='center',
                    grab_anywhere=False,
                    size=screen_size)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            exit()

        # Evaluate only after 'Login' button press
        if event == 'Login':
            user = values['-user-']
            password = values['-password-']

            # if username present and found in dictionary
            if user in accounts.keys():
                # if password hashes match
                if password and PasswordMatches(password, accounts[user]):
                    print('Login SUCCESSFUL!')
                    window.close()
                    return user
                # if password hashes do not match
                else:
                    window.Element('-status-').Update('Wrong password.')
                    attempts += 1
            # when user not found in dictionary
            else:
                window.Element('-status-').Update('Username not found.')
                attempts += 1
                # TODO: add new user routine
            # warn user when close to the login attempt limit
            if attempts == limit:
                window.Element('-status-').Update('Last attempt!')
            # disable login button after too many login attempts
            if attempts > limit:
                window.Element('-status-').Update(visible=False)
                window.Element('Login').Update(visible=False)
                window.close()
                exit()
                
if __name__ == "__main__":
    # execute only if launched from command line/opened directly
    main()
