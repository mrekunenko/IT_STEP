-- Домашнє завдання. Модуль 15. База даних ACADEMY

-- Перебудова таблиць
DROP TABLE IF EXISTS TEACHERS CASCADE;
DROP TABLE IF EXISTS GROUPS CASCADE;
DROP TABLE IF EXISTS FACULTIES CASCADE;
DROP TABLE IF EXISTS DEPARTMENTS CASCADE;

-- Таблиця DEPARTMENTS (кафедри)
-- FINANCING - фінансування кафедри (не < 0)
-- NAME - унікальна назва кафедри
CREATE TABLE DEPARTMENTS (
    ID SERIAL PRIMARY KEY,
    FINANCING NUMERIC(12,2) NOT NULL CHECK (FINANCING >= 0) DEFAULT 0,
    NAME VARCHAR(100) NOT NULL CHECK (NAME <> '') UNIQUE
);

INSERT INTO DEPARTMENTS (FINANCING, NAME) VALUES
(20000.00, 'Кафедра экономики'),
(18000.00, 'Кафедра бухгалтерского учёта и аудита'),
(22000.00, 'Кафедра финансов и банковского дела'),
(19000.00, 'Кафедра маркетинга и менеджмента'),
(21000.00, 'Кафедра информационных систем в экономике'),
(17000.00, 'Кафедра бизнес-анализа'),
(16000.00, 'Кафедра цифровой экономики'),
(15000.00, 'Кафедра программирования и IT-проектов'),
(14000.00, 'Кафедра управления данными и базами данных'),
(20000.00, 'Кафедра электронной коммерции');


-- Таблиця FACULTIES (факультети)
-- DEAN - декан факультету
-- NAME - унікальна назва факультету
CREATE TABLE FACULTIES (
    ID SERIAL PRIMARY KEY,
    DEAN VARCHAR(255) NOT NULL CHECK (DEAN <> ''),
    NAME VARCHAR(100) NOT NULL CHECK (NAME <> '') UNIQUE
);

INSERT INTO FACULTIES (DEAN, NAME) VALUES
('Петренко Иван Иванович', 'Факультет экономики и IT'),
('Сидоренко Елена Петровна', 'Факультет медицины'),
('Коваленко Андрей Сергеевич', 'Факультет юриспруденции'),
('Мельник Наталья Викторовна', 'Факультет инженерии и технологий'),
('Ткаченко Олег Михайлович', 'Факультет психологии и социальных наук'),
('Бондаренко Екатерина Павловна', 'Факультет биологии и экологии'),
('Шевченко Владимир Александрович', 'Факультет физики и математики'),
('Кузьменко Марина Владимировна', 'Факультет химии и материаловедения'),
('Гончаренко Сергей Игоревич', 'Факультет международных отношений'),
('Лысенко Юлия Алексеевна', 'Факультет искусств и дизайна');


-- Таблиця GROUPS (групи)
-- RATING - рейтинг групи (0..5)
-- YEAR - курс (1..5)
CREATE TABLE GROUPS (
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(10) NOT NULL CHECK (NAME <> '') UNIQUE,
    RATING INT NOT NULL CHECK (RATING BETWEEN 0 AND 5),
    YEAR INT NOT NULL CHECK (YEAR BETWEEN 1 AND 5)
);

INSERT INTO GROUPS (NAME, RATING, YEAR) VALUES
('ЭК-101', 4, 1),
('ЭК-102', 5, 1),
('ЭК-103', 3, 1),
('ЭК-201', 4, 2),
('ЭК-202', 5, 2),
('ЭК-203', 3, 2),
('ЭК-301', 4, 3),
('ЭК-302', 5, 3),
('ЭК-303', 2, 3),
('ЭК-304', 3, 3),
('ЭК-401', 4, 4),
('ЭК-402', 5, 4),
('ЭК-403', 3, 4),
('ЭК-404', 2, 4),
('ЭК-501', 4, 5),
('ЭК-502', 5, 5),
('ЭК-503', 3, 5),
('ЭК-504', 2, 5),
('IT-101', 4, 1),
('IT-102', 5, 1),
('IT-201', 3, 2),
('IT-202', 4, 2),
('IT-301', 5, 3),
('IT-302', 3, 3),
('IT-401', 4, 4),
('IT-402', 2, 4),
('IT-501', 5, 5),
('IT-502', 3, 5),
('IT-503', 4, 5),
('IT-504', 2, 5);


