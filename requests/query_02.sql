SELECT
	students.student_name as student,
	subjects.subjects,
	ROUND(AVG(grades.grades, 2)) as average

FROM students

LEFT JOIN
	subjects s ON subjects.id = grades.subjects_id

LEFT JOIN
	grades g ON students.id = grades.student_id

WHERE grades.subjects_id = 1

GROUP BY student
ORDER BY average
LIMIT 1;