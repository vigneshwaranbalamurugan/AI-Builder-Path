## Prompt

Generate SQL code for a Student Management System database.

Requirements:
1. Create tables:
   - Students
   - Departments
2. Include:
   - Primary keys
   - Foreign key relationship between Students and Departments
   - Proper data types
   - NOT NULL constraints where needed
3. Insert at least 5 sample records into each table.
4. Write SQL queries for:
   - Select all students
   - Find student by ID
   - List students in a department
   - Update student details
   - Delete a student record
   - Count number of students in each department
5. Use standard SQL compatible with MySQL or PostgreSQL.
6. Add simple comments explaining each query.

## Chatgpt

```sql
-- ==========================================
-- Student Management System Database (SQL)
-- Compatible with MySQL / PostgreSQL
-- ==========================================

-- ------------------------------------------
-- 1. Create Departments Table
-- Stores department information
-- ------------------------------------------
CREATE TABLE Departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL,
    department_head VARCHAR(100) NOT NULL
);


-- ------------------------------------------
-- 2. Create Students Table
-- Stores student information
-- Includes foreign key to Departments table
-- ------------------------------------------
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    date_of_birth DATE NOT NULL,
    department_id INT NOT NULL,

    -- Foreign key relationship
    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);


-- ------------------------------------------
-- 3. Insert Sample Records into Departments
-- At least 5 department records
-- ------------------------------------------
INSERT INTO Departments VALUES
(1, 'Computer Science', 'Dr. Smith'),
(2, 'Mechanical Engineering', 'Dr. Johnson'),
(3, 'Electrical Engineering', 'Dr. Lee'),
(4, 'Mathematics', 'Dr. Brown'),
(5, 'Physics', 'Dr. Davis');


-- ------------------------------------------
-- 4. Insert Sample Records into Students
-- At least 5 student records
-- ------------------------------------------
INSERT INTO Students VALUES
(101, 'Alice', 'Kumar', 'alice.kumar@example.com', '2002-03-15', 1),
(102, 'Rahul', 'Sharma', 'rahul.sharma@example.com', '2001-07-21', 2),
(103, 'Priya', 'Nair', 'priya.nair@example.com', '2003-01-11', 1),
(104, 'Arjun', 'Verma', 'arjun.verma@example.com', '2002-11-05', 3),
(105, 'Sneha', 'Iyer', 'sneha.iyer@example.com', '2001-09-30', 4);


-- ------------------------------------------
-- 5. Query: Select all students
-- Retrieves every student record
-- ------------------------------------------
SELECT * FROM Students;


-- ------------------------------------------
-- 6. Query: Find student by ID
-- Replace 101 with desired student ID
-- ------------------------------------------
SELECT * FROM Students
WHERE student_id = 101;


-- ------------------------------------------
-- 7. Query: List students in a department
-- Example: department_id = 1 (Computer Science)
-- ------------------------------------------
SELECT * FROM Students
WHERE department_id = 1;


-- ------------------------------------------
-- 8. Query: Update student details
-- Example: Update email for student ID 102
-- ------------------------------------------
UPDATE Students
SET email = 'rahul.newemail@example.com'
WHERE student_id = 102;


-- ------------------------------------------
-- 9. Query: Delete a student record
-- Example: Delete student ID 105
-- ------------------------------------------
DELETE FROM Students
WHERE student_id = 105;


-- ------------------------------------------
-- 10. Query: Count number of students in each department
-- Uses GROUP BY to aggregate student totals
-- ------------------------------------------
SELECT 
    d.department_name,
    COUNT(s.student_id) AS total_students
FROM Departments d
LEFT JOIN Students s
    ON d.department_id = s.department_id
GROUP BY d.department_name
ORDER BY total_students DESC;
```

## Claude Sonnet 4.6

