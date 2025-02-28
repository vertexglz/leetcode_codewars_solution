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

# вариант от gpt
from datetime import datetime

def get_date(prompt):
    while True:
        date_str = input(prompt)
        try:
            return datetime.strptime(date_str, '%d.%m.%Y')
        except ValueError:
            print("Ошибка! Дата должна быть в формате ДД.ММ.ГГГГ.")

first_date = get_date("Введите первую дату: ")
second_date = get_date("Введите вторую дату: ")

if first_date > second_date:
    first_date, second_date = second_date, first_date  # Меняем местами, если первая дата позже второй

difference = second_date - first_date
print(f"Разница между датами: {difference.days} дней")


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

# вариант от gpt
from datetime import datetime

def calculate_age(birthday_date):
    if birthday_date > datetime.now():
        return "Ошибка! Дата рождения не может быть в будущем."
    
    now = datetime.now()
    years_difference = now.year - birthday_date.year
    has_birthday_passed = (now.month, now.day) >= (birthday_date.month, birthday_date.day)
    age = years_difference - (0 if has_birthday_passed else 1)
    return age


birth_day = input('Введите дату рождения пользователя в форме ДД.ММ.ГГГГ: ')
try:
    birthday_date = datetime.strptime(birth_day, '%d.%m.%Y')
    result = calculate_age(birthday_date)
    if isinstance(result, str):  # Проверяем, является ли результат строкой (ошибка)
        print(result)
    else:
        print(f"Пользователю {result} лет")
except ValueError:
    print("Введите дату в правильном формате")

# Задачи с codewars - leetcode

# 1 .
"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""
def to_camel_case(text):
    # Список символов-разделителей
    declamers = '.,-_;$!@#%^&*'
    
    # Удаляем все специальные символы из строки
    for char in declamers:
        text = text.replace(char, ' ')
    
    # Разделяем строку на слова
    words = text.split()
    
    if not words:  # Если список пустой, возвращаем пустую строку
        return ''
    
    # Сохраняем первый элемент без изменения регистра
    result = [words[0]]  # Первое слово остается без изменений
    
    # Преобразуем остальные элементы с заглавной буквы
    result += [word.capitalize() for word in words[1:]]
    
    # Соединяем слова обратно в одну строку
    return ''.join(result)

# Лучший вариант решения
def to_camel_case(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0]+ ''.join([x.capitalize() for x in removed[1:]])

#вариант от gpt
import re

def to_camel_case(text):
    words = re.sub(r'[^A-Za-z0-9]+', ' ', text).split()
    if not words:
        return ''
    return words[0] + ''.join(word.capitalize() for word in words[1:])

# 2
"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
 

Constraints:

1 <= s.length <= 105
s[i] is a printable ascii character.
"""

class Solution:
    def reverseString(self, s: list) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    
# вызов
solution = Solution()

# Тестируем метод
input_list = ['h', 'E', 'L', 'L', 'O']
solution.reverseString(input_list)
print(input_list)

#вариант от gpt
class Solution:
    def reverseString(self, s: list) -> None:
        s[:] = s[::-1]
