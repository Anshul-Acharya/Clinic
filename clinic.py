import mysql.connector
import datetime
import PySimpleGUI as sg


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database='Clinic'
    )

cursor = db.cursor()

#mycursor.execute("select fname from DOCTOR WHERE employeeID=123456799")

#sg.change_look_and_feel('DarkTeal9')
sg.change_look_and_feel('GreenMono')

appointmentID = 0

def popup():
    sg.popup('SUBMITTED')

def receptionist_form():
    sg.change_look_and_feel('LightBrown9')
    
    layout = [  [sg.Text('Add New Patient')],
        [sg.Text("Patient First Name"), sg.Input(key='patientFName'), sg.Text(size=(40,2))],
        [sg.Text("Patient Last Name"), sg.Input(key='patientLName'), sg.Text(size=(40,2))],
        [sg.Text("Patient ID"), sg.Input(key='patientID'), sg.Text(size=(40,2))],
        [sg.Text("Patient Date of Birth"), sg.Input(key='patientDOB'), sg.Text(size=(40,2))],
        [sg.Text("Patient Insurance ID"), sg.Input(key='insuranceID'), sg.Text(size=(40,2))],
        [sg.Text("Nurse ID"), sg.Input(key='nurseID'), sg.Text(size=(40,2))],
        [sg.Text("Doctor ID"), sg.Input(key='doctorID'), sg.Text(size=(40,2))],
        [sg.Text("Current Time"), sg.Input(key='startTime'), sg.Text(size=(40,2))],
        [sg.Text("Reason For Visit"), sg.Input(key='reason'), sg.Text(size=(40,2))],
        [sg.Button('SUBMIT')]
    ]

    # Create the Window
    window = sg.Window('New Patient Form', layout, size=(500,500))
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break
        print("submitted")
        insert_patient = "INSERT INTO PATIENT (fname, lname, patientID, insuranceID)\
            VALUES ('%s', '%s', '%s', '%s')" %\
           (str(values['patientFName']), str(values['patientLName']), str(values['patientID']), str(values['insuranceID']))
        cursor.execute(insert_patient)
        db.commit()
        window.close()
        popup()


#not done
def doctor_form_window():
    
    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Dr blah blah blah examining blah blah')],
        [sg.Text("Appointment ID"), sg.Input(key='apptID'), sg.Text(size=(40,1))],
        [sg.Text("End Time"), sg.Input(key='end_time'), sg.Text(size=(40,1))],
        [sg.Text("Doctor Notes"), sg.Input(key='EID'), sg.Text(size=(40,1))],
        [sg.Text("Diagnosis Code"), sg.Input(key='EID', do_not_clear=False), sg.Text(size=(40,1))],
        [sg.Button('Add Additional Diagnosis'), sg.Button('End Appointment')]
    ]

    # Create the Window
    window = sg.Window('Doctor_Form', layout, size=(500,600))
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        end_visit = "UPDATE APPOINTMENT SET end_time = " + str(values['end_time']) +" WHERE appointmentID = " + str(values['apptID']) + ";"
        print(str(values['end_time']))
        cursor.execute(end_visit)
        db.commit()

        window.close()
        doctor_schedule()

def doctor_schedule():

    schedule_array = [[]]

    headings = ["appointmentID", "fname", "lname", "start_time", "room", "reason_for_visit"]

    schedule = "SELECT appointmentID, fname, lname, start_time, room, reason_for_visit FROM APPOINTMENT WHERE end_time is NULL AND doctorID is NULL;"

    cursor.execute(schedule)
    myResult = cursor.fetchall()

    for i in myResult:
        schedule_array.append(list(i))

    print("shit")

    layout = [
        [sg.Table(values=schedule_array,
            headings=headings, 
            max_col_width=50,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='TABLE',
            row_height=35)],
        [sg.Button('Begin Appointment')]
    ]

    window = sg.Window("Doctor Schedule", layout)

    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        doctor_form_window()
        window.close()

def nurse_schedule():

    schedule_array = [[]]

    headings = ["appointmentID", "fname", "lname", "start_time", "room", "reason_for_visit"]

    schedule = "SELECT appointmentID, fname, lname, start_time, room, reason_for_visit FROM APPOINTMENT WHERE end_time is NULL;"

    cursor.execute(schedule)
    myResult = cursor.fetchall()

    for i in myResult:
        schedule_array.append(list(i))

    print("shit")

    layout = [
        [sg.Table(values=schedule_array,
            headings=headings, 
            max_col_width=50,
            auto_size_columns=True,
            display_row_numbers=True,
            justification='right',
            num_rows=10,
            key='TABLE',
            row_height=35)],
        [sg.Button('Begin Appointment')]
    ]

    window = sg.Window("Nurse Schedule", layout)

    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        nurse_form_window()
        window.close()

