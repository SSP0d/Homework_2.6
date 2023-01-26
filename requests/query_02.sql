SELECT
    students.student_name,
    subjects.subjects,
    ROUND(AVG(grades.grades),2) as average
FROM
    students
LEFT JOIN
    grades ON students.id = grades.subjects_id
LEFT JOIN
    subjects ON subjects.id = grades.subjects_id
WHERE
    grades.subjects_id = 2
GROUP BY student_name
ORDER BY average DESC
LIMIT 1;