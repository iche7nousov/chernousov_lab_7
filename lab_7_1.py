"""
 Решите задачу: создайте словарь, связав его с переменной school , и наполните данными,
которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
(удален) другой класс. Вычислите общее количество учащихся в школе
"""

import random
if __name__ == "__main__":

    school = {"1А": 32, "1Б": 31, "1В": 19}

    while True:
        command = input(">>> ").lower()
        # Узнать количество участников
        if command == "all":
            print(school)
            all_student = 0

            for i in school.values():
                all_student += i

            print(all_student)
        # Изменить кол-во учеников
        if command == "student":
            print(school)
            search_class = input("Введите название класса: ")
            school[search_class] = int(input("Введите количество учеников: "))
            print("Вы изменили количество учеников в ", search_class, school)

        # Добавить класс
        elif command == "add":
            new_class = input("Введите номер класса: ")
            if new_class[0].isdigit() and int(new_class[0]) >= 1 and int(new_class[0]) <= 11:
                new_class += input("Введите букву класса: ").upper()
                school[new_class[0:2]] = random.randint(15, 30)
                print("Новый класс был добавлен", school)
            else:
                print("Такого класса быть не может")

        # Убрать класс
        elif command == "delete":
            print(school)

            del_class = input("Введите номер и букву класса: ")
            school.pop(del_class)
            print("Был ликвидирован класс - ", del_class[0:2], school)

        # Завершить программу
        elif command == "exit":
            break

        # Если введенный текст не соответствует команде
        else:
            print("Неизвестная команда")