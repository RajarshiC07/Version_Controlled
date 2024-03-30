import contextlib


class contextManager1:
    def __init__(self):
        self.name = self.__class__.__name__

    def __enter__(self):
        print('In {} enter dunder'.format(self.name))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('In {} exit block '.format(self.name))
        if exc_type is ValueError:
            print('Value Error', exc_val)
            return True
        else:
            return False

    def run(self):
        print('In {} run block '.format(self.name))


class xyz:

    def fun(self):
        print('In xyz fun')


@contextlib.contextmanager
def contextManager2():
    print('in context manager2')
    try:
        yield xyz()
    except Exception as e:
        print('In exception block {}'.format(e.args))
        # raise AttributeError('from context manager')
    finally:
        print('done in finally')


with contextManager1() as cm:
    cm.run()
    raise ValueError('error in value')
    

print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
try:
    with contextManager2() as cm,contextManager1() as cm1:
        cm.fun()
        cm1.run()
        raise Exception("noo")
        raise ValueError('value')

except AttributeError as e:
    print('All good')