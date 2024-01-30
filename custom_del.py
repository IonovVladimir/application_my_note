# -*- coding: utf-8 -*-

# Удаление заметки

import csv
#from datetime import datetime
#import pytz

def delete_note():
    filename = "my_notes_test"

    # Получаем идентификатор заметки от пользователя
    note_id = input("Введите идентификатор заметки для удаления: ")

    try:
        with open(f'{filename}.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            rows = list(reader)
            
            # Создаем временный список для хранения неподходящих данных
            remaining_rows = []

            # Ищем заметку с введенным идентификатором
            found = False
            for row in rows:
                if row and row[0] == note_id:
                    print("Заметка для удаления найдена:")
                    print("Тема:", row[1])
                    print("Содержание:", row[2])
                    print("Дата и время:", row[3])
                    found = True
                else:
                    remaining_rows.append(row)
            
            # Перезаписываем файл с оставшимися данными
            if found:
                confirmation = input("Вы уверены, что хотите удалить эту заметку? (yes/no): ")
                if confirmation.lower() == 'yes':
                    with open(f'{filename}.csv', 'w', newline='') as csvfile:
                        writer = csv.writer(csvfile, delimiter=';')
                        writer.writerows(remaining_rows)
                    print("Заметка успешно удалена.")
                else:
                    print("Удаление отменено.")
            else:
                print("Заметка с указанным идентификатором не найдена.")
    except FileNotFoundError:
        print("Файл с заметками не найден.")

print("\n\n --------\n\n")
# Тестовый вызов функции
#delete_note()
"""код вроде рабочий"""

