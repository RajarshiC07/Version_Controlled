import collections
import sys

arr = [1, 2, 3, 4]
arr1 = [100, 200, 300]
val1 = [_ for _ in arr1]
val = [(x, y) for x in arr for y in arr1]


def gen():
    for i in range(3):
        yield i


op = gen()
print(op.__next__())
print(op.__next__())
print(op.__next__())


class Student:
    __st_id = 0

    def __init__(self, name):
        self.name = name
        self.st_id = Student.__id_generator()

    @staticmethod
    def __id_generator():
        Student.__st_id += 100
        return Student.__st_id

    def __str__(self):
        return f'Student id = {self.st_id}, Student name = {self.name}'


class Class:
    __instance = None

    def __new__(cls, args=None):
        if args is None:
            args = list()
            if cls.__instance is None:
                cls.__instance = super().__new__(cls, args)
                return cls.__instance
            else:
                cls.add(cls.__instance, args)
                return cls.__instance

    def __init__(self, *args):
        self._st_list = [args[i] for i in range(len(args))]

    @classmethod
    def add(cls, self, stu):
        self._st_list.append(stu)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self._st_list):
            res = self._st_list[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration

    def __call__(self, *args, **kwargs):
        return self._st_list


st1 = Student('Ravi')
st2 = Student('Shyam')
# cl5 = Class(st1)


Student = collections.namedtuple('Student', ['name', 'age'])
st3 = Student('Ravi', 10)
l = ['raju', 20]
st4 = st3._make(l)
st5 = st3._make(['ramu', 300])

print(st3)
print(st4)
print(st5)

d1 = {'a': 0, 'b': 1, 'c': 2}
d2 = {'d': 3, 'e': 4}
d3 = {'f': 5}
st7 = collections.ChainMap(d1, d2)

print(st7)
print(st7.maps)
print(st7)
print(d1)

counter1 = collections.Counter(st7)
print(counter1)
counter2 = collections.Counter([1, 2, 3, 4, 5, 5, 6, 6, 6, 6])
print(counter2)

orddict = collections.OrderedDict()
ord1 = collections.OrderedDict.fromkeys('abcde', 100)
print(ord1)
ord1.move_to_end('a')
dq1 = collections.deque([1, 2, 2, 2, 2, 2, 3, 4])
print(dq1)
dq1.rotate(3)
print(dq1)
print(dq1.count(2))
x = 100


class semiSingleton:

    __lastInstance = None

l1 = [1,2,3,4,5]
l2 = reversed(l1)

print(l1[-1::-1])
print(list(l2))
