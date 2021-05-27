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
cols = ["Date", "User", "Country", "Name", "Roaster", "Processing", "RoastLevel", "Type", "Variety"]
# , "BrewingMethod", "BrewingRecipe"
#, "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"

username = 'TestGUI_2.5'

# Initialize dataframe 
df = pd.DataFrame(columns=cols)


# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Input Definition ------ #
# --- Beans text input aliases for easy formatting --- #
beans_size = (30,1)       # Size of field in characters, First number is width, second number is high
beans_clear = True        # For do_not_clear parameter, False means it will be cleared after ANY event
beans_font = ('Any 15')   # First number is width, second number is high
beans_align = 'center'    # For justification parameter, False means it will be cleared after ANY event
# --- Spin input aliases for easy formatting --- #
spininput_size = (29,1)
# --- Slider input aliases for easy formatting --- #
sliderinput_size = (38,20)   # Size of the actual slider in characters, first number is width, second number is high
slidertext_size = (7,1)      # Size of text above the slider
slidercount_size = (4,1)     # Size of counters of current value on slider

# Buttons
buttons = [sg.Button(button_text='Jde se ochutnávat!', tooltip='Kliknutím přejdeš na známkování chuti', font=beans_font)]

# ------ "Beans" Layout Definition ------ #
layoutBeans = [
    # ---- Menu, for future use, momentarily just for show ---- #
     [sg.Menu(menu_def, tearoff=True)],
    # ---- Fancy frame and title ---- #
    [sg.Frame('',[
     [sg.Text('Zrno', font=beans_font)],
    # ---- Beans origin details ---- #
     [sg.Input(key='Country', default_text = "Země - Kenya, Brazil...", size=beans_size, font=beans_font, justification=beans_align, do_not_clear=beans_clear)],
     [sg.Input(key='Name', default_text = "Jméno - Kiwami, Diamond...", size=beans_size, font=beans_font, justification=beans_align, do_not_clear=beans_clear)],
     [sg.Input(key='Roaster', default_text = "Pražírna - Motmot, Father's...", size=beans_size, font=beans_font, justification=beans_align, do_not_clear=beans_clear)],
     [sg.Input(key='Processing', default_text = "Zpracování - natural, washed...", size=beans_size, font=beans_font, justification=beans_align, do_not_clear=beans_clear)],
     [sg.Input(key='Variety', default_text = "Odrůda - Heirloom, Tabi...", size=beans_size, font=beans_font, justification=beans_align, do_not_clear=beans_clear)],
    # ---- Beans processing details ---- #
    # -- Spin box with roasting levels -- *
     [sg.Spin(
        key='RoastLevel',
        values=[
            '      1 Světlé pražení',
            '      2 Světlejší pražení',
            '      3 Střední pražení',
            '      4 Tmavší pražení',
            '      5 Tmavé pražení'],
        initial_value='      3 Střední pražení',                                  
        size=spininput_size,
        font=beans_font)],
    # -- Slider with Arabica/Robusta ratio -- *
     [sg.Text('0', key='_LEFT_', size=slidercount_size, font=beans_font),                     # Robusta counter
       sg.Text('Robusta', size=slidertext_size, font=beans_font, justification=beans_align),  # Robusta name
       sg.Text('Arabica', size=slidertext_size, font=beans_font, justification=beans_align),  # Arabica name
       sg.Text('100', key='_RIGHT_', size=slidercount_size, font=beans_font)],                # Arabica counter
     [sg.Slider(key='Type', range=(1, 100), orientation='h', disable_number_display=True, default_value=100, font=beans_font, enable_events=True)],
    # ---- Fancy frame ends here ---- #
     ], 
    element_justification='center')],
    # ---- Button to submit and go for the next page ---- #
    [sg.Column([buttons], justification=beans_align)]]

# ------ "Recepy" Layout Definition ------ #
layoutRecepy = [
    [sg.Input(default_text = "Způsob přípravy - espresso, V60...", key='BrewingMethod', size=(30,20))],
            [sg.Input(default_text = "Recept příprav - inverted aeropress, ristretto...", key='BrewingRecipe', size=(30,20))],
            ]


# Create the window
windowBeans = sg.Window("PyCoffee", layoutBeans, margins=(5,5), finalize=True)

# Clearance od default texts in text input fields in Beans windows
windowBeans['Country'].bind('<FocusIn>', '+FOCUS IN+')
windowBeans['Country'].block_focus(block = True)
windowBeans['Name'].bind('<FocusIn>', '+FOCUS IN+')
windowBeans['Roaster'].bind('<FocusIn>', '+FOCUS IN+')
windowBeans['Processing'].bind('<FocusIn>', '+FOCUS IN+')
windowBeans['Variety'].bind('<FocusIn>', '+FOCUS IN+')

# Create an event loop
while True:
    event, values = windowBeans.read()
    print(event,values)
    # If Arabica/Robusta slider is used, modify values of Arabica/Robusta counters, respectively
    if event in ('Type'):
         windowBeans.Element('_LEFT_').Update(100-values['Type'])
         windowBeans.Element('_RIGHT_').Update(values['Type'])
    # Clear default text if the text input field is focused
    if event == 'Country+FOCUS IN+' and values['Country'] == "Země - Kenya, Brazil...":
        windowBeans['Country'].update('')
    if event == 'Name+FOCUS IN+' and values['Name'] == "Jméno - Kiwami, Diamond...":
        windowBeans['Name'].update('')
    if event == 'Roaster+FOCUS IN+' and values['Roaster'] == "Pražírna - Motmot, Father's...":
        windowBeans['Roaster'].update('')
    if event == 'Processing+FOCUS IN+' and values['Processing'] == "Zpracování - natural, washed...":
        windowBeans['Processing'].update('')
    if event == 'Variety+FOCUS IN+' and values['Variety'] == "Odrůda - Heirloom, Tabi...":
        windowBeans['Variety'].update('')    
    # End program if user closes window or presses the "Jde se ochutnávat!" button
    if event in ("Jde se ochutnávat!", sg.WIN_CLOSED, 'Exit'):
        break

windowBeans.close()
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

# Přidat pamatování si předchozích textových inputů, když uživatel rozklikne, nabídne se mu, co psal dříve. Třeba 5 nejčastějších.