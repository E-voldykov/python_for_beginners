"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(number1, number2, number3):
    func = [number1, number2, number3]
    func.remove(min(func))
    return sum(func)
