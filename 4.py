def my_func(x, y):
    """
    Функция возведения числа в отрицательную степень
    """
    rez_x = 1
    for i in range(abs(y)):  # взятие по модулю
        rez_x *= x
    result = 1 / rez_x
    print(result)


my_func(
    float(input('Введите действительное положительное число: ')),
    int(input('Введите целое отрицательное число: '))
)
