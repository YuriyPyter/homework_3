def my_func(a, b, c):
    min_value = min(a, b, c)
    summa = sum([a, b, c]) - min_value
    print(summa)


my_func(
    int(input('Введите первое число: ')),
    int(input('Введите второе число: ')),
    int(input('Введите второе число: '))
)
