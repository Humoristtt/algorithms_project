"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход, который вы придумаете, например, применить словарь.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# Сложность: O(n^2)
def authorization_one(users_def):
    login_in_base = False  # O(1)
    user_id = None  # O(1)
    login = None  # O(1)
    is_active = None  # O(1)
    login = input('Введите логин:\n')  # O(1)
    for i in users_def:  # O(n)
        if login in i['login']:  # O(n)
            login_in_base = True  # O(1)
            user_id = i['id'] - 1  # O(1)
            login = i['login']  # O(1)
            is_active = i['is_active']  # O(1)
            break  # O(1)
    if not login_in_base:  # O(1)
        return exit('В доступе отказано! Данного пользователя нет в базе.')  # O(1)
    else:  # O(1)
        if is_active:
            return f'Добро пожаловать, {login}!'  # O(1)
        else:  # O(1)
            tmp = input(f'{login}, для входа вам необходимо активировать учетную запись.\n '
                        f'Произвести активацию (y/n)?:\n')  # O(1)
            if tmp == 'y':  # O(1)
                users[user_id]['is_active'] = True  # O(1)
                return f'Активация успешно произведена. Добро пожаловать, {login}!'  # O(1)
            else:  # O(1)
                return exit('Активация не пройдена.')  # O(1)


# Сложность: O(n)
def authorization_two(users_def, users_is_active_def):
    for login in users_def.keys():  # O(n)
        if not users_is_active_def[login]:  # O(1)
            tmp = input(f'{login}, для входа вам необходимо активировать учетную запись.\n'
                        f'Произвести активацию (y/n)?:\n')  # O(1)
            if tmp == 'y':  # O(1)
                users_is_active[login] = True  # O(1)
                print(f'Активация успешно произведена. Добро пожаловать, {login}!')  # O(1)
            else:  # O(1)
                print(exit('Активация не пройдена.'))  # O(1)
        else:  # O(1)
            print(f'Добро пожаловать, {login}!')  # O(1)


# Сложность: O(1) => Этот способ предпочтительнее по скорости, так как в ней не используется цикл
def authorization_three(users_def, user_name, user_password):
    if users_def.get(user_name):  # O(1)
        if users_def[user_name]['password'] == user_password and users_def[user_name]['is_active']:  # O(1)
            return 'Добро пожаловать! Доступ к ресурсу предоставлен'  # O(1)
        elif users_def[user_name]['password'] == user_password and not users_def[user_name]['is_active']:  # O(1)
            return 'Учетная запись не активна! Пройдите активацию!'  # O(1)
        elif users_def[user_name]['password'] != user_password:  # O(1)
            return 'Пароль не верный'  # O(1)
    else:  # O(1)
        return 'В доступе отказано! Данного пользователя нет в базе.'  # O(1)


users = [{'id': 1, 'login': 'Vyacheslav', 'password': 'password1', 'is_active': True},
         {'id': 2, 'login': 'Olga', 'password': 'password2', 'is_active': False},
         {'id': 3, 'login': 'Anna', 'password': 'password3', 'is_active': True}]
print(authorization_one(users))
print(users)

users_password = {'Vyacheslav': 'password1', 'Olga': 'password2', 'Anna': 'password3'}
users_is_active = {"Vyacheslav": True, "Olga": False, "Anna": True}
authorization_two(users_password, users_is_active)
print(users_is_active)

users = {'Vyacheslav': {'password': 'password1', 'is_active': True},
         'Olga': {'password': 'password2', 'is_active': False},
         'Anna': {'password': 'password3', 'is_active': True},
         }
authorization_three(users, 'Vyacheslav', 'password1')
authorization_three(users, 'Olga', 'password2')
authorization_three(users, 'Anna', 'password33')
print(users_is_active)
