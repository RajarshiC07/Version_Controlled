arr = [1, 2, 3, 4]
arr1 = [100, 200, 300]
val1 = [_ for _ in arr1]
val = [[i for i in arr] for _ in arr1]
print(val)
print(val1)
print({k: i for k, i in enumerate(arr)})

arr2 = ["apple", "orange"]
print(arr2)
print("\n".join(arr2))

obj = int(2)
print(obj in arr)


def display():
    print('inn')


class A:
    var = 100


A.display = display

obj = A()
print(getattr(obj, 'display'))
