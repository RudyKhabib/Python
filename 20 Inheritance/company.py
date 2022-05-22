class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        return 1000


class Manager(Employee):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)

    def salary(self):
        return 13000


class Agent(Employee):
    def __init__(self, name, surname, age, sales):
        super().__init__(name, surname, age)
        self.__sales = sales

    def salary(self):
        return 5000 + 0.05 * self.__sales


class Worker(Employee):
    def __init__(self, name, surname, age, hours):
        super().__init__(name, surname, age)
        self.__hours = hours

    def salary(self):
        return 100 * self.__hours
