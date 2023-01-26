import sqlite3


with open('query_1.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../salary.db.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

print(execute_query(sql))