"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""


def read_count(txt: str):
    with open(txt, 'r') as file:
        count = 0
        for line in file:
            count += 1
            print(f'Длина строки: {len(line)}')
            print(f'Количество слов: {len((line.strip()).split(" "))}')
        print(f'\nКоличество строк: {count}\n')


read_count("read_count.txt")