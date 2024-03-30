
class Sample:
    id = 0

    def __init__(self, *args):
        if len(args) == 0:
            self.a = 10e3
            self.b = 10e3

        elif len(args) == 2:
            self.a = args[0]
            self.b = args[1]
            print("h")
        else:
            return None

    def __add__(self, other):
        if not isinstance(other, Sample):
            return TypeError
        else:
            return Sample(self.a + other.a, self.b + other.b)

    def __call__(self):
        print("Calling self")
        if hasattr(self, "a") and hasattr(self, "b"):
            return f'{self.a}a {self.b}b UID = {self.id}'
        else:
            return f"None created"

    def __str__(self):
        if hasattr(self, "a") and hasattr(self, "b"):
            return f"| a = {self.a}, b = {self.b} UID = {self.id}|\n"
        else:
            return f"None created"

    def add(self, *value):
        return sum(value)

    def __genId__(self):
        for i in range(1000):
            yield i


print(callable(Sample))

obj1 = Sample()
obj2 = Sample()
obj3 = Sample(10, 2)
obj4 = Sample(10, 3)
print(obj3.add(10, 20))
print(obj1 is obj2)
print(obj1 == obj2)
print(obj1, obj2, obj3, obj4)
val = [obj1(), obj2(), obj3(), obj4()]
print(val)
print(obj3 + obj4)
