def generator():
    while True:
        value = yield 
        print(value*2)



res = generator()
print(type(res))
print(res.send(None))
for i in range(5):
    res.send(i)