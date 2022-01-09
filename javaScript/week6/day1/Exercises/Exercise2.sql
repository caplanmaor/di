-- insert

CREATE TABLE  students (
	id SERIAL,
	last_name varchar,
	first_name varchar,
	birth_date date
)


INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Marc', 'Benichou', '02/11/1998'),
	('Yoan', 'Cohen', '03/12/2010'),
	('Lea', 'Benichou', '27/07/1987'),
	('Amelia', 'Dux', '07/04/1996'),
	('David', 'Grez', '14/06/2003'),
	('Omer', 'Simpson', '03/10/1980')


INSERT INTO students (first_name, last_name, birth_date)
VALUES ('Maor', 'Caplan', '23/07/1995')

-- select

-- fetch all data
SELECT * FROM students

-- fetch all students first and last names
SELECT first_name, last_name FROM students

-- id = 2
SELECT first_name, last_name FROM students WHERE id = 2

-- marc benichou
SELECT first_name, last_name FROM students WHERE  first_name = 'Marc' AND 

-- first name contains a
SELECT first_name, last_name FROM students WHERE  first_name LIKE '%a%' 

-- start with a
SELECT first_name, last_name FROM students WHERE  first_name LIKE 'a%' 

-- ends with a
SELECT first_name, last_name FROM students WHERE  first_name LIKE '%a' 

-- second to last latter is a
SELECT first_name, last_name FROM students WHERE (SELECT RIGHT (first_name, 2)) LIKE 'a%';

-- id 1 and 3
SELECT first_name, last_name FROM students WHERE id = 1 OR id = 3