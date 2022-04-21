revenue = int(input('Введите значение выручки фирмы: '))
costs = int(input('Введите значение издержек фирмы: '))
if revenue >= costs:
    print ("Вы получили прибыль!")
    profit = revenue // costs
    print("Рентабельность выручки:", profit)
    staff = int(input('Сколько у Вас сотрудников: '))
    profit_per_staff = revenue // staff
    print("Прибыль фирмы в расчёте на одного сотрудника: ", profit_per_staff)
else:
    print("У вас убыток:(")
