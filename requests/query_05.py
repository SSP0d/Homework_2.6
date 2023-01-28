# Знайти які курси читає певний викладач.
import sqlite3

with open('query_05.sql', 'r') as query:
    sql = query.read()


def execute_query(sql: str) -> list:
    with sqlite3.connect('../salary.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


print(execute_query(sql))