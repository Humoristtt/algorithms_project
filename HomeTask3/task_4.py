"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"
Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...
Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш
Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП.
"""
import hashlib


class CachingWebPages:
    def __init__(self):
        self.page_cashing_dict = {
            'https://ru.wikipedia.org': 'f26828bb095d18209359b8d5726a41ec60e8317c960d0dfd10f3a62e101f2502',
            'https://vk.com/humoristtt': 'cbec9ae1f3b2d319c9fd0549ad1862ea268e62d60569fc1dfd099cc1b21e648c'
        }

    def check_web_page(self, args):
        salt, url = args
        if self.page_cashing_dict.get(url) is not None:
            print(f'Страница {url} уже есть в кэше. Значение хеша: {self.page_cashing_dict.get(url)}')
        else:
            url_hash = hashlib.sha256(url.encode('utf-8') + salt.encode('utf-8')).hexdigest()
            self.page_cashing_dict.update({url: url_hash})
            print(f'Страница {url} была добавлена в кэш. Значение хеша: {self.page_cashing_dict.get(url)}')


if __name__ == '__main__':
    urls = {'google': 'https://www.google.ru/', 'wikipedia': 'https://ru.wikipedia.org',
            'amazon': 'https://www.amazon.com/', 'vk': 'https://vk.com/humoristtt'}
    test_obj = CachingWebPages()
    for i in urls.items():
        test_obj.check_web_page(i)
    print(test_obj.page_cashing_dict)
