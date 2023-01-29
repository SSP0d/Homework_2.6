SELECT
	s.student_name as name,
	t.teachers_name as teacher,
	ROUND(AVG(g.grades), 2) as avg_grade
FROM
	grades g
LEFT JOIN
	students s ON s.id = g.id
LEFT JOIN
	subjects sub ON sub.id = g.id
LEFT JOIN
	teachers t ON t.id = sub.id
WHERE
	s.id = 5 AND t.id = 5
