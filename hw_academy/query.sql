-- Active: 1726065996358@@127.0.0.1@3306




-- Active: 1726065996358@@127.0.0.1@3306
CREATE TABLE departament (
    id INT PRIMARY KEY UNIQUE,
    name TEXT NOT NULL UNIQUE,
    financing DECIMAL DEFAULT (0) NOT NULL
);

CREATE Table faculties (
    id INTEGER PRIMARY KEY NOT NULL,
    dean TEXT NOT NULL,
    name TEXT NOT NULL UNIQUE
);

CREATE Table groups (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL UNIQUE,
    rating INTEGER,
    course INTEGER NOT NULL
);


CREATE Table teachers(
    id INTEGER PRIMARY KEY NOT NULL,
    employment_date DATE not NULL,
    is_assistent BIT not NULL DEFAULT(0),
    is_professor Bit not NULL DEFAULT(0),
    name TEXT not NULL,
    posotion TEXT not NULL,
    premium DECIMAL not NULL DEFAULT(0),
    salary DECIMAL not NULL DEFAULT(0),
    surname TEXT not NULL
)



SELECT financing, name, id FROM departament

select name as group_name, rating as group_rating FROM groups

SELECT
    surname as teacher_surname,
    (premium / salary) * 100 as premium_to_salary_percentage,
    premium / (salary+premium) * 100 as premium_to_total_percentage
FROM teachers


SELECT ('the dean of faculty '|| name) || (' is ' || dean) FROM faculties


SELECT surname
from teachers
WHERE salary > 1500 AND is_professor = TRUE


SELECT name
FROM departament
WHERE financing>25000 OR 11000>financing

SELECT name
from faculties
WHERE not name='Faculty of Science'

SELECT surname, posotion from teachers WHERE is_professor = 0;
 
select surname, posotion, premium 
FROM teachers
WHERE is_assistent=1 and 160<premium and premium<550


SELECT surname, salary
FROM teachers
WHERE is_assistent=1


select * FROM teachers WHERE employment_date < DATETIME('2000-01-01');


-- Active: 1726065996358@@127.0.0.1@3306
INSERT INTO departament (id, name, financing)
VALUES 
(1, 'Computer Science', 50000.00),
(2, 'Mathematics', 30000.00),
(3, 'Physics', 40000.00);

INSERT INTO faculties (id, dean, name)
VALUES 
(1, 'Dr. Smith', 'Faculty of Engineering'),
(2, 'Dr. Johnson', 'Faculty of Science'),
(3, 'Dr. Brown', 'Faculty of Arts');

INSERT INTO groups (id, name, rating, course)
VALUES 
(1, 'Group A', 4, 2),
(2, 'Group B', 3, 3),
(3, 'Group C', 5, 1),
(4, 'Group D', 2, 4);

INSERT INTO teachers (id, employment_date, is_assistent, is_professor, name, posotion, premium, salary, surname)
VALUES 
(1, '2024-01-15', 0, 1, 'John', 'Professor', 1500.00, 5000.00, 'Doe'),
(2, '2023-09-01', 1, 0, 'Emily', 'Assistant', 500.00, 3000.00, 'Smith'),
(3, '2022-05-20', 0, 0, 'Michael', 'Lecturer', 200.00, 2500.00, 'Brown'),
(4, '2021-11-11', 1, 0, 'Sarah', 'Assistant', 300.00, 2800.00, 'Johnson');
