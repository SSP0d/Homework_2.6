import sqlite3


# Знайти студента із найвищим середнім балом з певного предмета.
sql = """
SELECT
	students.student_name as student,
	subjects.subjects,
	ROUND(AVG(grades.grades, 2)) as average

FROM students

LEFT JOIN
	subjects s ON subjects.id = grades.subjects_id 
	
LEFT JOIN 
	grades g ON students.id = grades.student_id
	
WHERE grades.subjects_id = 1

GROUP BY student
ORDER BY average
LIMIT 1;

"""


def execute_query(sql: str) -> list:
    with sqlite3.connect('../salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


print(execute_query(sql))