# Оцінки студентів у певній групі з певного предмета на останньому занятті.
import sqlite3

with open('query_12.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


print(execute_query(sql))
