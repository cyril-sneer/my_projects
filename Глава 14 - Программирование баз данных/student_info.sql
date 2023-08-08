-- CREATE SECTION --
CREATE DATABASE IF NOT EXISTS student_info;
USE student_info;

CREATE TABLE IF NOT EXISTS Departments
(DeptID VARCHAR(3) NOT NULL PRIMARY KEY,
Name VARCHAR(30) NOT NULL);

CREATE TABLE IF NOT EXISTS Majors
(MajorID VARCHAR(6) NOT NULL PRIMARY KEY,
Name VARCHAR(30) NOT NULL);

CREATE TABLE IF NOT EXISTS Students
(StudentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
Name VARCHAR(30) NOT NULL,
MajorID VARCHAR(6) NOT NULL,
DeptID VARCHAR(3) NOT NULL,
FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
FOREIGN KEY (DeptID) REFERENCES Departments(DeptID));


-- INSERT SECTION --
INSERT INTO Departments (DeptID, Name)
VALUES
("TEC", "Technical"),
("HUM", "Humanitarian"),
("MED", "Medical"),
("LAW", "Juridical");

INSERT INTO Majors (MajorID, Name)
VALUES
("ECO001", "Economist"),
("LAW001", "Lawyer"),
("LAW002", "Judge"),
("ENG001", "Engineer"),
("ENG002", "IT specialist"),
("HUM001", "Teacher"),
("MED001", "Doctor"),
("MED002", "Nurse");

INSERT INTO Students (Name, MajorID, DeptID)
VALUES
("Serge", "LAW001", "LAW"),
("Alex", "HUM001", "HUM"),
("Katty", "MED002", "MED")


-- SELECT SECTION --
select Students.Name, Majors.Name, Departments.Name
FROM students, majors, departments
WHERE students.majorid = majors.majorid
AND students.deptID = departments.deptID