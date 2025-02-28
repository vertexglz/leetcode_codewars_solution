# Задачи от ментора
from datetime import datetime

# Вывод текущей даты
print("Текущая дата:", datetime.today())

# Запрос первой даты
first_date_str = input("Введите первую дату в формате ДД.ММ.ГГГГ: ")

# Преобразование первой даты
first_date = None
try:
    first_date = datetime.strptime(first_date_str, '%d.%m.%Y')
except ValueError:
    print("Ошибка! Первая дата введена в неверном формате.")
    exit()  # Выход из программы, если дата некорректна

# Запрос второй даты
second_date_str = input("Введите вторую дату в формате ДД.ММ.ГГГГ: ")

# Преобразование второй даты
second_date = None
try:
    second_date = datetime.strptime(second_date_str, '%d.%m.%Y')
except ValueError:
    print("Ошибка! Вторая дата введена в неверном формате.")
    exit()  # Выход из программы, если дата некорректна

# Вычисление разницы между датами
if first_date and second_date:
    difference = second_date - first_date
    print(f"Разница между датами: {difference.days} дней")
else:
    print("Одна или обе даты не были успешно определены.")



def age(birthday_date):
    if birthday_date is None:
        return

    now = datetime.now()
    
    years_difference = now.year - birthday_date.year

    has_birtday_passed = (now.month, now.day) >= (birthday_date.month,birthday_date.day)

    age = years_difference - (0 if has_birtday_passed else 1)

    print(f'Пользователю {age} лет')


birth_day = input('Введите дату рождения пользователя в форме ДД.ММ.ГГГГ: ')

birthday_date = None

try:
    birthday_date = datetime.strptime(birth_day,'%d.%m.%Y')

except ValueError:
    print("Введите дату в правильном формате")

age (birthday_date)