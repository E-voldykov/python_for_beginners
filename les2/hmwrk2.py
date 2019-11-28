"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""
count = 0
elements = []

while True:
    count += 1
    element = input(f"Введите элемент списка №{count}: \n")
    elements.append(element)

    while True:                                                            
        abort = input("Добавить новый элемент в список? Y - yes, N - no")
        if abort == 'Y' or abort == 'y':                                   # Как сократить эту запись?
            break
        elif abort == 'N' or abort == 'n':
            break
        else:
            print('Неправильная команда, попробуйте снова!')
    if abort == 'N' or abort == 'n':
        break

print(f'Ваш список:{elements} \nТеперь поменяем местами пары элементов:')

for items in range(len(elements))[1::2]:                                  #
    elements[items], elements[items - 1] = elements[items - 1], elements[items]

print(f'Измененный список: {elements}')
