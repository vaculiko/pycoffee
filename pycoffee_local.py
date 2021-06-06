import pandas as pd
from pycoffee_login import main as login
from pycoffee_home import main as home
from pycoffee_tasting_input import main as bean
from pycoffee_brewing_input import main as brew
from pycoffee_rating_input import main as rating

'''
Window order
1. login
2. home
3. tasting_input
4. brewing_input
5. rating_input
6. TODO: show_database

TODO: Back button implementation
'''
# login screen
user = login()
# home screen with info
select = home(user)

if select == 'brew':
    new_row = {} # empty dict to hold all tasting info
    # Go through all windows and save output to dict
    new_row.update(bean(user))  # .update() adds entries to row dictionary
    new_row.update(brew())
    new_row.update(rating())
    
    # Load only database columns, no data
    df = pd.read_csv(f'data/pycoffee-{user}.csv', header=0, index_col=False).head(0)
    # add new_row to empty dataframe with correct column name and order
    df = df.append(new_row, ignore_index=True)
    # choose databse based on username
    file = 'data/pycoffee-' + user + '.csv'
    # append new_row of tasting to user database
    df.to_csv(file, mode='a', index=False, header=False)
    print(df)

if select == 'database':
    pass
