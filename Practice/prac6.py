import inspect


def lines(cls, name):
    global attrname
    try:
        attrlist = list(str(getattr(cls, name)).split(" "))
        attrname = eval(f'{cls.__name__}.{name}') if f"{cls.__name__}.{name}" in attrlist else None
    except AttributeError:
        print("No such attribute present")
    if attrname is None:
        return attrname
    else:
        return int(str(list(str(inspect.getsourcelines(attrname)).split(" "))[-1])[:-1])


class A(object):

    classvar = 100
    line = None

    def func1(self):
        print('function 1')

    def __init__(self, name):
        self.name = name

    # Gets called when an attribute is accessed
    def __getattribute__(self, item):
        print('__getattribute__ ', item)
        # Calling the super class to avoid recursion
        return super().__getattribute__(item)

    # Gets called when the item is not found via __getattribute__
    def __getattr__(self, item):
        print('__getattr__ ', item)
        return super().__setattr__(item, 'orphan')

    def func2(self):
        print('function 2')


def main():
    A.lines = classmethod(lines)
    obj = A("helllooo")
    # print(obj.func1)
    print(A.lines('classvar'))
    print(obj.lines('func1'))
    print(obj.lines('func1t'))
    print(A.lines('func1'))
    print(A.lines('funct1'))
    print(obj.foo)
    print(obj.foo)
    print(obj.xyzzz)
    print(obj.xyzzz)
    print(obj.__setattr__('abc', 100))
    print(A.__dict__)
    print(obj.__dict__)
    l1 = obj.__dir__()
    l2 = dir(obj)
    print(sorted(l1))
    print(l2)
    print(l1 == l2)
    print("vars")
    print(vars(obj))

    print(obj.foo)


if __name__ == '__main__':
    main()
