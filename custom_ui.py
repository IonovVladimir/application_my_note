# -*- coding: utf-8 -*-

from custom_add2 import new_notes
from custom_redact3 import edit_note
from custom_del import delete_note
from custom_check_note import check_note 

def check_number(n):
    while n < 1 or n > 5:
        n = int(input("Ошибка, такого номера команды не "
                      "существует! Введите цифру от 1 до 3\n"
                      "Выберите функцию:\n"
                      "1. Добавить заметку или создать новый файл с заметкой \n"
                      "2. Изменить по идентификатору \n"
                      "3. Удалить по идентификатору \n"
                      "4. Вывод заметки по идентификатору\n"
                      "5. Выход \n"                                            
                      "Введите номер команды: "))
                      
    return n


def start_menu():
    command = None
    while command != 5:
        command = int(input("Доброго времени суток!\n"
                            "Выберите функцию:\n"
                            "1. Добавить заметку или создать новый файл с заметкой \n"
                            "2. Изменить по идентификатору \n"
                            "3. Удалить по идентификатору \n"
                            "4. Вывод заметки по идентификатору\n"
                            "5. Выход \n"                                                  
                            "Введите номер команды: "))
        command = check_number(command)
        if command == 1:
            new_notes()
        elif command == 2:
            edit_note()
        elif command == 3:
            delete_note()
        elif command == 4:
            check_note()
        
    print("Спасибо, что воспользовались нашими услугами!\n"
          "Всего доброго :)")

print("\n\n --------\n\n")