-- Таблиця TEACHERS (викладачі)
-- ISASSISTANT / ISPROFESSOR - булеві значення (було bit в умові)
-- PREMIUM, SALARY - числові значення замість money
CREATE TABLE TEACHERS (
    ID SERIAL PRIMARY KEY,
    EMPLOYMENTDATE DATE NOT NULL CHECK (EMPLOYMENTDATE > '1990-01-01'),
    ISASSISTANT BOOLEAN NOT NULL DEFAULT FALSE,
    ISPROFESSOR BOOLEAN NOT NULL DEFAULT FALSE,
    NAME VARCHAR(255) NOT NULL CHECK (NAME <> ''),
    SURNAME VARCHAR(255) NOT NULL CHECK (SURNAME <> ''),
    POSITION VARCHAR(255) NOT NULL CHECK (POSITION <> ''),
    PREMIUM NUMERIC(12,2) NOT NULL CHECK (PREMIUM >= 0) DEFAULT 0,
    SALARY NUMERIC(12,2) NOT NULL CHECK (SALARY > 0) DEFAULT 0
);

INSERT INTO TEACHERS
(EMPLOYMENTDATE, ISASSISTANT, ISPROFESSOR, NAME, SURNAME, POSITION, PREMIUM, SALARY)
VALUES
('2015-09-01', TRUE,  FALSE, 'Иван',     'Петренко',   'Ассистент кафедры экономики',                     500, 2000),
('2010-03-15', FALSE, TRUE,  'Елена',    'Сидоренко',  'Профессор кафедры IT',                            1000, 3500),
('2018-01-20', TRUE,  FALSE, 'Андрей',   'Коваленко',  'Ассистент кафедры маркетинга',                    400, 1800),
('2005-09-01', FALSE, TRUE,  'Наталья',  'Мельник',    'Профессор кафедры финансов',                     1200, 4000),
('2012-08-15', FALSE, TRUE,  'Олег',     'Ткаченко',   'Профессор кафедры бухгалтерского учета',          800, 3200),
('2019-02-01', TRUE,  FALSE, 'Катерина', 'Бондаренко', 'Ассистент кафедры цифровой экономики',            300, 1500),
('2008-06-10', FALSE, TRUE,  'Владимир', 'Шевченко',   'Профессор кафедры программирования',              900, 3600),
('2016-09-01', TRUE,  FALSE, 'Марина',   'Кузьменко',  'Ассистент кафедры баз данных',                    450, 1900),
('2011-11-20', FALSE, TRUE,  'Сергей',   'Гончаренко', 'Профессор кафедры электронной коммерции',         700, 3300),
('2017-03-10', TRUE,  FALSE, 'Юлия',     'Лысенко',    'Ассистент кафедры бизнес-анализа',                350, 1700),
('2013-07-01', FALSE, TRUE,  'Оксана',   'Мороз',      'Профессор кафедры маркетинга',                    950, 3400),
('2014-05-15', TRUE,  FALSE, 'Оксана',   'Мороз',      'Ассистент кафедры финансов',                      400, 1800),
('2009-09-01', FALSE, TRUE,  'Игорь',    'Федоренко',  'Профессор кафедры экономики',                    1100, 3700),
('2018-08-20', TRUE,  FALSE, 'Татьяна',  'Даниленко',  'Ассистент кафедры бухгалтерского учета',          300, 1600),
('2011-02-01', FALSE, TRUE,  'Виктор',   'Семененко',  'Профессор кафедры IT',                           1000, 3600),
('2016-09-01', TRUE,  FALSE, 'Алина',    'Бондарь',    'Ассистент кафедры программирования',              350, 1700),
('2010-01-10', FALSE, TRUE,  'Николай',  'Ткачук',     'Профессор кафедры баз данных',                    900, 3500),
('2019-03-15', TRUE,  FALSE, 'Евгения',  'Гаврилюк',   'Ассистент кафедры цифровой экономики',            250, 1500),
('2007-06-20', FALSE, TRUE,  'Павел',    'Козак',      'Профессор кафедры бизнес-анализа',               1200, 4000),
('2015-11-01', TRUE,  FALSE, 'Людмила',  'Кириленко',  'Ассистент кафедры электронной коммерции',         300, 1600);


