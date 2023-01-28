SELECT
	students.student_name
FROM
	students
LEFT JOIN
	groups ON groups.id = students.id
WHERE group_id = 1;