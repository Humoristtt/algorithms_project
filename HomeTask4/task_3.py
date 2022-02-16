"""
Задание 3.
Приведен код, формирующий из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через timeit
Обязательно предложите еще свой вариант решения!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):
    return str(enter_num)[::-1]


def revers_5(enter_num):
    return "".join(reversed(str(enter_num)))


number = 123456789987654321
print(timeit('revers(number)', globals=globals(), number=1000))
print(timeit('revers_2(number)', globals=globals(), number=1000))
print(timeit('revers_3(number)', globals=globals(), number=1000))
print(timeit('revers_4(number)', globals=globals(), number=1000))
print(timeit('revers_5(number)', globals=globals(), number=1000))

# Поэкспериментируем с числами. При number = 0 (однозначное число) мы получаем следующие результаты.
# 8.270000034826808e-05
# 8.149999848683365e-05
# 0.0002442999975755811
# 0.00021469999774126336 0.0003544999999576248

# При number = 10 (двухзначное число) мы получаем следующие результаты.
# 0.0005564999992202502
# 0.0002831999991030898
# 0.00030309999783639796
# 0.00025069999901461415
# 0.0005988000011711847

# При number = 123456789987654321 (большое число) мы получаем следующие результаты.
# 0.003621799998654751
# 0.002389299999776995
# 0.0002537000000302214
# 0.0002413000001979526
# 0.0006450000000768341

# Рекурсивная функция оказалась самой неэффективной. На втором месте С КОНЦА "классический алгоритм" 2‑й функции.
# На третьем месте у нас 5‑я функция, которая использует в своей реализации строковую функцию reversed(), которая
# уступает срезу в 3 раза по скорости. Ну и лавры первого места делят функции 3 и 4 (4 слегка быстрее поскольку сразу
# возвращает значение).
