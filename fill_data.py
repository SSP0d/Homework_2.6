from datetime import datetime, timedelta, date
from faker import Faker
from faker.providers import BaseProvider
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 30
NUMBER_GROUPS = 3
NUMBER_TEACHERS = 5
NUMBER_SUBJECTS = 8
GRADES = 20


def generate_fake_data(number_students, number_groups, nuber_teachers, number_subjects, grades) -> tuple():
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

    # Создаем список преподавателей в количестве fake_teachers
    for _ in range(nuber_teachers):
        fake_teachers.append(fake_data.name())

        # Создаем number_subjects набор предметов
        for _ in range(number_subjects):
            fake_subjects.append(fake_data.job())

    # Создаем список оценок fake_grades
    for _ in range(grades):
        fake_grades.append(fake_data.random_int(min=1, max=12))

    return fake_students, fake_groups, fake_teachers, fake_subjects, fake_grades


def prepare_data(students, groups, teachers, subjects, grades):
    for_students = []
    # подготавливаем список кортежей имен студентов
    for student in students:
        for_students.append(student, )

    for_groups = []
    # подготавливаем список кортежей наименований групп
    for group in groups:
        for_groups.append(group, )

    for_teachers = []
    # подготавливаем список кортежей преподавателей
    for teacher in teachers:
        for_teachers.append(teacher, )

    for_subjects = []
    # подготавливаем список кортежей предметов
    for subject in subjects:
        for_subjects.append((subject, choice(teachers)))

    for_grades = []
    # подготавливаем список кортежей оценок студентов
    for month in range(1, 13):
        grade_data: date = datetime(2022, month, randint(1, 28)).date()
        for student in students:
            for_grades.append((student, choice(grades), grade_data))

    return for_students, for_groups, for_teachers, for_subjects, for_grades


def insert_data_to_db(students, groups, teachers, subjects, grades) -> None:
    # Создадим соединение с нашей БД и получим объект курсора для манипуляций с данными

    with sqlite3.connect('salary.db') as con:

        cur = con.cursor()

        '''Заполняем таблицу студентов. И создаем скрипт для вставки, где переменные, которые будем вставлять отметим
        знаком заполнителя (?) '''

        sql_to_students = """
        INSERT INTO students(students_name)
        VALUES (?)
        """

        '''Для вставки сразу всех данных воспользуемся методом executemany курсора. Первым параметром будет текст
        скрипта, а вторым данные (список кортежей).'''

        cur.executemany(sql_to_students, students)

        # Вставляем данные о группах.
        sql_to_groups = """
        INSERT INTO groups(groups_name)
        VALUES (?)
        """

        cur.executemany(sql_to_groups, groups)

        # Вставляем данные о преподавателях.
        sql_to_teachers = """
        INSERT INTO teachers(teachers_name)
        VALUES (?)
        """

        cur.executemany(sql_to_teachers, teachers)

        # Вставляем данные о предметах.
        sql_to_subjects = """
        INSERT INTO subjects(subject, teacher)
        VALUES (?, ?)
        """

        # Данные были подготовлены заранее, потому просто передаем их в функцию
        cur.executemany(sql_to_subjects, subjects)

        # И добавляем данные о оценках
        sql_to_grades = """
        INSERT INTO grades(students_name, grade, date)
        VALUES (?, ?, ?)
        """

        cur.executemany(sql_to_grades, grades)

        # Фиксируем наши изменения в БД
        con.commit()


if __name__ == "__main__":
    students, groups, teachers, subjects, grades = prepare_data(*generate_fake_data(NUMBER_STUDENTS, NUMBER_GROUPS,
                                                                                    NUMBER_TEACHERS,NUMBER_SUBJECTS,
                                                                                    GRADES))
    insert_data_to_db(students, groups, teachers, subjects, grades)