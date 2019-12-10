"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def txtsum():
    name = input("Введите название файла:\n")
    with open(f'{name}.txt', 'a') as file:
        while True:
            number = input("Введите целое число, чтобы выйти просто нажмите Enter:\n")
            if not number:
                break
            else:
                number = f'{number} '
                file.write(number)
    print("А теперь посчитаем сумму:\n")
    with open(f'{name}.txt', 'r') as file:
        file = file.read()
        print(sum([int(i) for i in file[:-1].split(" ")]))


txtsum()
