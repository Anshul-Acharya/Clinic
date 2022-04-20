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
ID = 0
i = 0

#mycursor.execute("select fname from DOCTOR WHERE employeeID=123456799")

#sg.change_look_and_feel('DarkTeal9')
sg.change_look_and_feel('GreenMono')

appointmentID = 0

def popup():
    sg.popup('SUBMITTED')

def receptionist_form():
    
    layout = [  [sg.Text('Add New Patient')],
        [sg.Text("Patient First Name"), sg.Input(key='patientFName'), sg.Text(size=(40,2))],
        [sg.Text("Patient Last Name"), sg.Input(key='patientLName'), sg.Text(size=(40,2))],
        [sg.Text("Patient Date of Birth"), sg.Input(key='patientDOB'), sg.Text(size=(40,2))],
        [sg.Text("Patient Insurance ID"), sg.Input(key='insuranceID'), sg.Text(size=(40,2))],
        [sg.Text("Room"), sg.Input(key='room'), sg.Text(size=(40,2))],
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

        insert_patient = "INSERT INTO PATIENT (fname, lname, insuranceID)\
            VALUES ('%s', '%s', '%s')" %\
           (str(values['patientFName']), str(values['patientLName']), str(values['insuranceID']))
        cursor.execute(insert_patient)

        find_appt = "select MAX(patientID) FROM PATIENT"
        cursor.execute(find_appt)
        myResult = cursor.fetchone()
        
        insert_appt = "INSERT INTO APPOINTMENT (fname, lname, patientID, start_time, room, reason_for_visit)\
            VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" %\
           (str(values['patientFName']), str(values['patientLName']), str(myResult[0]), str(values['startTime']), str(values['room']), str(values['reason']))
        cursor.execute(insert_appt)


        db.commit()
        window.close()
        popup()


#not done
def doctor_form_window():
    

    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  [sg.Text('Dr blah blah blah examining blah blah')],
        [sg.Text("Appointment ID"), sg.Input(key='apptID'), sg.Text(size=(40,1))],
        [sg.Text("End Time"), sg.Input(key='end_time'), sg.Text(size=(40,1))],
        [sg.Text("Doctor Notes"), sg.Input(key='drNotes', do_not_clear=False), sg.Text(size=(40,1))],
        [sg.Text("Diagnosis Code"), sg.Input(key='dcode', do_not_clear=False), sg.Text(size=(40,1))],
        [sg.Text("Medication Code"), sg.Input(key='meds', do_not_clear=False), sg.Text(size=(40,1))],
        [sg.Button('Add Diagnosis/Medication'),sg.Button('Submit')],
        [sg.Text("Dr Signature"), sg.Checkbox('')]
    ]

    # Create the Window
    dry_window = sg.Window('Doctor_Form', layout, size=(500,600))
    # Event Loop to process "events"
    while True:             
        event, values = dry_window.read()
        if event == sg.WINDOW_CLOSED:
            break

        if event == 'Submit':
            end_visit = "UPDATE APPOINTMENT SET end_time = " + str(values['end_time']) +" WHERE appointmentID = " + str(values['apptID']) + ";"
            cursor.execute(end_visit)
            db.commit()
            dry_window.close()
            doctor_schedule()
        if event == 'Add Diagnosis/Medication':

            
            insert_diagnosis = "INSERT INTO APPOINTMENT_DIAGNOSIS (appointmentID, doctor_notes)\
                VALUES ('%s', '%s')" %\
                (str(values['apptID']), str(values['drNotes']))

            cursor.execute(insert_diagnosis)
            
            sis = "SELECT max(appt_diagnosis_code) FROM APPOINTMENT_DIAGNOSIS;"
            cursor.execute(sis)
            myResult = cursor.fetchone()



            insert_diagnosis_med = "INSERT INTO APPOINTMENT_DIAGNOSIS_MEDICATION (appointmentID, diagnosis_code, medication_code)\
                VALUES ('%s', '%s', '%s')" %\
                (str(values['apptID']), myResult[0], str(values['meds']))
            
            cursor.execute(insert_diagnosis_med)
            db.commit()

        

def doctor_schedule():

    schedule_array = [[]]

    headings = ["appointmentID", "fname", "lname", "start_time", "room", "reason_for_visit", "Nurse's Notes"]


    schedule = "SELECT a.appointmentID, a.fname, a.lname, a.start_time, a.room, a.reason_for_visit, a.nurse_notes \
        FROM APPOINTMENT a INNER JOIN DOCTOR d ON employeeID=" + ID + " AND d.employeeID=a.doctorID WHERE end_time is NULL;"
    db.commit()

    cursor.execute(schedule)
    myResult = cursor.fetchall()

    for i in myResult:
        schedule_array.append(list(i))

    layout = [
        [sg.Table(values=schedule_array,
            headings=headings, 
            max_col_width=50,
            auto_size_columns=True,
            display_row_numbers=False,
            justification='right',
            num_rows=10,
            key='TABLE',
            row_height=35)],
        [sg.Button('Begin Appointment')]
    ]

    ds_window = sg.Window("Doctor Schedule", layout)

    while True:
        event, values = ds_window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Quit':
            break
        doctor_form_window()
        ds_window.close()

