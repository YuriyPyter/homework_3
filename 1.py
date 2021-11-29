def share(a, b):
    if b == 0:
        print('Вы инициативый - деление на ноль!')
    return a / b


print(share(
    int(input('Введите первое число: ')),
    int(input('Введите второе число: '))
))
