import PySimpleGUI as sg

layout = [[sg.Input(default_text = "Země", key='CountryOrigin')],
          [sg.Input(default_text = "Region", key='EstateOrigin')],
          [sg.Input(default_text = "Zpracování", key='ProcessingRoastLevel')],
          [sg.Input(default_text = "Pražírna", key='Roaster')],
          [sg.Input(default_text = "Příprava", key='Preparation')],
          [sg.Input(default_text = "Recept", key='Recipe')],
          [sg.Button("Let's taste!")]]
# Add two potenctiometers/posuvníky for Roast level and for Variant = 100%Arabica-100%Robusta

# Create the window
window = sg.Window("Cisnik", layout, margins=(60,20))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Let's taste!" or event == sg.WIN_CLOSED:
        break

window.close()

# "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"

print(values)