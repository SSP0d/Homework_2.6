SELECT
    students.student_name as name,
    ROUND(AVG(grades.grades),2) as grades
FROM
    students
LEFT JOIN
    grades ON students.id = grades.grades
GROUP BY name
ORDER BY grades DESC
LIMIT 5;