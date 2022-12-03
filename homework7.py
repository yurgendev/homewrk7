# 1. Напишіть програму, яка порахує скільки літер «b» у введеному рядку тексту.
import string

text1 = 'bbbbbbbbbbbbbbbbbbbbbaslkdljasjd'
print(text1.count('b'))
import math

# 2. Користувач вводить з клавіатури ім'я людини.
# Написати програму для перевірки введеного ім'я на валідність
# (мається на увазі, що, наприклад, в імені людини не може бути цифр,
# воно повинно починатися з великої літери, за якою повинні йти маленькі).


name = input('enter your name: ')
for i in string.punctuation:
    name = name.replace(i, '')
res = ''.join([j for j in name if not j.isdigit()])
print(str.capitalize(res))

# 3. Напишіть програму, яка обчислить суму всіх кодів символів рядка.

print(sum(map(ord, input('enter elements for count: '))))

# 4. Виведіть на екран 10 рядків із значенням числа Pi.
# У першому рядку має бути 2 знаки після коми, у другому 3 і так далі.
import math

k = 0

for k in range(10):
    k += 2
    print(round(math.pi, k))

# #5 Вводиться з клавіатури користувачем текст. Знайти в ньому найдовше слово та вивести його на екран.
text2 = input('longest word check ')
print(max(text2.split(), key=len))
