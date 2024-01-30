# -*- coding: utf-8 -*-

import csv
from datetime import datetime
import pytz

def edit_note():
    #filename = "my_notes_test"
    filename = input("Укажите название файла: ")

    # Получаем идентификатор заметки от пользователя
    note_id = input("Введите идентификатор заметки для редактирования: ")

    try:
        with open(f'{filename}.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            rows = list(reader)
            
            # Создаем временный список для хранения измененных данных
            updated_rows = []

            # Ищем заметку с введенным идентификатором
            found = False
            for row in rows:
                if row and row[0] == note_id:
                    # Найдена заметка, предлагаем пользователю внести изменения
                    new_title = input("Введите новую тему заметки: ")
                    new_body = input("Введите новое содержание заметки: ")

                    # Обновляем данные заметки
                    row[1] = new_title
                    row[2] = new_body
                    row[3] = datetime.now(pytz.timezone('Europe/Moscow')).strftime('%H:%M %d.%m.%Y')
                    updated_rows.append(row)
                    found = True
                else:
                    updated_rows.append(row)
            
            # Перезаписываем файл с обновленными данными
            if found:
                with open(f'{filename}.csv', 'w', newline='') as csvfile:
                    writer = csv.writer(csvfile, delimiter=';')
                    writer.writerows(updated_rows)
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка с указанным идентификатором не найдена.")
    except FileNotFoundError:
        print("Файл с заметками не найден.")

print("\n\n --------\n\n")
# Тестовый вызов функции
#edit_note()
""" код рабочий"""
