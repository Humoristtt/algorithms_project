"""
Задание 4.
Приведены два алгоритма. В них определяется число, которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
import random
from collections import Counter

from timeit import timeit

array = [random.randint(0, 100) for _ in range(10000)]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    number, count = Counter(array).most_common(1)[0]
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(timeit('func_1', globals=globals(), number=1000))
print(timeit('func_2', globals=globals(), number=1000))
print(timeit('func_3', globals=globals(), number=1000))

# Результаты времени функций:
# 1.5400000847876072e-05
# 1.5300000086426735e-05
# 1.4999997802078724e-05
# Все функции почти что одинаковы хороши, но 3‑я все же лучше, поскольку за одно и то же время (+-) она может найти
# не только самый часто повторяющийся элемент, но и выдать список всех элементов и их количество повторений в массиве.
