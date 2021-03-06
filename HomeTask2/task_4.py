"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75
Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_of_elements(n, amount=0, start_value=1):
    if n == 0:
        return amount
    amount += start_value
    start_value /= -2
    return sum_of_elements(n - 1, amount, start_value)


count = int(input('Введите количество элементов:\n'))
print(f'Количество элементов - {count}, их сумма - {sum_of_elements(count)}')
