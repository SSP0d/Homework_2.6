SELECT
	grades.grades
FROM
	grades
LEFT JOIN
	groups ON groups.id = student_id
LEFT JOIN
	subjects ON subjects_id = grades.subjects_id
WHERE
	groups.id = 1 AND subjects.id = 2