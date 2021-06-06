import pandas as pd
from pandas.core.frame import DataFrame
from pycoffee_login import main as login
from pycoffee_home import main as home
from pycoffee_tasting_input import main as bean
from pycoffee_brewing_input import main as brew
from pycoffee_rating_input import main as rating

'''
Window arrangement
1. login
2. home
3. tasting_input
4. brewing_input
5. rating_input
6. TODO: show_database

TODO: Back button implementation
'''

user = login()
print(user)

select = home(user)
print(select)

if select == 'brew':
    new_row = {}
    new_row.update(bean(user))  # add entries to row dictionary
    new_row.update(brew())
    new_row.update(rating())
    print(new_row)
    # df = DataFrame(new_row)
    # df = df.append(new_row, ignore_index=True)
    print(df)

if select == 'database':
    pass
