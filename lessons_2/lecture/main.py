
class Phone:

    def __init__(self, model, email, number):
        self.model = model
        self.email = email
        self.number = number

    def call(self, to_number):
        print(f'Звоним с {self.number} на {to_number}')


class SatellitePhone:

    def call(self):
        print("Делаем спутниковый звонок")


class SmartPhone(Phone, SatellitePhone):

    def download_application(self):
        print("Down application")


phone = Phone('Nokia', 'email', 123456789)
phone.call(6996)

print("--"*30)

smart = SmartPhone('Iphone', 'dsdw', 56565)
smart.call(333)
smart.download_application()                                                                                                                                                                                                                                                                                                                                 
class Phone:

    def __init__(self, model, email, number):
        self.model = model
        self.email = email
        self.number = number

    def call(self, to_number):
        print(f'Звоним с {self.number} на {to_number}')


class SatellitePhone:

    def call(self):
        print("Делаем спутниковый звонок")


class SmartPhone(Phone, SatellitePhone):

    def download_application(self):
        print("Down application")


phone = Phone('Nokia', 'email', 123456789)
phone.call(6996)

print("--"*30)

smart = SmartPhone('Iphone', 'dsdw', 56565)
smart.call(333)
smart.download_application()