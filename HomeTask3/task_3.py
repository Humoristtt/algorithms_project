"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв
Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.
Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.
Пример:
lala - 6 уникальных подстрок
l
a
la
al
lal
ala
"""
import hashlib


def number_of_unique_substrings(row_def):
    unique_substrings = set()
    for i in range(1, len(row_def)):
        for j in range(len(row_def) - i + 1):
            res = hashlib.sha256(row_def[j:j + i].encode('utf-8')).hexdigest()
            unique_substrings.add(res)
    return len(unique_substrings)


row = input('Введите строку: ')
print(f'В строке {row} {number_of_unique_substrings(row)} уникальных подстрок')
