import random
import os
from tkinter.constants import CENTER
import pandas as pd
import PySimpleGUI as sg
from datetime import date
from pathlib import Path

# Define database columns
cols = ["Date", "User", "CountryOrigin", "EstateOrigin", "Processing", "RoastLevel", "Variety", "Roaster", "Preparation", "Recipe"]
#, "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"
username = 'TestGUI'

# Initialize dataframe 
df = pd.DataFrame(columns=cols)


# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Input Definition ------ #
# Aliases for easy resizing
textinput_size = 20,5
sliderinput_size = 10,20

# Text inputs
textinput = [[sg.Input(default_text = "Země", key='CountryOrigin', size=(textinput_size))],
            [sg.Input(default_text = "Region", key='EstateOrigin', size=(textinput_size))],
            [sg.Input(default_text = "Zpracování", key='ProcessingRoastLevel', size=(textinput_size))],
            [sg.Input(default_text = "Pražírna", key='Roaster', size=(textinput_size))],
            [sg.Input(default_text = "Příprava", key='Preparation', size=(textinput_size))],
            [sg.Input(default_text = "Recept", key='Recipe', size=(textinput_size))]]

# Slider inputs
sliderinput = [[sg.Text('Pražení'), sg.Text('Složení')],
          [sg.Text('Tmavé'), sg.Text('Arabica')],
          [sg.Slider(key='RoastLevel', range=(1, 100), orientation='v', size=(sliderinput_size), default_value=50),
          sg.Slider(key='Variant', range=(1, 100), orientation='v', size=(sliderinput_size), default_value=100)],
          [sg.Text('Světlé'), sg.Text('Robusta')]]

# Buttons
buttons = [sg.Button(button_text='Jde se ochutnávat!', tooltip='Kliknutím přejdeš na známkování chuti')]
layout = [[sg.Frame('',[[
          sg.Text('Z čeho a jak vaříme?')],
          [sg.Column(textinput),
          sg.Column(sliderinput)
          ]], element_justification='center')],
        [sg.Column([buttons], justification='center')]]
# Add two potenctiometers/posuvníky for Roast level and for Variant = 100%Arabica-100%Robusta

# Create the window
window = sg.Window("PyCoffee", layout, margins=(60,20))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Jde se ochutnávat!" or event == sg.WIN_CLOSED:
        break

window.close()
print(values)

# "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"

# Console input for tasting info
def input_tasting():
    row_dict = {}
    for col in cols:
        if col=="Date":
           row_dict[col] = date.today() # Autofill date
        elif col=="User":
            row_dict[col] = username # Autofill username
        else:
            # row_dict[col] = input(col+": ").title() # Make all inputs start with uppercase
            row_dict[col] = values[col].title() # Make all inputs start with uppercase
    return row_dict

# Manual input
new_row = input_tasting() # Generate dictionary
df = df.append(new_row, ignore_index=True) # Add dictionary as new line to database

# Create data directory
Path('data').mkdir(parents=True, exist_ok=True)
# Creates file with headers, if it does not exist; if it exists, it appends new data without headers
file = 'data/pycoffee-'+ username +'.csv'
hdr = False if os.path.isfile(file) else True
df.to_csv(file, mode='a', index=False, header=hdr)



print(df)

# Talon tips
# V GUI se výstup z okna ukládá přímo do dictionary, takže když si dobře pojmenuješ jednotlivé vstupy, 
# tak to pak jen příkazem dd.append přidáš do databáze
# Pro input pole v GUI definuješ hodnotu key, která je přímo navázána na dictionary
# Ten je v proměnné 'values' z výstupu funkce window.read()
# Udělej si print(values) a uvidíš 🙂