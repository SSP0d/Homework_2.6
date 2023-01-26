SELECT
    students.student_name,
    ROUND(AVG(grades.grades),2) as average
FROM
    students
LEFT JOIN
    grades ON students.id = grades.student_id
GROUP BY student_name
ORDER BY average DESC
LIMIT 5;