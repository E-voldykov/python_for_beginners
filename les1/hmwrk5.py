"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
print ('Займемся скукотой!')
revenue = float(input("Введи выручку:\n"))
loss = float(input("Введи убытки: \n"))

if revenue > loss: print ('Ты на коне! Все ОК, бабки не проблема!')
elif revenue == loss: print ('Идеальный баланс, Танос гордится тобой!')
else: print ('Твой бизнес интересен только налоговой!')

if ((revenue - loss) > 0) == True:
    print (f'Рентабельность успешного успеха: {revenue / (revenue-loss)} ')
    soul = int(input("Укажите количество работящих крепостных душ: \n"))
    print (f'Каждый заработал целых {(revenue / (revenue-loss)) / soul} рублей!')