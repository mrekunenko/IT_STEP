-- База даних "ACADEMY"
-- Створення структури + наповнення тестовими даними + приклади запитів


-- Видаляємо таблиці, щоб можна було запускати скрипт повторно
DROP TABLE IF EXISTS GROUPSLECTURES CASCADE;
DROP TABLE IF EXISTS GROUPSCURATORS CASCADE;
DROP TABLE IF EXISTS GROUPS CASCADE;
DROP TABLE IF EXISTS LECTURES CASCADE;
DROP TABLE IF EXISTS SUBJECTS CASCADE;
DROP TABLE IF EXISTS CURATORS CASCADE;
DROP TABLE IF EXISTS TEACHERS CASCADE;
DROP TABLE IF EXISTS DEPARTMENTS CASCADE;
DROP TABLE IF EXISTS FACULTIES CASCADE;


-- ФАКУЛЬТЕТИ
CREATE TABLE FACULTIES (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
    FINANCING DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (FINANCING >= 0)
);

-- дані факультетів
INSERT INTO FACULTIES (NAME, FINANCING) VALUES
('ІНФОРМАТИКИ', 500000),
('МЕДИЦИНИ', 750000),
('ЕКОНОМІКИ', 300000);


-- КАФЕДРИ
CREATE TABLE DEPARTMENTS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> ''),
    FINANCING DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (FINANCING >= 0),
    FACULTYID INT NOT NULL REFERENCES FACULTIES(ID)
);

-- дані кафедр
INSERT INTO DEPARTMENTS (NAME, FINANCING, FACULTYID) VALUES
('КІБЕРБЕЗПЕКА', 150000, 1),
('ПРОГРАМУВАННЯ', 200000, 1),
('АНАТОМІЯ', 250000, 2),
('МІКРОБІОЛОГІЯ', 300000, 2),
('ФІНАНСИ', 100000, 3);


-- ВИКЛАДАЧІ
CREATE TABLE TEACHERS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL CHECK (NAME <> ''),
    SURNAME VARCHAR(255) NOT NULL CHECK (SURNAME <> ''),
    SALARY DECIMAL(10,2) NOT NULL CHECK (SALARY > 0)
);

-- дані викладачів
INSERT INTO TEACHERS (NAME, SURNAME, SALARY) VALUES
('ІВАН', 'ПЕТРЕНКО', 25000),
('ОЛЕНА', 'КОВАЛЕНКО', 28000),
('АНДРІЙ', 'СИДОРЕНКО', 30000),
('СВІТЛАНА', 'МЕЛЬНИК', 32000);


-- КУРАТОРИ
CREATE TABLE CURATORS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL CHECK (NAME <> ''),
    SURNAME VARCHAR(255) NOT NULL CHECK (SURNAME <> '')
);

-- дані кураторів
INSERT INTO CURATORS (NAME, SURNAME) VALUES
('ІГОР', 'ДАНИЛЮК'),
('ЛІЛІЯ', 'ПОЛІЩУК'),
('ВІКТОР', 'САВЧЕНКО');


-- ПРЕДМЕТИ
CREATE TABLE SUBJECTS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(100) NOT NULL UNIQUE CHECK (NAME <> '')
);

-- дані предметів
INSERT INTO SUBJECTS (NAME) VALUES
('БАЗИ ДАНИХ'),
('АНАТОМІЯ ЛЮДИНИ'),
('МІКРОЕКОНОМІКА'),
('ПРОГРАМУВАННЯ PYTHON');


-- ЛЕКЦІЇ (який викладач читає яку дисципліну і в якій аудиторії)
CREATE TABLE LECTURES (
    ID SERIAL PRIMARY KEY,
    LECTUREROOM VARCHAR(255) NOT NULL CHECK (LECTUREROOM <> ''),
    SUBJECTID INT NOT NULL REFERENCES SUBJECTS(ID),
    TEACHERID INT NOT NULL REFERENCES TEACHERS(ID)
);

-- дані лекцій
INSERT INTO LECTURES (LECTUREROOM, SUBJECTID, TEACHERID) VALUES
('АУДИТОРІЯ 101', 1, 1),  -- БАЗИ ДАНИХ читає ІВАН ПЕТРЕНКО
('АУДИТОРІЯ 102', 4, 2),  -- ПРОГРАМУВАННЯ PYTHON читає ОЛЕНА КОВАЛЕНКО
('АУДИТОРІЯ 201', 2, 3),  -- АНАТОМІЯ ЛЮДИНИ читає АНДРІЙ СИДОРЕНКО
('АУДИТОРІЯ 301', 3, 4);  -- МІКРОЕКОНОМІКА читає СВІТЛАНА МЕЛЬНИК


