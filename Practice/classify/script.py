import config
import importlib

def addons_classes(self, *args, **kaargs):

    cls = self.__class__

    args = [importlib.import_module(mod) for mod in args]
    for module in args:
        for name in dir(module):
            value = getattr(module, name)
            if (type(value) is list or type(value) is tuple) and name in dir(cls):
                cls_val = getattr(cls, name)
                cls_val += value
            elif type(value) is dict and name in dir(cls):
                cls_val = getattr(cls, name)
                cls_val.update(value)
            else:
                cls_val = value
            setattr(cls,name,cls_val)



def classify(module, *args, **kaargs):
    cls = type(module.__name__,(),{key: staticmethod(value) if callable(value) else value for key, value in ((name, getattr(module, name)) for name in dir(module))})
    cls.addons_classes = addons_classes
    return cls


REPORTS = ["bbva", "esg_aum"]


configTestClass = classify(config, [config])
configTest = configTestClass()



for report in REPORTS:
    if report not in configTest.REPORT:
        configTest.addons_classes(report)

print(dir(configTest))
print(configTest.REPORT)

















