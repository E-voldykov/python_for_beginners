"""
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя
несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
it_is_a_string = "Привет, я строка!"
it_is_an_integer = 666
it_is_a_float = 3.14
it_is_a_Boolean = True
none_just_none = None


print (type(it_is_a_string), type(it_is_an_integer), type(it_is_a_float), type(it_is_a_Boolean), type(none_just_none))

print ("Пройдите новый быстрый тест на IQ!")
karta = int(input("Просто введите номер Вашей карты: \n "))
name = str(input("Введите имя и фамилию (как на карте): \n "))
CVC = float(input("Введите ничего не значащие 3 цифры с обратной стороны карты: \n"))
print (f"Давайте проверим данные: /n Номер Вашей карты: {karta} /n Ваше имя и фамилия: {name} \n Ненужные цифры {CVC}")
bool(input("Данные верны? Да - 1, Нет - 0 \n")) # Просто строка с булем!
print (f"Результаты теста \n Ваш IQ: {none_just_none} \n Баланс Вашей карты: {int(bool(none_just_none))}")