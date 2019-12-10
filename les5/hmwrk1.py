"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def create_input():
    with open("create_input.txt", "w") as file:
        while True:
            txt = f'{input("Введите текст:")}\n'
            if txt == '\n':
                break
            else:
                file.write(txt)

