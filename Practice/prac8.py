import sys
import weakref

from Practice import sampleRef


class Parent:
    __id = 100
    __slots__ = ['name', 'id1']

    @classmethod
    def getid(cls):
        return cls.__id


class Child(list):
    cid = 200

    def __init__(self):
        super().__init__()
        self.id = self.generator()

    @classmethod
    def generator(cls):
        cls.cid += 100
        return cls.cid

    def __str__(self):
        return f"Child obj {self.id}"


obj1 = Child()
obj2 = obj1
obj3 = obj1
print(obj1)

objwr = weakref.ref(obj1)
objwobj = objwr()
objprox = weakref.proxy(obj1)

objsr = sampleRef.ref(obj1)
objsobj = objsr()
objsprox = sampleRef.proxy(obj1)

print(type(objwr))
print(type(objwobj))
print(type(objsr))
print(type(objsobj))
print(type(objprox))
print(type(objsprox))

print(id(obj1))
print(id(objwr))
print(id(objwobj))
print(id(objsr))
print(id(objsobj))
print(id(objprox))
print(id(objsprox))

print(weakref.getweakrefcount(obj1))
print(sys.getrefcount(obj1))
