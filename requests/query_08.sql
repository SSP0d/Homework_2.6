SELECT
	t.teachers_name,
	ROUND(AVG(g.grades), 2) as avg_grade
FROM
	grades g
LEFT JOIN
	subjects s ON s.id = g.id
LEFT JOIN
	teachers t ON t.id = s.id
WHERE
	t.id = 1
