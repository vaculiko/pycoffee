import PySimpleGUI as sg
import pandas as pd

# define main function, can be used outside this script
def main(user = 'random'):
    # import user database
    df = pd.read_csv(f'data/pycoffee-{user}.csv', header=0, index_col=0)
    total = df.shape[0] # number of brewed cups
    last_brew = df.tail(1) # details of last brew

    sg.theme('DarkAmber')
    base_font = ('Any 15')

    layout = [[sg.Column(layout=[
        [sg.Text(f"Vítejte {user}!", font=base_font)],
        [sg.Text(
            f"Naši uživatelé uvařili celkem {df.shape[0]} šálků kávy.", font=base_font)],
        [sg.Text(
            f"Poslední šálek uvařil {last_brew['User'][0]} dne {last_brew.index[0]}.", font=base_font)],
        [sg.Button('Jde se vařit', key='-brew-')],
        [sg.Button('Ukaž databázi', key='-database-')]
    ], element_justification='center')
    ]]

    window = sg.Window('Home', layout,
                       text_justification='center')

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            exit()
        
        if event == '-brew-':
            window.close()
            return 'brew' # info where to switch in main flow
        
        if event == '-database-':
            window.close()
            return 'database' # info where to switch in main flow


if __name__ == "__main__":
    # execute only if launched from command line/opened directly
    main()
