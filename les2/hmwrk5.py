"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
"""
# Введем стартовый список
main_list = []

print(f"Начальный список такой маленький: \n{main_list} \nДавайте увеличим его!\nКогда надоест, введите 'end'")

# Сделаем все в цикле, чтобы пользователь мог дополнять стартовый список
while True:
    # Проверим ввод, чтобы это было число и заодно настроим выход
    digit = input('Введите число!\n')
    if digit == 'end':
        break
    elif not digit.isdigit():
        print("Ошибка! Можно добавить только число")
        continue
    elif int(digit) < 1:
        print("Ошибка! Натуральные числа больше 0")
        continue
    digit = int(digit)
    # Если это первые два числа списка, просто вставим их
    if len(main_list) == 0:
        main_list.append(digit)
    elif len(main_list) == 1:
        if digit < main_list[0]:
            main_list.append(digit)
        else:
            main_list.append(main_list[0])
            main_list[0] = digit
    # Чтобы не гонять цикл почем зря, проверим крайние положения списка.
    elif digit > main_list[0]:
        main_list.insert(0, digit)
    elif digit < main_list[-1]:
        main_list.append(digit)
    # Поищем похожие елементы и, если они есть, добавим к ним вводимое число.
    elif main_list.count(digit):
        main_list.insert((main_list.index(digit)+main_list.count(digit)), digit)
    # Ну а если ничего похожего нет, переберем список и вставим число на нужное место
    else:
        for items in range(len(main_list)):
            if main_list[items] < digit:
                main_list.insert(items, digit)
                break
    print (main_list)

print("Мы увеличили список бесплатно и без СМС")