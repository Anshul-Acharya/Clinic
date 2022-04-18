DROP DATABASE IF EXISTS Clinic;
CREATE DATABASE Clinic;

USE Clinic;


DROP TABLE IF EXISTS EMPLOYEE;
CREATE TABLE EMPLOYEE (


  fname    varchar(15) not null,
  lname    varchar(15) not null,
  employeeID     INT(9) not null AUTO_INCREMENT,
  bdate    date,
  phone_number varchar(15),
  job_title  varchar(15),

  CONSTRAINT pk_employeeID primary key (employeeID)
);

DROP TABLE IF EXISTS DOCTOR;
CREATE TABLE DOCTOR (
  employeeID     char(9),
  specialty varchar(9),

  CONSTRAINT pk_doctorID primary key (employeeID)
);

DROP TABLE IF EXISTS NURSE;
CREATE TABLE NURSE (
  employeeID     char(9),
  room int,

  CONSTRAINT pk_nurse primary key (employeeID)
);

DROP TABLE IF EXISTS RECEPTIONIST;
CREATE TABLE RECEPTIONIST (
  employeeID     char(9),

  CONSTRAINT pk_receptionist primary key (employeeID)
);


DROP TABLE IF EXISTS PATIENT;
CREATE TABLE PATIENT(
  fname    varchar(15) not null,
  lname    varchar(15) not null,
  patientID     INT(9) ZEROFILL not null AUTO_INCREMENT,
  bdate    date,
  insuranceID char(9),

  CONSTRAINT pk_patientID primary key (patientID)
);


DROP TABLE IF EXISTS APPOINTMENT;
CREATE TABLE APPOINTMENT(  
  fname    varchar(15) not null,
  lname    varchar(15) not null,
  appointmentID    INT(9) ZEROFILL not null AUTO_INCREMENT,
  patientID     char(9),
  nurseID     char(9),
  doctorID     char(9),
  start_time   time,
  end_time    time,
  room int,
  reason_for_visit char(50),
  nurse_notes char(50),

  CONSTRAINT pk_appointment primary key (appointmentID)
);


DROP TABLE IF EXISTS APPOINTMENT_DIAGNOSIS;
CREATE TABLE APPOINTMENT_DIAGNOSIS(
  appointmentID     char(9),
  appt_diagnosis_code     INT(9) not null AUTO_INCREMENT,
  doctor_notes char(50),

  CONSTRAINT pk_appt_diagnosis primary key (appt_diagnosis_code)
);


DROP TABLE IF EXISTS DIAGNOSIS;
CREATE TABLE DIAGNOSIS(
  diagnosis_code  INT(9) not null AUTO_INCREMENT,
  description char(50),

  CONSTRAINT pk_diagnosis_code primary key (diagnosis_code)
);

DROP TABLE IF EXISTS MEDICATION;
CREATE TABLE MEDICATION(
  medication_code   INT(9) not null AUTO_INCREMENT,
  diagnosis_code     char(9),
  description char(50),

  CONSTRAINT pk_medication primary key (medication_code)
);

DROP TABLE IF EXISTS APPOINTMENT_DIAGNOSIS_MEDICATION;
CREATE TABLE APPOINTMENT_DIAGNOSIS_MEDICATION(
  appt_medicine     INT(9) not null AUTO_INCREMENT,
  appointmentID     INt(9),
  diagnosis_code     char(9),
  medication_code     char(9),

  CONSTRAINT pk_appt_med primary key (appt_medicine)
);

INSERT INTO DOCTOR VALUES ('1234','');
INSERT INTO DOCTOR VALUES ('3456','');

INSERT INTO NURSE VALUES ('5676','69');
INSERT INTO NURSE VALUES ('3212','69');

INSERT INTO RECEPTIONIST VALUES ('2345');

