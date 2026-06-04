drop table students;
create table student(student_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
grade VARCHAR(5),
city VARCHAR(50),
marks INT
);
-- Retrieve all records from the Students table.
INSERT INTO Student VALUES
(1, 'Amit', 19, 'A', 'Ahmedabad', 85),
(2, 'Neha', 20, 'B', 'Mumbai', 75),
(3, 'Ajay', 18, 'A', 'Ahmedabad', 90),
(4, 'Riya', 21, 'C', 'Delhi', 65),
(5, 'Ankit', 22, 'B', 'Mumbai', 72),
(6, 'Priya', 19, 'A', 'Ahmedabad', 88),
(7, 'Arjun', 20, 'B', 'Surat', 78);
SELECT * from student;
-- Display only the names and ages of students.
SELECT name, age FROM Students;
-- Show details of students who live in Ahmedabad.
SELECT * FROM Students WHERE city = 'Ahmedabad';
-- List all students with grade 'A'.
SELECT * FROM students where grade='A';
-- Find students who scored more than 80 marks.
SELECT * FROM students WHERE marks>80;
-- Display students aged between 18 and 21.
SELECT * FROM students where age between 18 and 21; 
-- List students who are from Mumbai and have marks above 70
SELECT * FROM students where city='Mumbai' and marks >70;
-- Find students whose names start with the letter 'A'.
SElECT * FROM students where name LIKE 'A%';
-- Display all students sorted by marks in descending order.
select * from students order by marks desc;
-- List students sorted by age in ascending order.
SELECT * FROM students order by age asc;
-- Show students sorted by city and then by marks (highest first).
SELECT * FROM students order by city asc, marks desc;