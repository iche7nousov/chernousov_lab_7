#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    dicktory = {"Фамилия": [], "Имя" : [], "Знак Зодиака": [], "Дата рождения": []}

    while True:
        command = input(">>> ").lower()

        if command == "list":
            print(dicktory)

        if command == "add":
            print(dicktory)

            family = input("Фамилия: ").capitalize()
            name = input("Имя: ").capitalize()
            date = input("Дата рождения: ")

            dicktory["Фамилия"].append(family)
            dicktory["Имя"].append(name)
            dicktory["Дата рождения"].append(date)

            day = int(date[0:2])
            mounth = int(date[3:5])

            if mounth == 1:
                if day <= 20:
                    zodiak = "Козерог"
                elif day >= 21:
                    zodiak = "Водолей"

            elif mounth == 2:
                if day >= 21:
                    zodiak = "Рыбы"
                elif day <= 20:
                    zodiak = "Водолей"

            elif mounth == 3:
                if day <= 20:
                    zodiak = "Рыбы"
                elif day >= 21:
                    zodiak = "Овен"

            elif mounth == 4:
                if day >= 21:
                    zodiak = "Телец"
                elif day <= 20:
                    zodiak = "Овен"

            elif mounth == 5:
                if day >= 21:
                    zodiak = "Близнецы"
                elif day <= 20:
                    zodiak = "Близнецы"

            elif mounth == 6:
                if day >= 21:
                    zodiak = "Рак"
                elif day <= 20:
                    zodiak = "Телец"
            elif mounth == 7:
                if day >= 21:
                    zodiak = "Лев"
                elif day <= 20:
                    zodiak = "Рак"
            elif mounth == 8:
                if day >= 21:
                    zodiak = "Дева"
                elif day <= 20:
                    zodiak = "Лев"
            elif mounth == 9:
                if day >= 21:
                    zodiak = "Весы"
                elif day <= 20:
                    zodiak = "Дева"
            elif mounth == 10:
                if day >= 21:
                    zodiak = "Скорпион"
                elif day <= 20:
                    zodiak = "Весы"
            elif mounth == 11:
                if day >= 21:
                    zodiak = "Стрелец"
                elif day <= 20:
                    zodiak = "Скорпион"
            elif mounth == 12:
                if day >= 21:
                    zodiak = "Козерог"
                elif day <= 20:
                    zodiak = "Стрелец"
            dicktory["Знак Зодиака"].append(zodiak)
            print(dicktory)
