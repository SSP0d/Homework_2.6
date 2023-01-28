# Знайти оцінки студентів у окремій групі з певного предмета.
import sqlite3

with open('query_07.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


print(execute_query(sql))