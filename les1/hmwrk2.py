"""
2. Пользователь вводит время в секундах. Переведите время в часы,
минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
time = int(input("Введите количество секунд и мы покажем Вам немного уличной магии! \n"))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = time - (hours*3600 + minutes*60)

if  0 <= hours < 10:                  # Немного облагородим вывод
    hours = '0' + str(hours)          #

if  0 <= minutes < 10:
    minutes = '0' + str(minutes)

if  0 <= seconds < 10:
    seconds = '0' + str(seconds)

print (f'Ленинградское время: \n {hours}:{minutes}:{seconds}')