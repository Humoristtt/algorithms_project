"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Решите через рекурсию. В задании нельзя применять циклы.
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculate():
    operation_type = input('Выберете знак операции (+, -, *, /), или введите 0 для выхода:\n')
    if operation_type == '0':
        return exit('Завершение программы')
    else:
        if operation_type in "+-*/":
            try:
                num_1, num_2 = map(int, input('Введите два числачерез пробел:\n').split())
                if operation_type == '+':
                    res = num_1 + num_2
                    print(f'Ваш результат {res}')
                    return calculate()

                elif operation_type == '-':
                    res = num_1 - num_2
                    print(f'Ваш результат {res}')
                    return calculate()

                elif operation_type == '*':
                    res = num_1 * num_2
                    print(f'Ваш результат {res}')
                    return calculate()

                elif operation_type == '/':
                    try:
                        res = num_1 / num_2
                    except ZeroDivisionError:
                        print('Деление на 0 невозможно!')
                    else:
                        print(f'Ваш результат {res}')
                    finally:
                        return calculate()
            except ValueError:
                print('Вы ввели строку или что-то еще. Не надо так!')
                return calculate()
        else:
            print("Введен неверный символ, попробуйте еще раз")
            return calculate()


calculate()
