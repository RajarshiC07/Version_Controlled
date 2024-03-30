class AccessModifiers:
    _protected = None
    __private = None

    def publicmethod(self):
        print("inside parent public method")

    def _protectedmethod(self):
        print("inside parent protected method")

    def __privatemethod(self):
        print("inside parent private method")

    def __init__(self,val = 0):
        self._protected = val
        self.__private = val+10
        self.public = val+20

    def __str__(self):
        self.__privatemethod()
        self._protectedmethod()
        return f"protected = {self._protected} private = {self.__private} public = {self.public}"

def converter(val):
    return val*80

def generator(cls,name):
    if name == 'child':
        return object.__new__(access2)
    elif name == 'parent':
        return object.__new__(AccessModifiers)
    else:
        return None


class access2(AccessModifiers):

    def __init__(self, val):
        super().__init__(val)

    def publicmethod(self):
        print("inside child public method")

    def _protectedmethodchild(self):
        self._protectedmethod()

    def __privatemethod(self):
        print("inside child private method")

    def getval(self):
        return "hiiiii"

    def __str__(self):
        self.__privatemethod()
        self._protectedmethod()
        return f" public "

obj1 = AccessModifiers(10)
obj2 = access2(20)
access2.converter = staticmethod(converter)
access2.generator = classmethod(generator)
print(obj1)
print(getattr(obj2,'getval'))
print(issubclass(AccessModifiers,access2))
print(dir(obj2))

obj3 = access2.generator("child")
obj4 = access2.generator("parent")
print(type(obj3))
print(type(obj4))
print(obj2.converter(100))
print(obj2.__class__.__name__)