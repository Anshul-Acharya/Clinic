DROP DATABASE IF EXISTS Clinic;
CREATE DATABASE Clinic;

USE Clinic;


DROP TABLE IF EXISTS DOCTOR;
CREATE TABLE DOCTOR (


  fname    varchar(15) not null,
  lname    varchar(15) not null,
  employeeID     char(9),
  bdate    date,
  phone_number varchar(15),
  specialty varchar(9),

  CONSTRAINT pk_doctor primary key (employeeID)
);

DROP TABLE IF EXISTS NURSE;
CREATE TABLE NURSE (
  fname    varchar(15) not null,
  lname    varchar(15) not null,
  employeeID     char(9),
  bdate    date,
  phone_number varchar(15),
  room int,

  CONSTRAINT pk_nurse primary key (employeeID)
);

DROP TABLE IF EXISTS RECEPTIONIST;
CREATE TABLE RECEPTIONIST (
  fname    varchar(15) not null,
  lname    varchar(15) not null,
  employeeID     char(9),
  bdate    date,
  phone_number varchar(15),

  CONSTRAINT pk_receptionist primary key (employeeID)
);


DROP TABLE IF EXISTS PATIENT;
CREATE TABLE PATIENT(
  fname    varchar(15) not null,
  lname    varchar(15) not null,
  patientID     char(9),
  bdate    date,
  insuranceID char(9),

  CONSTRAINT pk_patientID primary key (patientID)
);


DROP TABLE IF EXISTS APPOINTMENT;
CREATE TABLE APPOINTMENT(
  fname    varchar(15) not null,
  lname    varchar(15) not null,
  appointmentID     char(9),
  patientID     char(9),
  nurseID     char(9),
  doctorID     char(9),
  start_time   time,
  end_time    time,
  room int,
  reason_for_visit char(50),

  CONSTRAINT pk_appointment primary key (appointmentID)
);

DROP TABLE IF EXISTS APPOINTMENT_TYPE;
CREATE TABLE APPOINTMENT_TYPE(
  appointment_type     char(9),
  description char(50),

  CONSTRAINT pk_appointment_type primary key (appointment_type)
);

DROP TABLE IF EXISTS ROOM;
CREATE TABLE ROOM(
  room_number int,
  room_type char(50),

  CONSTRAINT pk_room_number primary key (room_number)
);

DROP TABLE IF EXISTS APPOINTMENT_DIAGNOSIS;
CREATE TABLE APPOINTMENT_DIAGNOSIS(
  appointmentID     char(9),
  appt_diagnosis_code     char(9),
  description char(50),

  CONSTRAINT pk_appt_diagnosis primary key (appt_diagnosis_code)
);


DROP TABLE IF EXISTS DIAGNOSIS;
CREATE TABLE DIAGNOSIS(
  diagnosis_code     char(9),
  doctor_notes char(50),

  CONSTRAINT pk_diagnosis_code primary key (diagnosis_code)
);

DROP TABLE IF EXISTS MEDICATION;
CREATE TABLE MEDICATION(
  medication_code     char(9),
  diagnosis_code     char(9),
  description char(50),
  cost  double,
  notes char(50),

  CONSTRAINT pk_medication primary key (medication_code),
  CONSTRAINT fk_diagnosis foreign key (diagnosis_code) references DIAGNOSIS(diagnosis_code)
);

DROP TABLE IF EXISTS APPOINTMENT_DIAGNOSIS_MEDICATION;
CREATE TABLE APPOINTMENT_DIAGNOSIS_MEDICATION(
  appt_medicine     char(9),
  appointmentID     char(9),
  diagnosis_code     char(9),
  medication_code     char(9),

  CONSTRAINT pk_appointment primary key (appointmentID)
);

-- Insert all records
INSERT INTO DOCTOR VALUES ('Bill','Rogers','123456789','1979-05-22', '911', 'gp');
INSERT INTO DOCTOR VALUES ('Ed','Sproat','123456799','1999-05-22', '911', 'ent');

INSERT INTO NURSE VALUES ('Bill','Rogers','123456779','1979-05-22', '911', '69');
INSERT INTO NURSE VALUES ('Ed','Sproat','123456799','1999-05-22', '911', '420');

INSERT INTO RECEPTIONIST VALUES ('Bilil','Rogers','123456780','1979-05-22', '911');
INSERT INTO RECEPTIONIST VALUES ('Biloooo','Rskjogers','123456789','1979-05-22', '911');

INSERT INTO PATIENT VALUES ('Bi','gers','023456789','1979-05-22', '911');
INSERT INTO PATIENT VALUES ('Bo','Rers','000000000','1979-05-22', '911');

INSERT INTO APPOINTMENT VALUES ('Biloooo','Rskjogers', '000000000', '123456779' , '123456789','19792', '2017-08-15 19:30:10', '2017-09-15 19:30:10', '69', 'herpes');

INSERT INTO APPOINTMENT_TYPE VALUES ('PHYSICAL','examine subject');

INSERT INTO ROOM VALUES ('89' , 'can do x ray');

INSERT INTO APPOINTMENT_DIAGNOSIS VALUES ('000','8998uu', '65');

-- Adding FK constraint after loading data into system
--Alter table EMPLOYEE
--ADD CONSTRAINT fk_employee_employee foreign key (superssn) references EMPLOYEE(ssn);



-- Select Staements to validate all the tables were created properly
SELECT * FROM DOCTOR;
SELECT * FROM DEPENDENT;
SELECT * FROM DEPT_LOCATIONS;
SELECT * FROM EMPLOYEE;
SELECT * FROM PROJECT;
SELECT * FROM WORKS_ON;
