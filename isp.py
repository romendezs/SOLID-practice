from abc import ABC, abstractmethod


class IHuman(ABC):
    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class IEmployee(ABC):
    @abstractmethod
    def work(self):
        pass

class IMachine(ABC):
    @abstractmethod
    def charge():
        pass

class Programmer(IEmployee, IHuman):
    def work(self):
        print("Programmer programs programs")

    def eat(self):
        print("Programmer eats pizza")

    def sleep(self):
        print("Programmer falls asleep at 2 AM")


class Android(IEmployee, IMachine):
    def work(self):
        print("Android moves boxes")
    
    def char(self):
        print("Androif charges")