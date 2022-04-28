types = ['Max', 4, 3.14, ['he', 'she'], True, {3, 4}, ('y', 'e', 's'), {'apple': 'яблоко'}]
for i, value in enumerate(types, 1):
    print(f"{value} - {type(value)}")