-- Запити

-- 1. Вивести таблицю кафедр, але поля у зворотному порядку
SELECT
    NAME,
    FINANCING,
    ID
FROM DEPARTMENTS;

-- 2. Назви груп та їх рейтинг
SELECT
    NAME   AS group_name,
    RATING AS group_rating
FROM GROUPS;

-- 3. Прізвище викладача і відсоток надбавки
SELECT
    SURNAME,
    PREMIUM,
    SALARY,
    (PREMIUM / SALARY * 100) AS premium_percent_of_salary,
    (PREMIUM / (SALARY + PREMIUM) * 100) AS premium_percent_of_total
FROM TEACHERS;

-- 4. "The dean of faculty X is Y."
SELECT
    'The dean of faculty ' || NAME || ' is ' || DEAN || '.' AS faculty_info
FROM FACULTIES;

-- 5. Прізвища професорів зі ставкою > 1050
SELECT
    SURNAME
FROM TEACHERS
WHERE ISPROFESSOR = TRUE
  AND SALARY > 1050;

-- 6. Кафедри з фінансуванням <11000 або >25000
SELECT
    NAME
FROM DEPARTMENTS
WHERE FINANCING < 11000
   OR FINANCING > 25000;

-- 7. Факультети, окрім "Computer Science"
SELECT
    NAME
FROM FACULTIES
WHERE NAME <> 'Computer Science';

-- 8. Прізвища та посади тих, хто не професор
SELECT
    SURNAME,
    POSITION
FROM TEACHERS
WHERE ISPROFESSOR = FALSE;

-- 9. Асистенти з надбавкою в діапазоні 160..550
SELECT
    SURNAME,
    POSITION,
    SALARY,
    PREMIUM
FROM TEACHERS
WHERE ISASSISTANT = TRUE
  AND PREMIUM BETWEEN 160 AND 550;

-- 10. Асистенти: прізвище і ставка
SELECT
    SURNAME,
    SALARY
FROM TEACHERS
WHERE ISASSISTANT = TRUE;

-- 11. Прийняті на роботу до 01.01.2000
SELECT
    SURNAME,
    POSITION
FROM TEACHERS
WHERE EMPLOYMENTDATE < '2000-01-01';

-- 12. Кафедри, що йдуть в алфавіті раніше за "Кафедра программирования и IT-проектов"
SELECT
    NAME AS "Name of Department"
FROM DEPARTMENTS
WHERE NAME < 'Кафедра программирования и IT-проектов'
ORDER BY NAME ASC;

-- 13. Асистенти із сумарною зарплатою (ставка + надбавка) <= 1200
SELECT
    SURNAME
FROM TEACHERS
WHERE ISASSISTANT = TRUE
  AND (SALARY + PREMIUM) <= 1200;

-- 14. Групи 5-го курсу з рейтингом 2..4
SELECT
    NAME
FROM GROUPS
WHERE YEAR = 5
  AND RATING BETWEEN 2 AND 4;

-- 15. Асистенти зі ставкою < 550 або надбавкою < 200
SELECT
    SURNAME
FROM TEACHERS
WHERE ISASSISTANT = TRUE
  AND (SALARY < 550 OR PREMIUM < 200);