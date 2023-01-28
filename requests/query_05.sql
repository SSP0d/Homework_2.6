SELECT
	t.teachers_name,
	s.subjects
FROM
	subjects s
LEFT JOIN
	teachers t ON t.id  = s.teachers_id
WHERE t.id  = 5;