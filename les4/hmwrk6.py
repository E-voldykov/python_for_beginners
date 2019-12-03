"""
Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
"""


# Немного не понял как именно нужно оформить задание, оформил как функции с выводом

def inf_numbers():
    from itertools import count
    start = input('Введите начальное целое число:\n')
    for number in count(start=int(start), step=1):
        print(number)


def inf_elements():
    from itertools import cycle
    start_list = input("Введите элементы списка через пробел:\n")
    start_list = start_list.split(' ')
    for element in cycle(start_list):
        print(element)
