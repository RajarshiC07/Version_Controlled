from prac6 import lines as l


class Name:

    def __init__(self):
        self._name = ''

    def __get__(self, instance, owner):
        return self._name

    def __set__(self, instance, value):
        self._name = value

    def __del__(self):
        self._name = ''

    def __str__(self):
        return f"The name is {self._name}"


class Name1:

    def __init__(self):
        self._name = ''

    def fget(self):
        print("inside Name1 get")
        return self._name

    def fset(self, name):
        print("inside Name1 set")
        self._name = name

    def fdel(self):
        print("inside Name1 del")
        self._name = ''

    name = property(fget, fset, fdel)


class Name2:

    def __init__(self):
        self._name = ''

    @property
    def name(self):
        print("inside Name2 get")
        return self._name

    @name.setter
    def setname(self, name):
        self._name = name

    @name.deleter
    def name(self):
        self._name = ''


Name.lines = classmethod(l)


class location:
    __city = None
    __country = None

    def __init__(self):
        self.__city = ''
        self.country = ''

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    @city.deleter
    def city(self):
        self.__city = ''

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, value):
        self.__country = value

    @country.deleter
    def country(self):
        self.__country = ''

    def __str__(self):
        return f"City = {self.__city} Country = {self.__country}"


class Person:
    name = Name()
    name1 = Name1()
    name2 = Name2()
    loc = location()
    loc1 = location()


user = Person()
user.name = 'Hari'
user.name1 = 'Ram'
user.name2 = 'Krishna'
print(user.name)
print(user.name1)
print(user.name2)
user.loc.city = 'Kolkata'
user.loc1.city = 'Delhi'
print(user.loc)
print(user.loc1)
