import mysql.connector
import PySimpleGUI as sg


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='Clinic'
    )

cursor = db.cursor()

#mycursor.execute("select fname from DOCTOR WHERE employeeID=123456799")

#sg.change_look_and_feel('LightBrown9')
#sg.change_look_and_feel('BrownBlue')
sg.change_look_and_feel('DarkTeal9')

def doctor_form_window():
    sg.change_look_and_feel('LightBrown9')
    layout = [
        [sg.Text("Enter Employee Portal")]
    ]

    window = sg.Window('Doctor Evaluation Form', layout, modal=True)
    print("yeys")
    window.close()
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Some text on Row 1')],
        [sg.Text('Enter something on Row 2'), sg.InputText()],
        [sg.OK(), sg.Cancel()]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

    window.close()


employee_column = [
    [sg.Text("Enter Employee Portal")],
    [sg.Input(key='EID')],
    [sg.Text(size=(40,1), key='-OUTPUT-')]
]

patient_column = [
    [sg.Text("Enter Patient Portal")],
    [sg.Input(key='PID')],
    [sg.Text(size=(40,1), key='-OUTPUT-')]
]

# Define the window's contents
layout = [
    [
        sg.Column(employee_column),
        sg.VSeperator(),
        sg.Column(patient_column)
    ],
    [sg.Button('Ok'), sg.Button('Quit')]
]

# Create the window
window = sg.Window('LOGIN', layout, margins=(20,100))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    employee_query = "select fname, lname from DOCTOR WHERE employeeID=" + str(values['EID']) + ";"
    cursor.execute(employee_query)
    myResult = cursor.fetchall()
    print(myResult)
    window['-OUTPUT-'].update('Welcome Dr ' + str(myResult))
    doctor_form_window()



# Finish up by removing from the screen
window.close()


















