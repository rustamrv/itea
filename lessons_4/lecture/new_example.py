
class Person:

    def __new__(cls, *args, **kwargs):
        person_object = super().__new__(cls)
        person_object.age = 25
        return person_object

    def __init__(self, first_name, surname):
        self._first_name = first_name
        self._surname = surname

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


person = Person('John', 'Dar')
print(person.first_name)
person.first_name = 'Rustam'
print(person.first_name)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
class Person:

    def __new__(cls, *args, **kwargs):
        person_object = super().__new__(cls)
        person_object.age = 25
        return person_object

    def __init__(self, first_name, surname):
        self._first_name = first_name
        self._surname = surname

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value


person = Person('John', 'Dar')
print(person.first_name)
person.first_name = 'Rustam'
print(person.first_name)
