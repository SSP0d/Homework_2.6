from datetime import datetime
from faker import Faker
from faker.providers import BaseProvider
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_SUBJECTS = 8
NUMBER_TEACHERS = 5
GRADES = 20


def generate_fake_data(number_students, number_groups, number_subjects, nuber_teachers, grades) -> tuple():
    fake_students = []  # здесь будем хранить студентов
    fake_groups = []  # здесь будем хранить группы
    fake_subjects = []  # здесь будем хранить предметы
    fake_teachers = [] # здесь будем хранить преподавателей
    fake_grades = [] # здесь будем хранить оценки
    '''Возьмём три компании из faker и поместим их в нужную переменную'''
    fake_data = Faker()

    # Создадим список студентов в количестве number_students
    for _ in range(number_students):
        fake_students.append(fake_data.name())

    # Сгенерируем теперь number_groups количество групп'''
    for _ in range(number_groups):
        fake_groups.append(fake_data.job())

    # Создаем number_subjects набор предметов
    for _ in range(number_subjects):
        fake_subjects.append(fake_data.job())

    # Создаем список преподавателей количестве fake_teachers
    for _ in range(nuber_teachers):
        fake_teachers.append(fake_data.name())

    # Создаем список оценок fake_grades
    for _ in range(grades):
        fake_grades.append(fake_data.random_int(min=1, max=12))

    return fake_students, fake_groups, fake_subjects


def prepare_data(students, groups, subjects, teachers, grades) -> tuple():
    for_students = []
    # подготавливаем список кортежей имен студентов
    for student in students:
        for_students.append(student, )

    for_groups = []
    # подготавливаем список кортежей наименований групп
    for group in groups:
        for_groups.append(group, )

    for_subjects = []
    # подготавливаем список кортежей предметов
    for subject in subjects:
        for_subjects.append(subject, )


    for emp in groups:
        '''
        Для записей в таблицу сотрудников нам надо добавить должность и id компании. Компаний у нас было по умолчанию
        NUMBER_COMPANIES, при создании таблицы companies для поля id мы указывали INTEGER AUTOINCREMENT - потому каждая
        запись будет получать последовательное число увеличенное на 1, начиная с 1. Потому компанию выбираем случайно
        в этом диапазоне
        '''
        for_employees.append((emp, choice(teachers), randint(1, NUMBER_STUDENTS)))

    '''
    Похожие операции выполним и для таблицы payments выплаты зарплат. Примем, что выплата зарплаты во всех компаниях
    выполнялась с 10 по 20 числа каждого месяца. Вилку зарплат будем генерировать в диапазоне от 1000 до 10000 у.е.
    для каждого месяца, и каждого сотрудника.
    '''
    for_payments = []

    for month in range(1, 12 + 1):
        # Выполняем цикл по месяцам'''
        payment_date = datetime(2021, month, randint(10, 20)).date()
        for emp in range(1, NUMBER_GROUPS + 1):
            # Выполняем цикл по количеству сотрудников
            for_payments.append((emp, payment_date, randint(1000, 10000)))

    return for_students, for_employees, for_payments


def insert_data_to_db(companies, employees, payments) -> None:
    # Создадим соединение с нашей БД и получим объект курсора для манипуляций с данными

    with sqlite3.connect('salary.db') as con:

        cur = con.cursor()

        '''Заполняем таблицу компаний. И создаем скрипт для вставки, где переменные, которые будем вставлять отметим
        знаком заполнителя (?) '''

        sql_to_companies = """INSERT INTO companies(company_name)
                               VALUES (?)"""

        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет текст
        скрипта, а вторым данные (список кортежей).'''

        cur.executemany(sql_to_companies, companies)

        # Далее вставляем данные о сотрудниках. Напишем для него скрипт и укажем переменные

        sql_to_employees = """INSERT INTO employees(employee, post, company_id)
                               VALUES (?, ?, ?)"""

        # Данные были подготовлены заранее, потому просто передаем их в функцию

        cur.executemany(sql_to_employees, employees)

        # Последней заполняем таблицу с зарплатами

        sql_to_payments = """INSERT INTO payments(employee_id, date_of, total)
                              VALUES (?, ?, ?)"""

        # Вставляем данные о зарплатах

        cur.executemany(sql_to_payments, payments)

        # Фиксируем наши изменения в БД

        con.commit()


if __name__ == "__main__":
    companies, employees, posts = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS, NUMBER_POST))
    insert_data_to_db(companies, employees, posts)