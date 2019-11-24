"""
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
например название, а значение — список значений-характеристик, например список названий товаров.
"""
goods = []
count = 0
info = [{"good": "Товар"},
        {"price": "Цена"},
        {"pcs": "Количество"},
        {"msr": "Единица измерения"}]
# Создаем цикл для заполнения карточки товара
while True:
    print("Заполните карточку товара:")
    good_info = {}
    count += 1
    # Создаем словарь вводимыми данными и добавляем в него номер через счетчик
    for item in info:
        card = input(item[tuple(item)[0]])
        if card.isdigit():
            card = int(card)
        good_info[item[tuple(item)[0]]] = card
    good_info = (count, good_info)
    goods.append(good_info)
    end = input("Добавить еще один товар? y-да, n-нет")
    if end == "n":
        break
    else:
        continue
print(f'Список товаров:\n{goods}')

# Создаем словарь для аналитики
analytics = {}
for item in info:
    analytics[item[tuple(item)[0]]] = []

# Заполняем его
for number, item in goods:
    for char in tuple(item):
        analytics[char].append(item[char])

# Сортируем и удаляем дубликаты
for key in analytics:
    analytics[key] = set(analytics[key])
    analytics[key] = list(analytics[key])
    analytics[key] = sorted(analytics[key])

print(f'Анализ товара: \n{analytics}')
