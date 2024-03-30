import sys


class decorator1:

    def __init__(self):
        self.value = 'val'

    def __call__(self, func):
        print('in class decorator 1 {}'.format(self.value))

        def wrapper():
            print('in wrapper ')
            func()
        return wrapper


@decorator1()
def operation1():
    print('operation 1')


# def decorator2(func):
#     print('in decorator2')
#     func()
#
# @decorator2
# def operation2():
#     print('operation 2')


if __name__ == '__main__':
    operation1()
print(sys.path)