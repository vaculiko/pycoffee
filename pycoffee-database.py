import random
import pandas as pd
from datetime import date
from pathlib import Path

# Define database columns
cols = ["Datum", "Uživatel", "Země", "Region", "Zpracování", "Pražírna", "Příprava", "Recept", 
        "Známka", "Acidita", "Zemitost", "Intenzita", "Sladkost", "Poznámka"]
# Initialize dataframe 
df = pd.DataFrame(columns=cols)

# Console input for tasting info
def input_tasting():
    row_dict = {}
    for col in cols:
        if col=="Datum":
            row_dict[col] = date.today() # Autofill date
        else:
            row_dict[col] = input(col+": ").title() # Make all inputs start with uppercase
    return row_dict

# Manual input
# new_row = input_tasting() # Generate dictionary
# df = df.append(new_row, ignore_index=True) # Add dictionary as new line to database
# print(df.head())

# Generate random data for visualisation testing
user = ["Aestas", "Cruduk", "Talon", "Zorin"]
country = ["Kenya", "Honduras", "Rwanda", "Ethipoia", "Costa Rica", "Brazil"]
regions = ["Kiranga", "Cadexsa", "Kiyumba", "Dambi Uddo", "Blend", "Palmichal", None]
process = ["Washed", "Natural", "Honey", "Carbon"]
roastery = ["Motmot", "Father's", "Rebelbean", "Laura Coffee", "Naughty dog", "Monogram"]
machine = ["Aeropress", "V60", "Espresso", "Frenchpress", "Moka"]
recipe = ['aaa', 'bbb', 'ccc', None]
data = [date.today(), user, country, regions, process, roastery, machine, recipe]

def random_tasting():
    row_dict = {}
    for i,col in enumerate(cols):
        if i == 0:
            row_dict[col] = str(data[i]) # date
        if 1 <= i <= 7:
            row_dict[col] = random.choice(data[i]) # random text input
        if i > 7:
            row_dict[col] = random.randint(1,5) # random numerical input
        if i == 13:
            row_dict[col] = None # no comment
    return row_dict

# Generate dataset with 50 random rows
for _ in range(51):
    new_row = random_tasting()
    df = df.append(new_row, ignore_index=True) # Add dictionary as new line to database

# Create data directory, if it does not exist
Path('data').mkdir(parents=True, exist_ok=True)
# Export random dataframe to csv
df.to_csv('data/pycoffee-random.csv', index=False)
# Import from csv
test_df = pd.read_csv('data/pycoffee-random.csv')
print(test_df.head(5))

# TODO: data filering examples
