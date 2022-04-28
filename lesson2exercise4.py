user_input = input('Введите строку из нескольких слов, разделённых пробелами').split()
for i, letter in enumerate(user_input, 1):
    print(f'{i}. {letter[:10]}')
