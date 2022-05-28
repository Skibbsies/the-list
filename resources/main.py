import sys

sys.path.append('../')

from lib import database_utils
from datetime import date
import PySimpleGUI as sg


sg.theme('Black')


layout = [
        [sg.Text('username', size=(15, 1)), sg.InputText(size=(20), key='username-field')],
        [sg.Text('reason', size=(15,1)), sg.InputText(size=(20), key='reason-field')],
        [sg.Text('game', size=(15, 1)), sg.InputText(size=(20), key='game-field')],
        [sg.Radio('current date', 'RADIO1', default=True, enable_events=True, key='current-date'),
            sg.Radio('custom date', 'RADIO1', enable_events=True, key='custom-date')],
        [sg.Text('date yyyy/mm/dd', size=(15, 1)), sg.InputText(size=(20), disabled=True, key='date-field')],
        [sg.Button('add-user'), sg.Button('check-db')]
]


window = sg.Window('The List', layout, keep_on_top=True, location=(5000, 0))


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == 'custom-date':
        window['date-field'].update(disabled=False)
    if event == 'current-date':
        window['date-field'].update(disabled=True)
    if event == 'add-user':
        if values['current-date'] == True:
            values['date-field'] = str(date.today())
            values['date-field'] = values['date-field'].replace('-', '/')
        
        database_utils.AddUser(
                values['username-field'],
                values['reason-field'],
                values['game-field'],
                values['date-field']
        )

        keys_to_clear = [
                window['username-field'],
                window['reason-field'],
                window['game-field'],
                window['date-field']
        ]

        for key in keys_to_clear:
            key.update('')
    if event == 'check-db':
        matches = database_utils.ReadUsers(values)
        sg.popup(matches, any_key_closes=True, auto_close=True, title='Database Matches')


window.close()
