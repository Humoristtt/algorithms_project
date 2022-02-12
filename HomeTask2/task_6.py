"""
Задание 6.  В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
Решите через рекурсию. В задании нельзя применять циклы.
"""
import random


def guess_the_number(attempts):
    if attempts == 0:
        return exit('Вы проиграли!')
    try:
        answer = int(input('Введите число от 0 до 100: '))
        if answer == hidden_number:
            return exit('Вы победили!')
        elif answer > hidden_number:
            print(f'Загаданное число меньше! Попыток осталось: {attempts - 1}')
        else:
            print(f'Загаданное число больше! Попыток осталось: {attempts - 1}')
    except ValueError:
        print(f'Нужно вводить число, а не буквы! Попыток осталось: {attempts - 1}')
    return guess_the_number(attempts - 1)


hidden_number = random.randint(0, 100)
number_of_attempts = 10
guess_the_number(number_of_attempts)
