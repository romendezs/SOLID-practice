from abc import ABC, abstractmethod


class IEmployee(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Programmer(IEmployee):
    def work(self):
        print("Programmer programs programs")

    def eat(self):
        print("Programmer eats pizza")

    def sleep(self):
        print("Programmer falls asleep at 2 AM")


class Android(IEmployee):
    def work(self):
        print("Android moves boxes")

    def eat(self):
        raise NotImplementedError("Android doesn't eat, it's a machine")

    def sleep(self):
        raise NotImplementedError("Android doesn't sleep, it's a machine")