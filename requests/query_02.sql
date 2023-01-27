SELECT
	students.student_name as name,
	subjects.subjects,
	ROUND(AVG(grades.grades),2) as avg_grades
FROM
    grades
LEFT JOIN
    students ON students.id = grades.student_id
LEFT JOIN
	subjects ON subjects.id = grades.subjects_id
WHERE subjects.id = 1
GROUP BY name
ORDER BY avg_grades DESC
LIMIT 1;