def nurse_schedule():

    print(ID)

    schedule_array = [[]]

    headings = ["appointmentID", "fname", "lname", "start_time", "room", "reason_for_visit"]

    schedule = "SELECT a.appointmentID, a.fname, a.lname, a.start_time, a.room, a.reason_for_visit \
        FROM APPOINTMENT a INNER JOIN NURSE n ON employeeID=" + ID + " AND n.room=a.room WHERE end_time is NULL AND a.doctorID is NULL;"

    cursor.execute(schedule)
    myResult = cursor.fetchall()

    for i in myResult:
        schedule_array.append(list(i))

    layout = [
        [sg.Table(values=schedule_array,
            headings=headings, 
            max_col_width=50,
            auto_size_columns=True,
            display_row_numbers=False,
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
        if event == sg.WIN_CLOSED:
            break
        nurse_form_window()
        window.close()

def nurse_form_window():
    doctor_array = [[]]

    doctors = "SELECT fname, lname, employeeID FROM EMPLOYEE WHERE job_title = 'doctor';"
    cursor.execute(doctors)
    myResult = cursor.fetchall()
    db.commit()

    for i in myResult:
        doctor_array.append(list(i))

    # All the stuff inside your window. This is the PSG magic code compactor...
    layout = [  
        [sg.Text("Appointment ID"), sg.Input(key='apptID'), sg.Text(size=(40,1))],
        [sg.Text("Assign Doctor"), sg.Combo(doctor_array), sg.Input(key='dr')],
        [sg.Text("Height"),  sg.Combo(['4ft', '5ft','6ft','7ft']), sg.Combo(['0"', '1"','2"','3"','4"','5"','6"','7"','8"','9"', '10"','11"'])],
        [sg.Text("Weight (pounds)"),  sg.Slider(range=(0, 1000), orientation='horizontal', default_value=150, size=(40,25))],
        [sg.Text("Blood Pressure (Systolic)"),  sg.Slider(range=(50, 200), orientation='vertical', default_value=100, size=(10,20)), \
            sg.Text("(Diastolic)"), sg.Slider(range=(50, 200), orientation='vertical', default_value=100, size=(10,20))],
        [sg.Text("Nurse's Notes"), sg.Input(key='notes'), sg.Text(size=(40,1))],
        [sg.Button('End Appointment')]
    ]

    # Create the Window
    nwindow = sg.Window('Nurse_Form', layout, size=(500,600))
    # Event Loop to process "events"
    while True:             
        event, values = nwindow.read()
        if event in (sg.WIN_CLOSED, 'Cancel'):
            break

        if event == 'End Appointment':
            end_visit = "UPDATE APPOINTMENT SET doctorID = '" + str(values['dr']) + "' \
                , nurse_notes = '" + str(values['notes']) + "' WHERE appointmentID = " + str(values['apptID']) + ";"
            cursor.execute(end_visit)
            db.commit()
            nwindow.close()
            nurse_schedule()


def patient_history():


    history_array = [[]]

    headings = ["AppointmentID", "Time", "Diagnosis", "Medication", "Dr's Notes"]

    history = "SELECT a.appointmentID, a.start_time, di.description, m.description, ad.doctor_notes  \
        FROM APPOINTMENT a \
        JOIN APPOINTMENT_DIAGNOSIS ad \
	        ON a.appointmentID = ad.appointmentID \
        JOIN APPOINTMENT_DIAGNOSIS_MEDICATION adm \
	        ON ad.appointmentID = adm.appointmentID AND ad.appt_diagnosis_code = adm.diagnosis_code \
        JOIN MEDICATION m \
	        ON m.medication_code = adm.medication_code \
        JOIN DIAGNOSIS di \
	        on adm.diagnosis_code = di.diagnosis_code \
        WHERE " + ID +  " = a.patientID;"

    cursor.execute(history)
    myResult = cursor.fetchall()

    for i in myResult:
        history_array.append(list(i))

    layout = [
        [sg.Table(values=history_array,
            headings=headings, 
            max_col_width=50,
            auto_size_columns=True,
            display_row_numbers=False,
            justification='right',
            num_rows=10,
            key='TABLE',
            row_height=35)],
        [sg.Button('View And Pay Bill'), sg.Exit()]
    ]

    window = sg.Window("Patient Portal", layout)

    while True:
        event, values = window.read()
        # See if user wants to quit or window was closed
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            print("Exited Patient")
            window.close()
            break
        if event == 'View And Pay Bill':
            print("view and pay bill")
            popup()


employee_column = [
    [sg.Text("Login As Employee")],
    [sg.Input(key='EID', do_not_clear=False)],
]

patient_column = [
    [sg.Text("Enter Patient Portal")],
    [sg.Input(key='PID', do_not_clear=False)]
]

button_column = [
    [sg.Button('Enter'), sg.Button(' Quit')],
    [sg.Text(size=(40,1), key='-OUTPUT-')]
]

# Define the window's contents
layout = [
    [
        sg.Column(employee_column),
        sg.VSeperator(),
        sg.Column(patient_column)
    ], [sg.VPush(), sg.Column(button_column, element_justification='c'), sg.Push()] 
]

# Create the window
window = sg.Window('LOGIN', layout, margins=(20,100))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == ' Quit':
        break
    # Output a message to the window

    if event == 'Enter' and values['PID'] == '':
        employee_query = "select job_title from EMPLOYEE WHERE employeeID = " + str(values['EID']) + ";"
        cursor.execute(employee_query)
        myResult = cursor.fetchone()

        ID = values['EID']


        while myResult:
            if myResult[0] == "doctor":
                doctor_schedule()
                break
            elif myResult[0] == "nurse":
                nurse_schedule()
                break
            elif myResult[0] == "receptionist":
                receptionist_form()
                break
            else: 
                print("fail")
            #cursor.close()


    if values['PID'] != '':
        patient_query = "select fname, lname from PATIENT WHERE patientID=" + str(values['PID']) + ";"
        cursor.execute(patient_query)
        myResult = cursor.fetchall()

        ID = values['PID']

        while myResult:
            patient_history()
            break


# Finish up by removing from the screen
window.close()











