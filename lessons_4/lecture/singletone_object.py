
class SingleError(Exception):
    pass


class Singletone:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            obj = super().__new__(cls, *args, **kwargs)
            cls._instance = obj
            return obj
        return cls._instance
        # else:
        #     raise SingleError(f'The object of class {cls.__name__} already exists')


ob = Singletone()
ob2 = Singletone()
print(id(ob), id(ob2), ob is ob2)                                                                                     
class SingleError(Exception):
    pass


class Singletone:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            obj = super().__new__(cls, *args, **kwargs)
            cls._instance = obj
            return obj
        return cls._instance
        # else:
        #     raise SingleError(f'The object of class {cls.__name__} already exists')


ob = Singletone()
ob2 = Singletone()
print(id(ob), id(ob2), ob is ob2)