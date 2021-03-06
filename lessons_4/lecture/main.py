# abstract class
from abc import ABC, abstractmethod


class Phone(ABC):

    def __init__(self, model, imei):
        self.model = model
        self.imei = imei

    @abstractmethod
    def call(self):
        pass


class SmartPhone(Phone):

    def __init__(self, model, imei, os_):
        super(SmartPhone, self).__init__(model, imei)
        self._os = os_

    def call(self):
        print(f"calling from {self.model}")

    def download_aplication(self):
        print("Down")


SmartPhone('ddd', '2333', 'ddds').call()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           # abstract class
from abc import ABC, abstractmethod


class Phone(ABC):

    def __init__(self, model, imei):
        self.model = model
        self.imei = imei

    @abstractmethod
    def call(self):
        pass


class SmartPhone(Phone):

    def __init__(self, model, imei, os_):
        super(SmartPhone, self).__init__(model, imei)
        self._os = os_

    def call(self):
        print(f"calling from {self.model}")

    def download_aplication(self):
        print("Down")


SmartPhone('ddd', '2333', 'ddds').call()