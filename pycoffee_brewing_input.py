from tkinter.constants import CENTER
from types import resolve_bases
from warnings import resetwarnings
import pandas as pd
import PySimpleGUI as sg
from datetime import date
from pathlib import Path

"""
Windows Layout Explanation
--------------------------
Layout consists of graphic elements, input elements and buttons.
Graphic elements are frames and text headers. They look nice, but have zero effect on generated database.
Input elements are all text input fields.

Text inputs utilize two lists of specific variables: keys and default text. They cover data about coffee
beans origins. Where they come from, who roasted them, what they are.
# Fields for text inputs are generated by function <BeansOrigin>, which is run for every <key> and <text>
  from special list [(Key, text),(Key, text),...]. This "special list" is generated for first all entries 
  from lists <keys> and <def_txs>.
# Results are 5 text input fields for each specific key and individual default text is visible in each field.
  Column element is used in layout specification for text input fields, because Frame element has issues
  with generated content. If Frame is ever removed, Column can be removed, too. (Functionality already tested.)

There are currently two buttons:
# Button to submit inputs & continue to the next page.
# Button to returning to the previous page.
--------------------------
ToDo:
# Podmínka pro vytvoření/nevytvoření Headerů, pokud soubor headery neobsahuje/obsahuje (soubor vždy existuje)
# Přidat pamatování si předchozích textových inputů, když uživatel rozklikne, nabídne se mu, co psal dříve. Třeba 5 nejčastějších.
# Vyrobit akci na tlačítku Zpět :D
# Hezká grafika
"""

cols = ["BrewingMethod", "BrewingRecipe"] 
df = pd.DataFrame(columns=cols)  # Initialize dataframe

username = 'TestGUI_3.6'

# ------ Menu Definition ------ #
menu_def = [['&Account', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&History', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Global definitions ------ #
sg.theme('DarkAmber')
base_font = ('Any 15')
base_align = 'center'   # For justification parameter = horizontal alignment of elements

# ---- Function for generating text inputs & enabling of easy formatting for Beans Origin section ---- #
def BrewingSpecs(key_sp, def_text):
    return [sg.Input(key=key_sp,
                     default_text=def_text,
                     tooltip=def_text[:def_text.index(' ')],
                     size=(30, 1),              # Size of the text input field
                     font=('Any 15'),
                     justification='center',     # Alignment of text in the input field
                     pad=((0,0),(10,10)),
                     border_width=10)]

# -- Lists of keys and defaults text for text input fields for Beans Origin section -- #
keys=['BrewingMethod','BrewingRecipe']
def_txs=["Příprava – espresso, V60, Aeropress...",
         "Postup - inverted aeropress, ristretto, 40:60 dripper..."]


# Buttons
buttons = [[sg.Button(button_text='Jde se ochutnávat!', key='Next', auto_size_button=None,
                     tooltip='Kliknutím přejdeš na známkování chuti', font=('Any 24'),
                     mouseover_colors=('sienna1','OrangeRed4') )],
           [sg.Button(button_text='Zpět', bind_return_key=True, key='Back',
                     tooltip='Kliknutím se vrátíš na login', font=base_font,
                     mouseover_colors=('sienna1','OrangeRed4'))]]

# ------ "Brewing" Layout Definition ------ #
layoutBrew = [
    # ---- Menu, for future use, momentarily just for show ---- #
    [sg.Menu(menu_def, tearoff=True)],
    
    # ---- Fancy frame and title ---- #
    [sg.Frame('', layout=[
     [sg.Text('Příprava', font=base_font)],
     
     # ---- Generated "Beans Origin" text input fields: ---- #
     [sg.Column(layout=[BrewingSpecs(key_sp,def_text) for key_sp,def_text in [(keys[i],def_txs[i]) for i in range(len(keys))]])],
                      
     # ---- Fancy frame ends here ---- #
     ], element_justification='center')],
    
    # ---- Buttons to submit and go for the next page OR return back---- #
    [sg.Column(buttons, justification=base_align, key='ColumnButtons', element_justification=base_align)]]


# ------ Create the window ------ #
windowBrew = sg.Window("PyCoffee", layoutBrew, margins=(
    5, 5), no_titlebar=False, finalize=True)

# ------ Focus Event Binding from Thinker on PySimpleGUI "Beans Origins" text inputs ------ #
# Blocks any Focus on the window opening, so the first click also clears default text
windowBrew[keys[0]].block_focus(block=True)
# Binds generating of Focus Events on text input fields created from list <keys>
[windowBrew[key].bind('<FocusIn>', '+FOCUS IN+') for key in keys]

# ------ Expands Elements to fit the width of window ------ #
[windowBrew[key].expand(expand_x = True) for key in keys + ['ColumnButtons','Next','Back']]


# ------ Create an event loop ------ #
'''
'Clear' For Loop Explanation
-----------------
<For loop> is used to check if any text input field was focused (selected by user).
For every text input field there is a <key> matching entry from the list <keys>.
For every text input field there is also <default text> in the text input field 
(returned as <value> by window.read function) and it matches entry from the list
<def_txs> on the same position as <key> in <keys>.
    # E.g. on the first position of <keys> there is 'BrewingMethod', on first pozition of 
    <def_txs> there is "Příprava – espresso, V60, Aeropress...".
    So the text input field with <key> 'BrewingMethod' contains <default text> "Příprava – espresso, V60, Aeropress...".

<For loop> checks if for any <key> from <keys> the Focus Event was created (syntax is 
<key+'+FOCUS IN+'> and it is generated by Focus Event Binding code above).
    # If such Focus event was created (user klicked on thetext input field) and <value> of 
      <key> (the text of the input field) matches entry from <def_txs> on the same position
      (matches default text given by code), that value (default text) is deleted.
-----------------
'''
while True:
    event, values = windowBrew.read()
    # -- Clear default text of the text input field on Focus -- #
    for key in keys:      
        if event == (key+'+FOCUS IN+') and values[key] == def_txs[keys.index(key)]:       
            windowBrew[key].update('')       
    # -- If User presses the "Jde se ochutnávat!" button, open next Windows -- #
    if event in ('Next'):
        print(values)
        break
    # -- End program if User closes window -- #
    if event in (sg.WIN_CLOSED, 'Exit', 'Back'):
        break

windowBrew.close()


# ------ Console input for tasting info ------ #
def input_tasting():
    row_dict = {}
    for col in cols:
        row_dict[col] = values[col].title()
    return row_dict


# ------ Manual input ------ #
# -- Generate dictionary and add it as new line to database-- #
new_row = input_tasting()
df = df.append(new_row, ignore_index=True)
# -- Create data directory -- #
Path('data').mkdir(parents=True, exist_ok=True)
# -- Create database file with headers -- #
# -- If database file already exists, append new data without headers #
file = 'data/pycoffee-' + username + '.csv'
hdr = False if file else True
df.to_csv(file, mode='a', index=False, header=hdr)
print(df)