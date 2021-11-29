def int_func():
    my_words = input('Введите слова из маленьких латинских букв: ').split()
    my_list = []
    for el in my_words:
        my_list.append(el.title())
    print(my_list)


int_func()