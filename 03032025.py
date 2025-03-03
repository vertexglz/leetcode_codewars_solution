# Задачи от ментора
"""
"""
#Создайте программу, которая находит все числа в тексте.
"""
import re
s = input()
numbers_in_text = re.findall(r'\d+',s)
print (numbers_in_text)

"""
#Замените все пробелы в тексте на символ _
"""
string = input()
solution = re.sub(r'\s+','_',string)
print (solution)

"""
#Проверить является ли адрес email-ом
"""

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Тестирование
emails = ["example@example.com", "example@com", "user.name+tag+sorting@example.com"]
for email in emails:
    print(f"{email}: {'Валиден' if is_valid_email(email) else 'Невалиден'}")


"""

#codewars

#найти индексы элем массивов, которые в сумме дают таргет
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                temp = (i,j)
    return temp

#проверить валидацию пин-кода
def validate_pin(pin):
    if not len(pin) in [4,6]:
        return False
    if not pin.isdigit():
        return False
    return True