```sql
-- ============================================================
-- STUDENT MANAGEMENT SYSTEM DATABASE
-- Compatible with MySQL and PostgreSQL
-- ============================================================


-- ============================================================
-- TABLE CREATION
-- ============================================================

-- Create the Departments table (must be created before Students due to FK)
CREATE TABLE Departments (
    department_id   INT             PRIMARY KEY,
    department_name VARCHAR(100)    NOT NULL,
    head_of_dept    VARCHAR(100),
    established_year INT
);

-- Create the Students table with a foreign key referencing Departments
CREATE TABLE Students (
    student_id      INT             PRIMARY KEY,
    first_name      VARCHAR(50)     NOT NULL,
    last_name       VARCHAR(50)     NOT NULL,
    email           VARCHAR(100)    NOT NULL UNIQUE,
    date_of_birth   DATE            NOT NULL,
    enrollment_date DATE            NOT NULL,
    department_id   INT             NOT NULL,
    gpa             DECIMAL(3, 2),

    -- Foreign key linking each student to a department
    CONSTRAINT fk_department
        FOREIGN KEY (department_id)
        REFERENCES Departments(department_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);


-- ============================================================
-- SAMPLE DATA — DEPARTMENTS
-- ============================================================

-- Insert 5 sample department records
INSERT INTO Departments (department_id, department_name, head_of_dept, established_year) VALUES
    (1, 'Computer Science',      'Dr. Alan Turing',      1985),
    (2, 'Mechanical Engineering','Dr. Nikola Tesla',     1970),
    (3, 'Business Administration','Prof. Adam Smith',    1990),
    (4, 'Mathematics',           'Dr. Emmy Noether',     1965),
    (5, 'Physics',               'Dr. Marie Curie',      1960);


-- ============================================================
-- SAMPLE DATA — STUDENTS
-- ============================================================

-- Insert 8 sample student records across various departments
INSERT INTO Students (student_id, first_name, last_name, email, date_of_birth, enrollment_date, department_id, gpa) VALUES
    (1001, 'Alice',   'Johnson',  'alice.johnson@uni.edu',  '2002-03-15', '2020-09-01', 1, 3.85),
    (1002, 'Bob',     'Smith',    'bob.smith@uni.edu',      '2001-07-22', '2020-09-01', 2, 3.40),
    (1003, 'Clara',   'Davis',    'clara.davis@uni.edu',    '2003-01-10', '2021-09-01', 1, 3.92),
    (1004, 'David',   'Martinez', 'david.martinez@uni.edu', '2002-11-05', '2021-09-01', 3, 3.10),
    (1005, 'Eva',     'Wilson',   'eva.wilson@uni.edu',     '2001-06-30', '2019-09-01', 4, 3.75),
    (1006, 'Frank',   'Brown',    'frank.brown@uni.edu',    '2003-08-18', '2022-09-01', 5, 3.60),
    (1007, 'Grace',   'Lee',      'grace.lee@uni.edu',      '2002-04-25', '2020-09-01', 3, 3.20),
    (1008, 'Henry',   'Taylor',   'henry.taylor@uni.edu',   '2001-12-12', '2019-09-01', 2, 3.55);


-- ============================================================
-- QUERIES
-- ============================================================

-- 1. Select all students with their full details
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    s.email,
    s.date_of_birth,
    s.enrollment_date,
    d.department_name,
    s.gpa
FROM Students s
JOIN Departments d ON s.department_id = d.department_id
ORDER BY s.last_name, s.first_name;


-- 2. Find a specific student by their ID (replace 1003 with desired ID)
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    s.email,
    s.date_of_birth,
    s.enrollment_date,
    d.department_name,
    s.gpa
FROM Students s
JOIN Departments d ON s.department_id = d.department_id
WHERE s.student_id = 1003;


-- 3. List all students enrolled in a specific department (Computer Science = 1)
SELECT
    s.student_id,
    s.first_name,
    s.last_name,
    s.email,
    s.gpa
FROM Students s
JOIN Departments d ON s.department_id = d.department_id
WHERE d.department_name = 'Computer Science'
ORDER BY s.gpa DESC;


-- 4. Update a student's email and GPA (update student ID 1002)
UPDATE Students
SET
    email = 'bob.smith_updated@uni.edu',
    gpa   = 3.65
WHERE student_id = 1002;


-- 5. Delete a student record by ID (removes student ID 1008)
DELETE FROM Students
WHERE student_id = 1008;


-- 6. Count the number of students enrolled in each department
SELECT
    d.department_name,
    COUNT(s.student_id) AS student_count
FROM Departments d
LEFT JOIN Students s ON d.department_id = s.department_id
GROUP BY d.department_id, d.department_name
ORDER BY student_count DESC;
```

