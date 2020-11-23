import time
from threading import Thread
import requests


class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = start - time.time()
        return result, end


@Decorator
def do_nothing(name, is_demon, second):
    print(f'Task {name} start, {"is demon" if is_demon else "not demon"}')
    time.sleep(second)
    print(f'Task {name} finish, {"is demon" if is_demon else "not demon"}')


def download(link, name):
    format = link.split('.')[-1]
    print(f'Начало загрузки файла {name}.{format}')

    f = open(f'{name}.{format}', 'wb')
    ufc = requests.get(link)
    f.write(ufc.content)
    print(f'Конец загрузки {name}.{format}')


if __name__ == "__main__":
    print('Task 1')
    t1 = Thread(target=do_nothing, args=('Thread-One', False, 1), name='Thread-One', daemon=False)
    t2 = Thread(target=do_nothing, args=('Thread-Two', True, 2), name='Thread-Two', daemon=True)
    t3 = Thread(target=do_nothing, args=('Thread-Three', True, 3), name='Thread-Three', daemon=True)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    print('Task 2')
    list_link = ['https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg',
                 'https://investgazeta.ua/images/easyblog_articles/2979/Ukraine-Stub-Map_Renovated.png']

    iter = 1
    for i in list_link:
        t = Thread(target=download, args=(i, f'File-{iter}'))
        t.start()
        t.join()
        iter += 1



from threading import Thread
import requests


class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = start - time.time()
        return result, end


@Decorator
def do_nothing(name, is_demon, second):
    print(f'Task {name} start, {"is demon" if is_demon else "not demon"}')
    time.sleep(second)
    print(f'Task {name} finish, {"is demon" if is_demon else "not demon"}')


@Decorator
def download(link, name):
    format = link.split('.')[-1]
    print(f'Начало загрузки файла {name}.{format}')

    f = open(f'{name}.{format}', 'wb')
    ufc = requests.get(link)
    f.write(ufc.content)
    print(f'Конец загрузки {name}.{format}')


if __name__ == "__main__":
    print('Task 1')
    t1 = Thread(target=do_nothing, args=('Thread-One', False, 1), name='Thread-One', daemon=False)
    t2 = Thread(target=do_nothing, args=('Thread-Two', True, 2), name='Thread-Two', daemon=True)
    t3 = Thread(target=do_nothing, args=('Thread-Three', True, 3), name='Thread-Three', daemon=True)
    t1.start()
    t1.join()
    t2.start()
    t2.join()
    t3.start()
    t3.join()
    print('Task 2')
    list_link = ['https://upload.wikimedia.org/wikipedia/commons/4/49/Flag_of_Ukraine.svg',
                 'https://investgazeta.ua/images/easyblog_articles/2979/Ukraine-Stub-Map_Renovated.png']

    iter = 1
    for i in list_link:
        t = Thread(target=download, args=(i, f'File-{iter}'))
        t.start()
        t.join()
        iter += 1



