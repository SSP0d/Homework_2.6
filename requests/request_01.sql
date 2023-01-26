SELECT
    student.name,
    ROUND(AVG(grade.grade),2) as average
FROM
    student
LEFT JOIN
    grade ON student.id = grade.student_id
GROUP BY name
ORDER BY average DESC
LIMIT 5;