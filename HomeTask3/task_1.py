"""
Задание 1.
Реализуйте функции:
a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени
ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
import time


def time_of_function(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        func = function(*args)
        end_time = time.perf_counter_ns()
        print(f'{function.__name__} : {end_time - start_time}')
        return func

    return wrapped


################ Пункт A ################
# Сложность: O(n)
@time_of_function
def filling_in_the_list(array_def):
    array_def = [i for i in range(10000)]
    return array_def


# Сложность: O(n)
@time_of_function
def filling_out_the_dictionary(dictionary_def):
    dictionary_def = {i: i for i in range(10000)}
    return dictionary_def


# filling_in_the_list : 271900
# filling_out_the_dictionary : 549400
# Вывод: список заполняется быстрее, поскольку словарь требует вычисление хешей.


################ Пункт B ################
# Сложность: O(1)
@time_of_function
def getting_a_list_item(array_def, idx):
    return array_def[idx]


# Сложность: O(1)
@time_of_function
def getting_a_dictionary_element(dictionary_def, idx):
    return dictionary_def.get(idx)


# getting_a_list_item : 300
# getting_a_dictionary_element : 600 (В редких случаях наоборот или же равно)
# Вывод: Получение элемента происходит быстрее у словаря? НО почему тогда замер времени зачастую показывает иной
# расклад? Быть может я не прав и сделал что-то не так?


################ Пункт С ################
# Сложность: O(n)
@time_of_function
def deleting_a_list_item(array_def, idx):
    del array_def[idx]
    return array_def


# Сложность: O(1)
@time_of_function
def deleting_a_dictionary_element(dictionary_def, idx):
    del dictionary_def[idx]
    return dictionary_def


# deleting_a_list_item : 2600
# deleting_a_dictionary_element : 500
# Вывод: Удаление элемента у словаря происходи быстрее, чем у списка, поскольку в списке все элементы после удаления
# сдвигаются.


#########################################
array = filling_in_the_list(list())
dictionary = filling_out_the_dictionary(dict())

element = 567
getting_a_list_item(array, element)
getting_a_dictionary_element(dictionary, element)

deleting_a_list_item(array, element)
deleting_a_dictionary_element(dictionary, element)
