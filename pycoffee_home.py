import pandas as pd
import PySimpleGUI as sg


# define main function, can be used outside this script
def main(user, screen_size=(300, 600)):
    # import user database
    users = pd.read_csv('data/accounts.csv')['user'].tolist()
    # Pull info about brews (user, date) from all users and make it smart (load only needed columns)
    df_list = [pd.read_csv(
        f'data/pycoffee-{u}.csv', usecols=['User', 'Date']) for u in users]
    df = pd.concat(df_list, ignore_index=True)
    total = df.shape[0]  # number of brewed cups
    last_brew = df.iloc[-1]  # details of last brew
    if last_brew.empty:  # prevent crashing if user has no brews
        last_brew['User'] = ['---']
        last_brew['Date'] = ['---']
    sg.theme('DarkAmber')
    base_font = ('Any 15')

    layout = [[sg.Column(layout=[
        [sg.Text(f"Vítejte {user}!", font=base_font, size=(20, 5))],
        [sg.Text(
            f"Naši uživatelé uvařili celkem {total} šálků kávy.", font=base_font, size=(20, 5))],
        [sg.Text(
            f"Poslední šálek uvařil {last_brew['User']} dne {last_brew['Date']}.", font=base_font, size=(20, 5))],
        [sg.Button('Jde se vařit', key='-brew-',
                   font=base_font, size=(20, 1))],
        [sg.Button('Ukaž databázi', key='-database-',
                   font=base_font, size=(20, 1))]
    ], element_justification='center')
    ]]

    window = sg.Window('Home', layout,
                       text_justification='center',
                       element_justification='center',
                       size=screen_size)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            exit()

        if event == '-brew-':
            window.close()
            return 'brew'  # info where to switch in main flow

        if event == '-database-':
            window.close()
            return 'database'  # info where to switch in main flow


if __name__ == "__main__":
    # execute only if launched from command line/opened directly
    main(user='Aestas')
