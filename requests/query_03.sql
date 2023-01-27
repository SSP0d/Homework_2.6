SELECT
	groups.groups as Groups,
	subjects.subjects,
	ROUND(AVG(grades.grades),2) as avg_grades
FROM
    grades
LEFT JOIN
    students ON students.id = grades.student_id
LEFT JOIN
	subjects ON subjects.id = grades.subjects_id
LEFT JOIN groups ON groups.id  = students.group_id
WHERE subjects.id = 1
GROUP BY Groups
ORDER BY avg_grades DESC;