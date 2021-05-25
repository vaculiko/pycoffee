import random
import os
import pandas as pd
from datetime import date
from pathlib import Path

# Define database columns
cols = ["Datum", "Uživatel", "Země", "Region", "Zpracování", "Pražírna", "Příprava", "Recept", 
        "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"]

username = 'Test'

# Initialize dataframe 
df = pd.DataFrame(columns=cols)

# Console input for tasting info
def input_tasting():
    row_dict = {}
    for col in cols:
        if col=="Datum":
           row_dict[col] = date.today() # Autofill date
        elif col=="Uživatel":
            row_dict[col] = username # Autofill username
        else:
            row_dict[col] = input(col+": ").title() # Make all inputs start with uppercase
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

