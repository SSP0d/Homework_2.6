-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name VARCHAR(255) NOT NULL,
    group_id INTEGER,
    FOREIGN KEY (group_id) REFERENCES groups(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    groups VARCHAR(255) NOT NULL
);

-- Table: teachers
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    teachers_name VARCHAR(255) NOT NULL
);

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    subjects VARCHAR(255) NOT NULL,
    teachers_id INTEGER,
    FOREIGN KEY (teachers_id) REFERENCES teachers (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Table: grades
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    grades INTEGER,
    subjects_id INTEGER,
    date_of DATE NOT NULL,
    student_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students (id)
    FOREIGN KEY (subjects_id) REFERENCES subjects (id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);