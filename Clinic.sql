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
  diagnosisID INT(9),
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

INSERT INTO DOCTOR VALUES ('1234','gp');
INSERT INTO DOCTOR VALUES ('3456','gp');

INSERT INTO NURSE VALUES ('5676','1');
INSERT INTO NURSE VALUES ('3212','2');

INSERT INTO RECEPTIONIST VALUES ('2345');

INSERT INTO EMPLOYEE VALUES ('Mary','OGallagher','1234','1979-05-22', '972-454-4545', 'doctor');
INSERT INTO EMPLOYEE VALUES ('Edward','Sproat','3456','1979-05-22', '843-344-3244', 'doctor');

INSERT INTO EMPLOYEE VALUES ('Milo','Derek','5676','1979-05-22', '349-341-9981', 'nurse');
INSERT INTO EMPLOYEE VALUES ('Richard','Miller','3212','1979-05-22', '233-565-5911', 'nurse');

INSERT INTO EMPLOYEE VALUES ('Christian','Martinez','2345','1979-05-22', '911-243-2332', 'receptionist');

INSERT INTO PATIENT VALUES ('Amanda','Cooper','112345678','1969-08-30', '231988');
INSERT INTO PATIENT VALUES ('James','Marler',null,'1997-11-07', '231988');
INSERT INTO PATIENT VALUES ('Andrew','Hansen',null,'1997-12-01', '038834');
INSERT INTO PATIENT VALUES ('Kristen','Wood',null,'2000-01-12', '3242343');
INSERT INTO PATIENT VALUES ('Blake','Willaims',null,'1999-05-22', '2312312');

INSERT INTO APPOINTMENT VALUES ('Amanda', 'Cooper','223456789', '112345678', null , null, '2017-08-15 19:30:10', '2017-09-15 19:30:10', '1', 'Chest Pain', null);
INSERT INTO APPOINTMENT VALUES ('James', 'Marler', '223456790','112345679', null, null, '2017-08-15 19:30:10', null, '1', 'flu like symptoms',null);
INSERT INTO APPOINTMENT VALUES ('Andrew', 'Hansen','223456791', '112345680' , null, null, '2017-08-15 19:30:10', null, '1', 'stomach pain', null);
INSERT INTO APPOINTMENT VALUES ('Kristen', 'Wood', '223456792','112345681', null, null, '2017-08-15 19:30:10', null, '2', 'sore throat', null);
INSERT INTO APPOINTMENT VALUES ('Blake', 'Williams','223456793','112345682',  null,null, '2017-08-15 19:30:10', null, '2', 'back pain', null);

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

INSERT INTO MEDICATION (description) VALUES
	('ACETYLCYSTEINE'),
	('ADENOSINE'),
	('ALDACTAZIDE'),
	('ALDACTONE'),
	('ALFENTANIL INJECTION'),
	('AMMONIUM CHLORIDE'),
	('Ampicillin Sodium'),
	('ARGATROBAN'),
	('AROMASIN'),
	('ENALAPRILAT'),
	('ESTRING'),
	('GLYNASE PRESTAB'),
	('HEPARIN SODIUM INJECTION'),
	('HETASTARCH'),
	('HEXTEND'),
	('HUMATIN'),
	('MILRINONE LACTATE'),
	('MINIPRESS'),
	('PLEGISOL'),
	('POTASSIUM ACETATE'),
	('POTASSIUM PHOSPHATES'),
	('PRECEDEX'),
	('SUFENTANIL CITRATE'),
	('SYNAREL'),
	('TALZENNA'),
	('TAPAZOLE'),
	('TESTOSTERONE CYPIONATE'),
	('TOBRAMYCIN'),
	('TOPOTECAN'),
	('TORISEL'),
	('TOVIAZ'),
	('TRECATOR'),
	('TROBICIN'),
	('TRUMENBA'),
	('TYGACIL'),
	('UNASYN'),
	('Vancomycin Hydrochloride'),
	('VIROPTIC'),
	('XALATAN'),
	('XANAX'),
	('XELJANZ'),
	('ZARONTIN'),
	('ZOLEDRONIC ACID'),
	('ZOLOFT'),
	('ZOSYN'),
	('ZYVOX');



SELECT * 
FROM APPOINTMENT a 
JOIN APPOINTMENT_DIAGNOSIS ad 
	ON a.appointmentID = ad.appointmentID 
JOIN APPOINTMENT_DIAGNOSIS_MEDICATION adm 
	ON ad.appointmentID = adm.appointmentID AND ad.appt_diagnosis_code = adm.diagnosis_code
JOIN MEDICATION m 
	ON m.medication_code = adm.medication_code 
JOIN DIAGNOSIS di
	on adm.diagnosis_code = di.diagnosis_code;
