"""
Задание 2.
Приведен код, который формирует из введенного числа обратное по порядку входящих в него цифр.
Задача решена через рекурсию.
Выполнена попытка оптимизировать решение мемоизацией.
Сделаны замеры обеих реализаций.
Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?
П.С. задание не такое простое, как кажется
"""

from random import randint
from timeit import timeit


def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
# print('Не оптимизированная функция recursive_reverse')
# print(timeit("recursive_reverse(num_100)", globals=globals(), number=100))
# print(timeit("recursive_reverse(num_1000)", globals=globals(), number=10000))
# print(timeit("recursive_reverse(num_10000)", globals=globals(), number=10000))
# print()

# print('Оптимизированная функция recursive_reverse_mem')
# print(timeit('recursive_reverse_mem(num_100)', globals=globals(), number=10000))
# print(timeit('recursive_reverse_mem(num_1000)', globals=globals(), number=10000))
# print(timeit('recursive_reverse_mem(num_10000)', globals=globals(), number=10000))
# print()

# Ну на первый взгляд кажется все логичным и мемоизация играет свою роль в оптимизации.
# Дальше я решил поиграться с количеством вызовов timeit. Я указал выполнить выражение 10 и 100 раз. И увидел следующее:
print(timeit("recursive_reverse(num_100)", globals=globals(), number=10))
# 2.010000025620684e-05 Время НЕ оптимизированной функции для number=10
print(timeit("recursive_reverse(num_1000)", globals=globals(), number=100))
# 0.0002733000001171604 Время НЕ оптимизированной функции для number=100
print(timeit("recursive_reverse(num_1000)", globals=globals(), number=1000))
# 0.001776699999027187 Время НЕ оптимизированной функции для number=1000
print(timeit('recursive_reverse_mem(num_100)', globals=globals(), number=10))
# 8.499999239575118e-06 Время оптимизированной функции для number=10
print(timeit('recursive_reverse_mem(num_1000)', globals=globals(), number=100))
# 2.0300001779105514e-05 Время оптимизированной функции для number=100
print(timeit('recursive_reverse_mem(num_1000)', globals=globals(), number=1000))
# 0.0001467000001866836 Время оптимизированной функции для number=1000 - Тут уже заметна эффективность

# На основании этих наблюдений могу сказать что для НЕ многократных вызовов мемоизация не играет роли,
# поскольку только при многочисленном запуске самой функции мы начинаем использовать кэш предыдущего запуска.
# Грубо говоря нужно исходить из условия задачи. Надеюсь мысль свою донес:)
