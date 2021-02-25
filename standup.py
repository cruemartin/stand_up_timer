#this is progam to remind me to stand up for 15 mins of every hour 

import PySimpleGUI as sg
import time as t
import constants as const
import datetime as dt

print("Running...")

# t.sleep(5)
t.sleep(const.FIVE_MINUTES)

# print('before loop')
while True:


    #check that it is not after 5 
    now = dt.datetime.now()
    hr = now.hour

    print(now)

    print('hour: %d' % (hr))

    if int(hr) >= 17: 
        break

    layout_1 = [
            [sg.Text('Time to Stand up for 15 mins')],
            [sg.Button('OK'), sg.Button('Cancel')]
    ]

    layout_2 = [ 
            [sg.Text('Ok time to sit back down')],
            [sg.Button('OK'), sg.Button('Cancel')]
    ]

    window = sg.Window('Stand Up!', layout_1, size=(250,70))

    event, values = window.read()

    # print('Before if statement')
    
    if event == 'OK':
        window.close()

    elif event == sg.WIN_CLOSED or event == 'Cancel': #if user closes the window or clicks cancel button
        break

    # print('after if statement') 

    # t.sleep(15)
    t.sleep(const.FIFTEEN_MINUTES)

    window = sg.Window('Sit Down!', layout_2, size=(500,100))

    event, values = window.read()

    # print('Before if statement')

    if event == 'OK':
        window.close()

    elif event == sg.WIN_CLOSED or event == 'Cancel': #if user closes the window or clicks cancel button
        break

    # print('after if statement')

    # t.sleep(30)
    t.sleep(const.FORTYFIVE_MINUTES)

print('Exiting...')