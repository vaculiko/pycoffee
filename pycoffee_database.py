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
data = [user, country, regions, process, roastery, machine, recipe]
random.seed(42)

def random_tasting():
    row_dict = {}
    for i,col in enumerate(cols):
        if i == 0:
            row_dict[col] = str(date.today()) # date
        if 1 <= i <= 7:
            row_dict[col] = random.choice(data[i-1]) # random text input
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
print(test_df.head(5)) # print only first 5 rows
print('\n--------------------')
print('Select column(s) by label\n')
print(test_df['Příprava'].head(5))
print(test_df[['Uživatel', 'Známka']].head(5))
print('\n--------------------')
print('Select columns by data type\n')
print(test_df.dtypes)
print(test_df.select_dtypes(include='int64', exclude=None).head(5))
print('\n--------------------')
print('Select rows using boolean operators\n')
print(test_df[test_df['Uživatel'] == 'Aestas'].head(5))
print(test_df[(test_df['Uživatel'] == 'Cruduk') & 
              (test_df['Pražírna'] == 'Laura Coffee')])
print(test_df[test_df['Známka'] <= 2].head(5))
