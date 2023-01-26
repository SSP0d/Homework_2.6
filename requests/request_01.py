import sqlite3


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
sql = """
SELECT
    students.student_name,
    ROUND(AVG(grades.grades),2) as average
FROM
    students
LEFT JOIN
    grades ON students.id = grades.grades
GROUP BY student_name
ORDER BY average DESC
LIMIT 5;
"""


def execute_query(sql: str) -> list:
    with sqlite3.connect('../salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


print(execute_query(sql))