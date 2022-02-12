"""
Задание 5. На закрепление навыков работы со стеком
Реализуйте собственный класс-структуру "стопка тарелок".
Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.
После реализации структуры, проверьте ее работу на различных сценариях.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
import math


class StackClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def push_in(self, limit, plates):
        number_of_stacks = math.ceil(plates / limit)
        plate = 1
        for i in range(number_of_stacks):
            self.elems.append([])
            while len(self.elems[i]) < limit:
                if plate == plates + 1:
                    break
                else:
                    self.elems[i].append(plate)
                    plate += 1
        return self.elems

    def pop_out(self, limit_pop):
        self.elems.reverse()
        for el in self.elems:
            for i in el:
                while limit_pop != 0:
                    if len(el) == 0:
                        break
                    else:
                        el.pop()
                        limit_pop -= 1
        for i in self.elems:
            if len(i) == 0:
                self.elems.remove(i)
        self.elems.reverse()
        return self.elems

    def get_last_stacks(self):
        return self.elems[len(self.elems) - 1]

    def stacks_size(self):
        return len(self.elems)


if __name__ == '__main__':
    sc_obj = StackClass()
    print(sc_obj.is_empty())
    LIMIT = 5
    PLATES = 27
    print(sc_obj.push_in(LIMIT, PLATES))
    print(sc_obj.pop_out(4))
    print(sc_obj.get_last_stacks())
    print(sc_obj.stacks_size())
