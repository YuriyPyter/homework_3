def request():
    sum_result = 0
    """
    Функция расчёта суммы чисел с сохраняющимся результатом по запросу чисел из строки
    """
    while True:
        my_list = input('Введите числа через пробел (Enter - да / q - выйти): ').split()
        if my_list[-1] == 'q':   # условие при введении q
            if len(my_list) == 1:
                break
            elif len(my_list) != 1:  # условие при введении q последним символом
                del my_list[-1]
                my_int_sum(my_list)
                sum_result += my_int_sum(my_list)
                print(f'Сумма введеных чисел: {sum_result}')
                break
        else:                        # условие рассчёта суммы чисел
            my_int_sum(my_list)
            sum_result += my_int_sum(my_list)
            print(f'Сумма введеных чисел: {sum_result}')


def my_int_sum(numbers):
    """
    Функция оцифровки каждого элемента из списка
    """
    one_sum = 0
    for number in numbers:
        number = int(number)
        one_sum += number
    return one_sum


request()