# -*- coding: utf-8 -*-

# Вывод заметики

import csv
#from datetime import datetime
#import pytz

def check_note():
    #filename = "my_notes_test"
    filename = input("ВВедите название фала с заметками: ")
    # Получаем идентификатор заметки от пользователя
    note_id = input("Введите идентификатор заметки для просмотра: ")

    try:
        with open(f'{filename}.csv', 'r', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            rows = list(reader)
            
            # Создаем временный список для хранения данных
            storage_rows = []

            # Ищем заметку с введенным идентификатором
            found = False
            for row in rows:
                if row and row[0] == note_id:
                    print("Заметка найдена:")
                    print("Заголовок:", row[1])
                    print("Тело заметки:", row[2])
                    print("Время и дата:", row[3])
                    found = True
                else:
                    storage_rows.append(row)
                    
            if found == True:
                print("Заметка существует :)")
            else:
                print("Заметки не существует в файле :( ")
            
    except FileNotFoundError:
        print("Файл с заметками не найден.")

print("\n\n --------\n\n")
# Тестовый вызов функции
#check_note()
"""код рабочий"""