#not done
def nurse_form_window():
    
    doctor_array = [[]]

    doctors = "SELECT fname, lname, employeeID FROM DOCTOR;"
    cursor.execute(doctors)
    myResult = cursor.fetchall()

    for i in myResult:
        doctor_array.append(list(i))

    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  
        [sg.Text("Appointment ID"), sg.Input(key='apptID'), sg.Text(size=(40,1))],
        [sg.Text("Assign Doctor"), sg.Combo(doctor_array),sg.Input(key='assignedDoctor')],
        [sg.Text("Height"),  sg.Input(key='apptID'), sg.Text(size=(40,1))],
        [sg.Text("Weight"),  sg.Input(key='apptID'),sg.Text(size=(40,1))],
        [sg.Text("Blood Pressure"),  sg.Input(key='apptID'),sg.Text(size=(40,1))],
        [sg.Text("Nurse's Notes"), sg.Input(key='EID'), sg.Text(size=(40,1))],
        [sg.Button('End Appointment')]
    ]

    # Create the Window
    window = sg.Window('Nurse_Form', layout, size=(500,600))
    # Event Loop to process "events"
    while True:             
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            nurse_schedule()
            break
        nurse_schedule()
        print(str(values['apptID']))
        end_visit = "UPDATE APPOINTMENT SET doctorID = " + str(values['assignedDoctor']) +" WHERE appointmentID = " + str(values['apptID']) + ";"
        cursor.execute(end_visit)
        db.commit()
        window.close()


employee_column = [
    [sg.Text("Login As Doctor")],
    [sg.Input(key='DID', do_not_clear=False)],
    [sg.Text("Login as Nurse")],
    [sg.Input(key='NID', do_not_clear=False)],
    [sg.Text("Login as Receptionist")],
    [sg.Input(key='RID', do_not_clear=False)],
]

patient_column = [
    [sg.Text("Enter Patient Portal")],
    [sg.Input(key='PID')],
    [sg.Button('Ok'), sg.Button('Quit')]
]


    


# Define the window's contents
layout = [
    [
        sg.Column(employee_column),
        sg.VSeperator(),
        sg.Column(patient_column)
    ], [sg.Text(size=(40,1), key='-OUTPUT-')],
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
    
    if values['DID'] != '':
        employee_query = "select fname, lname from DOCTOR WHERE employeeID=" + str(values['DID']) + ";"
        cursor.execute(employee_query)
        myResult = cursor.fetchall()
        if myResult:
            print(myResult)
            window['-OUTPUT-'].update('Welcome Dr: ' + str(myResult))
            doctor_schedule()
        else: 
            window['-OUTPUT-'].update('Invalid Login')
    if values['NID'] != '':
        employee_query = "select fname, lname from NURSE WHERE employeeID=" + str(values['NID']) + ";"
        cursor.execute(employee_query)
        myResult = cursor.fetchall()
        if myResult: 
            print(myResult)
            window['-OUTPUT-'].update('Welcome Nurse:' + str(myResult))
            nurse_schedule()
        else: 
            window['-OUTPUT-'].update('Invalid Login')
    if values['RID'] != '':
        employee_query = "select fname, lname from RECEPTIONIST WHERE employeeID=" + str(values['RID']) + ";"
        cursor.execute(employee_query)
        myResult = cursor.fetchall()
        if myResult:
            print(myResult)
            window['-OUTPUT-'].update('Welcome Receptionist' + str(myResult))
            receptionist_form()
        else: 
            window['-OUTPUT-'].update('Invalid Login')
    if values['PID'] != '':
        patient_query = "select fname, lname from PATIENT WHERE patientID=" + str(values['PID']) + ";"
        cursor.execute(patient_query)
        myResult = cursor.fetchall()
        if myResult:
            print(myResult)
            window['-OUTPUT-'].update('Welcome Valued Patient: ' + str(myResult))
            #patientport goes under
            receptionist_form()
        else: 
            window['-OUTPUT-'].update('Invalid Login')


# Finish up by removing from the screen
window.close()


















