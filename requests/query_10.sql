SELECT
	s.student_name as name,
	sub.subjects
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
