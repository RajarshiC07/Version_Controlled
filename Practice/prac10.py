import inspect
import sys


class A:
    _classvariable = 10

    def __init__(self,val):
        self.instancevariable = val

    def display(self):
        return f'returning self'


print(sys.path)
sys.path.extend(['path1', 'path2'])
print(sys.path)