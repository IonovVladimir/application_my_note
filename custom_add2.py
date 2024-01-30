# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import pytz

def new_notes():
    #filename = "my_notes_test"
    filename= input("Укажите название файла: ")
    id_notes = None
    title_notes = input("Укажите тему заметки: ")
    note_body = input("Укажите содержание заметки: ")

    # Открываем файл для проверки существующих записей и определения нового id
    try:
        with open(f'{filename}.csv', 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            rows = list(reader)
            if len(rows) > 1:  # Проверяем, есть ли заголовок и какие-либо записи
                last_id = int(rows[-1][0])  # Получаем последний id
                id_notes = last_id + 2  # Уникальный id как будто бы
            else:
                id_notes = 1  # Если файл пуст, начинаем с id=1
    except FileNotFoundError:
        id_notes = 1  # Если файл не существует, начинаем с id=1

    if id_notes and title_notes and note_body:
        date_and_time = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M %d.%m.%Y')

        try:
            with open(f'{filename}.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=";")
                if csvfile.tell() == 0:  # Если файл пустой, добавляем заголовок
                    writer.writerow(['Id_note', 'title_notes', 'note_body', 'time_and_date'])
                writer.writerow([id_notes, title_notes, note_body, date_and_time])
                print("Заметка успешно добавлена.")
        except Exception as e:
            print(f"Произошла ошибка при записи заметки: {e}")
    else:
        print("Ошибка: Необходимо заполнить все поля заметки.")

print("\n\n --------\n\n")
# Тестовый вызов функции
#new_notes()
"""этот код рабочий"""

