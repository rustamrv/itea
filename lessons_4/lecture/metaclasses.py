even_numbers = [2, 5, 4, 6, 8]

metaclass = type(type(even_numbers))
print(metaclass)


def get_num_of_wheels(self):
    return self.num_of_wheels


# Vehicle = type('Vehicle', (), {'num_of_wheels': 4, 'get_num_of_wheels': lambda self: self.num_of_wheels})
# # print(Vehicle)
# # print(Vehicle.num_of_wheels)
# # print(Vehicle().get_num_of_wheels())

#class mixin
class DriveMixin:

    def drive(self):
        print(f'{self.model} is driving')


class CarMetaClass(type):

    def __new__(mcs, name, base, attrs):
        if not aeven_numbers = [2, 5, 4, 6, 8]

metaclass = type(type(even_numbers))
print(metaclass)


def get_num_of_wheels(self):
    return self.num_of_wheels


# Vehicle = type('Vehicle', (), {'num_of_wheels': 4, 'get_num_of_wheels': lambda self: self.num_of_wheels})
# # print(Vehicle)
# # print(Vehicle.num_of_wheels)
# # print(Vehicle().get_num_of_wheels())

#class mixin
class DriveMixin:

    def drive(self):
        print(f'{self.model} is driving')


class CarMetaClass(type):

    def __new__(mcs, name, base, attrs):
        if not attrs.get('num_of_wheels'):
            raise NotImplementedError('num_of_wheels attribute is required')
        base = (DriveMixin, )
        car_class = super().__new__(mcs, name, base, attrs)
        print(name, base, attrs)
        return car_class


class Car(metaclass=CarMetaClass):

    num_of_wheels = 4

    def __init__(self, engine, model):
        self.engine = engine
        self.model = model

    def __call__(self, *args, **kwargs):
        print(f"I'm {self.model}")


car = Car('v-3', 'mers')
car()

import time

class Decorator:

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = start - time.time()
        return result, end


@Decorator
def do_nothing(second):
    time.sleep(second)


print(do_nothing(2))

