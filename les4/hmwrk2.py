"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
"""
# Так как мы не знаем предыдущего числа, первый элемент не выводится.

numbers = [1, 4, 3, 9, 10, 5, 45, 15, 88]

numbers_gen = [numbers[el] for el in range(1, len(numbers)) if numbers[el] > numbers[el - 1]]

for item in numbers_gen:
    print(item, end=" ")
