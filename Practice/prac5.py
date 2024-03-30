class A:
    __val = None

    def __init__(self, val):
        self.__val = val
        print("inside A init")

    def __str__(self):
        return f" inside A {self.__val}"


class B:

    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        print("inside B init")

    def __str__(self):
        return f" inside B {self.val1} and {self.val2} and {self.val3}"


class C(A, B):
    # def __new__(cls, *val):
    #     if len(val) == 0:
    #         return object.__new__(C)
    #     elif len(val) == 1:
    #         return object.__new__(A,val)
    #     elif len(val) == 2:
    #         return object.__new__(B,val)
    #     else:
    #         return None

    def __init__(self, *val):
        if len(val) == 1:
            super(A, self)
        elif len(val) == 2:
            super(B, self)
        print("inside C")

    def __str__(self):
        return f" inside C"


obj1 = C(1)
#obj2 = A(10)
print(obj1)
#print(obj2)
print(type(obj1))
