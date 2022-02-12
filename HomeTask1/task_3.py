"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


# Сложность: O(n^2)
def solution_one(company):
    COMPANY = 3  # O(1)
    sorted_values = sorted(company.values(), reverse=True)  # O(n * log n)
    sorted_company = {}  # O(1)
    for i in sorted_values:  # O(n)
        for k in company.keys():  # O(n)
            if company[k] == i and COMPANY != 0:  # O(1)
                sorted_company[k] = company[k]  # O(1)
                COMPANY -= 1  # O(1)
    return f'Топ-3 компании по прибыли: {sorted_company}'  # O(1)


# Сложность: O(n * log n)
def solution_two(company):
    sorted_company = {}  # O(1)
    cnt = 3  # O(1)
    for key, val in sorted(company.items(), key=lambda x: x[1], reverse=True):  # O(n * log n)
        if cnt > 0:  # O(1)
            sorted_company.setdefault(key, val)  # O(1)
        else:  # O(1)
            break  # O(1)
        cnt -= 1  # O(1)
    return f'Топ-3 компании по прибыли: {sorted_company}'  # O(1)


# Сложность: O(n) => Этот способ предпочтительнее по скорости, т.к. имеет минимальную вычислительную сложность и
# решает поставленную задачу без изменений исходного словаря и лишней сортировки.
def solution_three(company):
    sorted_company = {}  # O(1)
    list_d = dict(company)  # O(1)
    for i in range(3):  # O(n)
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])  # O(1)
        del list_d[maximum[0]]  # O(1)
        sorted_company[maximum[0]] = maximum[1]  # O(1)
    return f'Топ-3 компании по прибыли: {sorted_company}'  # O(1)


the_company = {'Компания A': '1234', 'Компания B': '3456', 'Компания С': '2345', 'Компания D': '5678',
               'Компания E': '4567'}
print(solution_one(the_company))
print(solution_two(the_company))
print(solution_three(the_company))