## Gemini-Flash-1,5
```sql
-- ========================================================
-- 1. DATABASE SCHEMA SETUP
-- ========================================================

-- Create Departments table first (Parent Table)
CREATE TABLE Departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL,
    location VARCHAR(100)
);

-- Create Students table (Child Table)
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    dept_id INT,
    -- Links student to a department; sets to NULL if department is deleted
    CONSTRAINT fk_department 
        FOREIGN KEY (dept_id) 
        REFERENCES Departments(dept_id)
        ON DELETE SET NULL
);

-- ========================================================
-- 2. INSERT SAMPLE DATA
-- ========================================================

-- Adding Departments
INSERT INTO Departments (dept_id, dept_name, location) VALUES
(101, 'Computer Science', 'Building A'),
(102, 'Mathematics', 'Building B'),
(103, 'Physics', 'Science Lab'),
(104, 'Literature', 'Arts Wing'),
(105, 'Economics', 'Social Science Block');

-- Adding Students
INSERT INTO Students (student_id, first_name, last_name, email, dept_id) VALUES
(1, 'Alice', 'Smith', 'alice.s@university.edu', 101),
(2, 'Bob', 'Johnson', 'bjohnson@university.edu', 101),
(3, 'Charlie', 'Davis', 'charlie.d@university.edu', 102),
(4, 'Diana', 'Prince', 'diana.p@university.edu', 103),
(5, 'Ethan', 'Hunt', 'ehunt@university.edu', 105);

-- ========================================================
-- 3. FUNCTIONAL QUERIES
-- ========================================================

-- Query 1: Select all students
SELECT * FROM Students;

-- Query 2: Find a student by ID
SELECT * FROM Students WHERE student_id = 3;

-- Query 3: List students in a specific department (e.g., Computer Science)
SELECT s.first_name, s.last_name, d.dept_name 
FROM Students s
JOIN Departments d ON s.dept_id = d.dept_id
WHERE d.dept_name = 'Computer Science';

-- Query 4: Update student details (Change last name and email)
UPDATE Students 
SET last_name = 'Wayne', email = 'bruce.w@university.edu' 
WHERE student_id = 2;

-- Query 5: Delete a student record
DELETE FROM Students WHERE student_id = 4;

-- Query 6: Count number of students in each department
-- (Includes departments with 0 students using LEFT JOIN)
SELECT d.dept_name, COUNT(s.student_id) AS total_students
FROM Departments d
LEFT JOIN Students s ON d.dept_id = s.dept_id
GROUP BY d.dept_name;
```

## Deepseek r1 1.5b(Local)
```sql
-- Create Departments table
CREATE TABLE Departments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

-- Create Students table with foreign key relationship
CREATE TABLE Students (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department_id INT NOT NULL,
    enrollment_date DATE NOT NULL,
    FOREIGN KEY (department_id) REFERENCES Departments(id)
);

-- Insert sample departments
INSERT INTO Departments (name) VALUES
('Computer Science'),
('Mathematics'),
('Physics'),
('Biology'),
('Chemistry');

-- Insert sample students
INSERT INTO Students (name, email, department_id, enrollment_date) VALUES
('Alice Johnson', 'alice@uni.edu', 1, '2025-09-01'),
('Bob Smith', 'bob@uni.edu', 1, '2025-08-15'),
('Carol Davis', 'carol@uni.edu', 2, '2025-09-02'),
('David Wilson', 'david@uni.edu', 3, '2025-08-20'),
('Emma Brown', 'emma@uni.edu', 4, '2025-09-05');

-- Query 1: Select all students
SELECT * FROM Students;

-- Query 2: Find student by ID
SELECT * FROM Students WHERE id = 3;

-- Query 3: List students in a department (e.g. Computer Science)
SELECT Students.id, Students.name 
FROM Students 
JOIN Departments ON Students.department_id = Departments.id
WHERE Departments.name = 'Computer Science';

-- Query 4: Update student details (e.g. change email)
UPDATE Students SET email = 'new_email@uni.edu' WHERE id = 1;

-- Query 5: Delete a student record
DELETE FROM Students WHERE id = 5;

-- Query 6: Count students per department
SELECT Departments.name, COUNT(Students.id) AS student_count
FROM Departments
LEFT JOIN Students ON Departments.id = Students.department_id
GROUP BY Departments.name;
```