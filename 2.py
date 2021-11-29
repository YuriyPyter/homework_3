def data(name, surname, year_of_birth, email, phone):
    return name, surname, year_of_birth, email, phone


print(type(data))
print(data(
    input('Введите имя: '),
    input('Введите фамилию: '),
    input('Введите год рождения: '),
    input('Введите email: '),
    input('Введите телефон: ')
))