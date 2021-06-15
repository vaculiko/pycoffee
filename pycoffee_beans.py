import pandas as pd
import PySimpleGUI as sg

def beans(user, screen_size=(300, 600)):
    sg.theme('DarkAmber')
    base_font = ('Any 15')
    
    df = pd.read_csv(f'data/pycoffee-{user}.csv',
                     usecols=['Country', 'Name', 'Roaster', 'Processing', 'Variety', 'RoastLevel', 'Type'])
    
    # find last 5 unique brews
    limit = 5
    if df.shape[0] < limit:
        limit = df.shape[0]
    last_beans = [df.iloc[-1].to_dict()] # add last brew
    for i in range(1,df.shape[0]):
        last_row = df.iloc[-i].to_dict()
        current_row = df.iloc[-i-1].to_dict()
        if last_row not in last_beans: # add current brew if it is not found in the list
            last_beans.append(current_row) 
        if len(last_beans) == limit:
            break # end if 
    print(last_beans)
    
    def beanButton(i, row):
        return [sg.Button(button_text=f"{row['Country']}\n{row['Name']}\n{row['Roaster']}",
                         key=f'-bean{i}-', font=base_font, size=(20, 3))]
    
    layout = [
        [beanButton(i, row) for i, row in enumerate(last_beans)],
        [sg.Button(button_text='New beans', key='-new-', font=base_font, size=(20, 1))]
        ]
    
    window = sg.Window('Recent Beans', layout,
                       text_justification='center',
                       element_justification='center',
                       size=screen_size)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            window.close()
            exit()

        if event in [f'-bean{i}-' for i in range(limit)]:
            window.close()
            return last_beans[int(event[-2])]  # info where to switch in main flow

        if event == '-new-':
            window.close()
            return 'tasting'  # info where to switch in main flow

if __name__ == "__main__":
    # execute only if launched from command line/opened directly
    beans(user='random')
