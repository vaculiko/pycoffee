import PySimpleGUI as sg
from pycoffee_login import main as login
from pycoffee_home import main as home
from pycoffee_tasting_input import main as bean

user = login()
print(user)

select = home(user)
print(select) 

if select == 'brew':
    bean_dict = bean(user)
    print(bean_dict)
if select == 'database':
    pass
