


class _sampleRef:
    def __init__(self, cobj):
        self.obj = cobj

    def __call__(self):
        return self.obj


def ref(cobj):
    return _sampleRef(cobj)


class _sampleproxy:
    def __init__(self, objc):
        self.obj = objc

    def __str__(self):
        return self.obj

    def __set_name__(self, owner, name):
        return "<class 'sampleproxy>"


def proxy(obj):
    return _sampleproxy(obj)
