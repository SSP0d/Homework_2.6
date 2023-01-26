SELECT
    students.name,
    ROUND(AVG(grades.grade),2) as average
FROM
    students
LEFT JOIN
    grade ON students.id = grades.student_id
GROUP BY name
ORDER BY average DESC
LIMIT 5;