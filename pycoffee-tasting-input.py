import random
import os
from tkinter.constants import CENTER
import pandas as pd
import PySimpleGUI as sg
from datetime import date
from pathlib import Path

# ------ Database Definition ------ #
# Entry info: date, user
# Been info: Country, Name, Roaster, Processing, Roast Level, Type, Variety, Brewing Method, Brewing Recipe
cols = ["Date", "User", "Country", "Name", "Roaster", "Processing", "RoastLevel", "Type", "Variety", "BrewingMethod", "BrewingRecipe"]
#, "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"

username = 'TestGUI_2.5'

# Initialize dataframe 
df = pd.DataFrame(columns=cols)


# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Input Definition ------ #
# Aliases for easy resizing
textinput_size = 20,5   # First number is width, second number is high
sliderinput_size = 10,20   # First number is high, second number is width

# Text & spin inputs, separated from sliders for easier column separation in the layout
textinput = [[sg.Input(default_text = "Země - Kenya, Brazil...", key='Country', size=(textinput_size))],
            [sg.Input(default_text = "Jméno - Kiwami, Diamond...", key='Name', size=(textinput_size))],
            [sg.Input(default_text = "Pražírna - Motmot, Father's...", key='Roaster', size=(textinput_size))],
            [sg.Input(default_text = "Zpracování - natural, washed...", key='Processing', size=(textinput_size))],
            [sg.Input(default_text = "Odrůda - Heirloom, Tabi...", key='Variety', size=(textinput_size))],
            [sg.Input(default_text = "Způsob přípravy - espresso, V60...", key='BrewingMethod', size=(textinput_size))],
            [sg.Input(default_text = "Recept příprav - inverted aeropress, ristretto...", key='BrewingRecipe', size=(textinput_size))],
            [sg.Text('Pražení'), # Spin box, selection of values is pre-given by app
            sg.Spin(values=('1 Světlé', '2', '3 Střední', '4', '5 Tmavé'), key='RoastLevel', initial_value='Střední', size=(10,5))]]

# Slider inputs, separated from text & spin for easier column separation in the layout
sliderinput = [[sg.Text('Typ')],
          [sg.Text('100% Arabica')],
          [sg.Slider(key='Type', range=(1, 100), orientation='v', size=(sliderinput_size), default_value=100, disable_number_display=True)],
          [sg.Text('100% Robusta')]]

# Buttons
buttons = [sg.Button(button_text='Jde se ochutnávat!', tooltip='Kliknutím přejdeš na známkování chuti')]

# ------ Layout Definition ------ #
layout = [[sg.Menu(menu_def, tearoff=True)],
          [sg.Frame('',[[
          sg.Text('Informace o zrnu')],
          [sg.Column(textinput),
          sg.Column(sliderinput)
          ]], element_justification='center')],
        [sg.Column([buttons], justification='center')]]

# Create the window
window = sg.Window("PyCoffee", layout, margins=(60,20))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the "Jde se ochutnávat!" button
    if event in ("Jde se ochutnávat!", sg.WIN_CLOSED, 'Exit'):
        break

window.close()
print(values)

# Console input for tasting info
def input_tasting():
    row_dict = {}
    for col in cols:
        if col=="Date":
           row_dict[col] = date.today() # Autofill date
        elif col=="User":
            row_dict[col] = username # Autofill username
        elif col=="Type":
            row_dict[col] = values[col] # Variety has numeric value, it's a float object and cannot be uppercased
        else:
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