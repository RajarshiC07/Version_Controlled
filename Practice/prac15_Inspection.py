i = 100
print(type(i))
print(type(type(i)))
print(type(i)(1))
print(i.__class__.__class__.__name__)
print(type(globals()))
globals()['val'] = 100


def fun():
    x = 200
    return x


print(globals())
locals()['value'] = 500
print(locals())
