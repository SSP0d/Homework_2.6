SELECT
    s.student_name as name,
    ROUND(AVG(g.grades),2) as avg_grades
FROM
    grades g
LEFT JOIN
    students s ON s.id = g.student_id
GROUP BY name
ORDER BY avg_grades DESC
LIMIT 5;