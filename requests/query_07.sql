SELECT
	students.student_name as name,
	groups.groups,
	subjects.subjects,
	grades.grades
FROM
	grades
LEFT JOIN
	subjects ON subjects_id = grades.subjects_id
LEFT JOIN
	students ON students.id = grades.id
LEFT JOIN
	groups ON groups.id = student_id
WHERE
	groups.id = 1 AND subjects.id = 5
ORDER BY name DESC