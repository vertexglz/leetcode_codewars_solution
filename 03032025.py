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


def two_sum(numbers, target):
    temp = []
    for i in range(len(numbers)):
        for j in range(1,len(numbers)):
            if numbers[i] + numbers[j] == target and i != j:
                temp.append ([i,j])
    return temp

print(two_sum ([1,2,3],4))