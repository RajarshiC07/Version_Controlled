class Singleton:
    __instances = None
    __counter = 0
    __forge = False

    def __new__(cls):
        if cls.__instances is None or cls.__forge is True:
            cls.__counter += 1
            cls.__instances = super().__new__(cls)
            cls.__forge = False
        return cls.__instances

    def __init__(self):
        self.instance_No = self.__counter

    @classmethod
    def new_child(cls):
        cls.__forge = True
        return Singleton()

    def __str__(self):
        return f'Instance with id {self.instance_No}'


obj1 = Singleton()
obj2 = Singleton()
print(obj1)
print(obj2)
obj3 = Singleton.new_child()
print(obj3)
obj4 = Singleton()
obj5 = Singleton.new_child()
print(obj4)
print(obj5)