INSERT INTO EMPLOYEE VALUES ('Bilo','SCOOTER','1234','1979-05-22', '911', 'doctor');
INSERT INTO EMPLOYEE VALUES ('SCOOTEW','pooR','3456','1979-05-22', '911', 'doctor');
INSERT INTO EMPLOYEE VALUES ('Nilo','OOTER','5676','1979-05-22', '911', 'nurse');
INSERT INTO EMPLOYEE VALUES ('lo','TER','3212','1979-05-22', '911', 'nurse');
INSERT INTO EMPLOYEE VALUES ('B','OOT','2345','1979-05-22', '911', 'receptionist');
INSERT INTO EMPLOYEE VALUES ('ilo','SCOOT','3312','1979-05-22', '911', 'receptionist');

INSERT INTO PATIENT VALUES ('Bi','gers','023456789','1979-05-22', '911');
INSERT INTO PATIENT VALUES ('Bo','Rers','000000000','1979-05-22', '911');
INSERT INTO PATIENT VALUES ('Bi','gers','023456788','1979-05-22', '911');

INSERT INTO PATIENT VALUES ('Edward','Sproat','420','1979-05-22', '911');
INSERT INTO PATIENT VALUES ('Dylkan','Faj','69','1979-05-22', '911');

INSERT INTO APPOINTMENT VALUES ('a', 'dd', '69', '123456779' , '123456789',null, '2017-08-15 19:30:10', '2017-09-15 19:30:10', '69', 'herpes', null);
INSERT INTO APPOINTMENT VALUES ('b', 'dssdfsf', '420', '123456779' , '123456789',null, '2017-08-15 19:30:10', null, '69', 'herpes',null);
INSERT INTO APPOINTMENT VALUES ('c', 'hello','0100332', '10000000' , '123456789',null, '2017-08-15 19:30:10', null, '69', 'herpes', null);
INSERT INTO APPOINTMENT VALUES ('d', 'uwu', '690', '123456779' , '123456789',null, '2017-08-15 19:30:10', null, '69', 'herpes', null);
INSERT INTO APPOINTMENT VALUES ('d', 'tbh', '5320010', '123456779' , '123456789',null, '2017-08-15 19:30:10', null, '69', 'herpes', null);

INSERT INTO DIAGNOSIS (description) VALUES
    ('Acid reflux'),
    ('Allergies'),
    ('Bronchitis'),
    ('Bruises'),
    ('Bug bites'),
    ('Burns'),
    ('Chickenpox'),
    ('Colds'),
    ('Concussion'),
    ('Cuts'),
    ('Ear infection'),
    ('Eye infection'),
    ('Fever'),
    ('Fifth disease'),
    ('Flu'),
    ('Fungal infection'),
    ('Gout'),
    ('Head lice'),
    ('Headache'),
    ('Heartburn'),
    ('Hives'),
    ('Ingrown toenail'),
    ('Joint pain'),
    ('Laryngitis'),
    ('Migraine'),
    ('Mononucleosis'),
    ('Nausea'),
    ('Pink eye'),
    ('Poison ivy'),
    ('Respiratory infection'),
    ('Ringworm'),
    ('Shingles'),
    ('Skin rash'),
    ('Sore throat'),
    ('STDs'),
    ('Strained muscle'),
    ('Strep throat'),
    ('Styes'),
    ('urinary tract infection'),
    ('Whooping cough');



INSERT INTO MEDICATION (diagnosis_code, description) VALUES ('1', 'xZANTAC');
INSERT INTO MEDICATION (diagnosis_code, description) VALUES ('2', 'xxZANTAC');
INSERT INTO MEDICATION (diagnosis_code, description) VALUES ('3', 'xxxZANTAC');
INSERT INTO MEDICATION (diagnosis_code, description) VALUES ('4', 'xxxxZANTAC');
INSERT INTO MEDICATION (diagnosis_code, description) VALUES ('5', 'xxxxxZANTAC');



SELECT adm.*
FROM APPOINTMENT a 
JOIN APPOINTMENT_DIAGNOSIS ad 
	ON a.appointmentID = ad.appointmentID 
JOIN APPOINTMENT_DIAGNOSIS_MEDICATION adm 
	ON ad.appointmentID = adm.appointmentID AND ad.appt_diagnosis_code = adm.diagnosis_code;
JOIN MEDICATION m 
	ON m.medication_code = adm.medication_code; 