-- ГРУПИ (студентські групи)
CREATE TABLE GROUPS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(10) NOT NULL UNIQUE CHECK (NAME <> ''),
    YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5),
    RATING INT NOT NULL CHECK (RATING BETWEEN 0 AND 5) DEFAULT 3,
    DEPARTMENTID INT NOT NULL REFERENCES DEPARTMENTS(ID)
);

-- дані груп
INSERT INTO GROUPS (NAME, YEAR, RATING, DEPARTMENTID) VALUES
('ІНФ-11', 1, 4, 2),
('ІНФ-21', 2, 5, 1),
('МЕД-31', 3, 3, 3),
('ЕКО-41', 4, 4, 5);


-- ГРУПИ ↔ КУРАТОРИ (який куратор яку групу курує)
CREATE TABLE GROUPSCURATORS (
    ID SERIAL PRIMARY KEY,
    CURATORID INT NOT NULL REFERENCES CURATORS(ID),
    GROUPID INT NOT NULL REFERENCES GROUPS(ID)
);

-- дані про кураторів груп
INSERT INTO GROUPSCURATORS (CURATORID, GROUPID) VALUES
(1, 1),
(2, 2),
(3, 3);


-- ГРУПИ ↔ ЛЕКЦІЇ (якій групі читається яка лекція)
CREATE TABLE GROUPSLECTURES (
    ID SERIAL PRIMARY KEY,
    GROUPID INT NOT NULL REFERENCES GROUPS(ID),
    LECTUREID INT NOT NULL REFERENCES LECTURES(ID)
);

-- дані про лекції для груп
INSERT INTO GROUPSLECTURES (GROUPID, LECTUREID) VALUES
(1, 1),
(1, 2),
(2, 3),
(3, 4);


--------------------------------------------------
-- ЗАПИТИ
--------------------------------------------------

-- 1. Усі можливі пари викладачів і груп
--    (кожен викладач у поєднанні з кожною групою)
SELECT
    T.NAME  AS TeacherName,
    G.NAME  AS GroupName
FROM TEACHERS T
CROSS JOIN GROUPS G;


-- 2. Факультети, де існує кафедра з фінансуванням більшим,
--    ніж фінансування самого факультету
SELECT DISTINCT
    F.NAME AS FacultyName
FROM FACULTIES F
JOIN DEPARTMENTS D ON D.FACULTYID = F.ID
WHERE D.FINANCING > F.FINANCING;


-- 3. Куратори і групи, які вони курують
SELECT
    C.SURNAME AS CuratorSurname,
    G.NAME    AS GroupName
FROM GROUPSCURATORS GC
JOIN CURATORS C ON C.ID = GC.CURATORID
JOIN GROUPS   G ON G.ID = GC.GROUPID;


-- 4. Викладачі, які читають лекції у конкретній групі
--    (приклад: група 'ІНФ-11')
SELECT DISTINCT
    T.NAME    AS TeacherName,
    T.SURNAME AS TeacherSurname
FROM GROUPSLECTURES GL
JOIN LECTURES       L  ON L.ID        = GL.LECTUREID
JOIN GROUPS         G  ON G.ID        = GL.GROUPID
JOIN TEACHERS       T  ON T.ID        = L.TEACHERID
WHERE G.NAME = 'ІНФ-11';


-- 5. Кафедри і групи, які до них належать
SELECT
    D.NAME AS DepartmentName,
    G.NAME AS GroupName
FROM DEPARTMENTS D
JOIN GROUPS G ON G.DEPARTMENTID = D.ID;


-- ДОДАТКОВО:
-- Предмети, які читає викладач ІВАН ПЕТРЕНКО
SELECT DISTINCT
    S.NAME AS SubjectName
FROM SUBJECTS S
JOIN LECTURES L ON L.SUBJECTID = S.ID
JOIN TEACHERS T ON T.ID = L.TEACHERID
WHERE T.NAME = 'ІВАН'
  AND T.SURNAME = 'ПЕТРЕНКО';


-- Кафедри, на яких викладається конкретна дисципліна
-- (наприклад 'БАЗИ ДАНИХ')
SELECT DISTINCT
    D.NAME AS DepartmentName
FROM DEPARTMENTS D
JOIN GROUPS G           ON G.DEPARTMENTID = D.ID
JOIN GROUPSLECTURES GL  ON GL.GROUPID     = G.ID
JOIN LECTURES L         ON L.ID           = GL.LECTUREID
JOIN SUBJECTS S         ON S.ID           = L.SUBJECTID
WHERE S.NAME = 'БАЗИ ДАНИХ';
