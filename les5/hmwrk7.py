"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список.
Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""


def saldo(txt: str):
    import json
    delta_dict = {}
    success_count = 0
    success_sum = 0
    with open(txt, "r") as file:
        for firm in file:
            firm = firm.split(" ")
            delta_dict[firm[0]] = int(firm[2]) - int(firm[3])
            if delta_dict[firm[0]] >= 0:
                success_count += 1
                success_sum += delta_dict[firm[0]]
    average_list = [delta_dict, {"average_profit": (success_sum / success_count)}]
    with open("firm_saldo.json", "w") as file:
        json.dump(average_list, file)


saldo("firms.txt")