number = int(input('Введите целое положительное число: '))
max_number = 0
while number > 0:
    min_number = number % 10
    if min_number >= max_number: max_number = min_number
    number//=10
print("Наибольшая цифра в числе -", max_number)
