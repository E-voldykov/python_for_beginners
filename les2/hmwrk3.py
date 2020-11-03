"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."
"""

months_list = ["январь", "февраль", "март",
               "апрель", "май", "июнь",
               "июль", "август", "сентябрь",
               "октябрь", "ноябрь", "декабрь"]

# Создаем список времен года и соответствующих им порядковых номеров месяцев
seasons_list = ["зима", 12, 1, 2, "весна", 3, 4, 5, "лето", 6, 7, 8, "осень", 9, 10, 11]

# Ввод нужного месяца и проверка введенной информации
while True:
    month = input("Введите порядковый номер месяца (от 1 до 12): \n")
    if not month.isdigit() or not (0 < int(month) < 13):
        print("Ошибка!")
        continue
    else:
        break

# Определение сезона - гоним цикл по списку "seasons_list" назад, когда находим время года - выходим из цикла
for season in seasons_list[seasons_list.index(int(month))::-1]:
    if type(season) == str:
        break

# Выводим решение с помощью списка
print(f'\n{month} месяц это {months_list[(int(month) - 1)]}, а время года - {season}!\n')

# На основе списка времен года создадим словарь времен года, где номер - ключ, время года - значение
seasons_dict = {}
season_key = 0
season_item = ""

for season in seasons_list:
    if type(season) == str:
        season_item = season
    if type(season) == int:
        season_key = season
        seasons_dict[season_key] = season_item

# Выводим решение с помощью словаря
print(f'Согласно словарю {month} месяц приходится на следующее время года: {seasons_dict.get(int(month))}!')

