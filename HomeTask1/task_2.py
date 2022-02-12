"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""
from random import randint


# Сложность: O(n^2)
def min_first(array):
    for i in range(len(array)):  # O(n)
        idx = i  # O(1)
        for j in range(len(array) - 1):  # O(n)
            if array[i] > array[j + 1] and array[idx] > array[j + 1]:  # O(1)
                idx = j + 1  # O(1)
        array[i], array[idx] = array[idx], array[i]  # O(1)
    min_value = array[0]  # O(1)
    return min_value  # O(1)


# Сложность: O(n^2)
def min_second(array):
    for i in array:  # O(n)
        min_value = True  # O(1)
        for j in array:  # O(n)
            if i > j:  # O(1)
                min_value = False  # O(1)
        if min_value:  # O(1)
            return i  # O(1)


# Сложность: O(n)
def min_third(array):
    min_value = array[0]  # O(1)
    for i in array:  # O(n)
        if min_value > i:  # O(1)
            min_value = i  # O(1)
    return min_value  # O(1)


list_of_random_numbers = [randint(0, 100) for i in range(5)]
min_one = min_first(list_of_random_numbers)
min_two = min_second(list_of_random_numbers)
min_three = min_third(list_of_random_numbers)
print(min_one, min_two, min_three)
