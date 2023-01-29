SELECT
	s.student_name,
	sub.subjects,
	gr.groups,
	g.date_of,
	g.grades
FROM
	grades g
LEFT JOIN
	students s ON s.id = g.id
LEFT JOIN
	groups gr ON gr.id = s.id
LEFT JOIN
	subjects sub ON sub.id = g.id
WHERE gr.id  = 1 AND sub.id = 1 AND g.date_of = (
	SELECT g.date_of
	FROM
		grades g
	LEFT JOIN
		students s ON s.id = g.id
	LEFT JOIN
		groups gr ON gr.id = s.id
	WHERE
		s.id = 1 AND gr.id = 1
	ORDER BY g.date_of DESC
	LIMIT 1
)
ORDER BY g.date_of DESC