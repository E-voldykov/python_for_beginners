"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
biggest, easter, count = 0, 0, 0

while True:
    if easter == 6: print ("Я могу требовать это БЕСКОНЕЧНО, а ты?")
    print ("Введи ПОЛОЖИТЕЛЬНОЕ ЦЕЛОЕ ЧИСЛО, и не вздумай обманывать! \n ")
    number = int(input())
    easter +=1
    print (easter)
    # if type (number) == str:
    #     sprint ("ЧИСЛО! Ты знаешь, что это такое?")
    #     continue
    # elif type (number) == bool or type (number) is None:
    #     print ("Слушай, давай без экзотики, самый умный что ли?")
    #     continue
    # elif type (number) == float:
    #     print ("ЦЕЛОЕ! Ну хотя бы это число! Так и быть, округлю для тебя, дружочек!")
    #     number = int(number)
    #     continue
    if number <= 0:
        print ("Больше 0! Или ты случайно ввел свой IQ? Мои соболезнования...")
        continue
    elif number > 0:
        print ('Какой внимательный пользователь, сейчас найдем самую большую цифирку!')
        break

number = str(number)

while count < len(number):
    if biggest <= int(number[count]): biggest = int(number[count])
    count += 1

print (f'ТАДААААМ наибольшая цифра в числе - {biggest}!')
