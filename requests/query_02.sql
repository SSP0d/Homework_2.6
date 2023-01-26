SELECT
    Students.student_name as name,
    Subjects.subjects as subject,
    ROUND(AVG(Grades.grades),2) as average
FROM
    students
LEFT JOIN
    subjects
LEFT JOIN
	grades ON students.id = grades.grades
WHERE
    subjects.id = 2
GROUP BY name
ORDER BY average DESC
LIMIT 1;