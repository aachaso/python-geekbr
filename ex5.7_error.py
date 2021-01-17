try:
    with open('file_two.txt') as f:
        data = f.read()
except IOError:
    print('Произошла ошибка ввода/вывода')
except FileNotFoundError:
    print('Произошла ошибка файла')

print(data)