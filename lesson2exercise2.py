my_list = input('Введите знаменитое выражение').split()
print('А теперь что получится если переставить первое и второе слово в каждой паре:)')
for i in range (1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
new_list = " ".join(my_list)
print(new_list)