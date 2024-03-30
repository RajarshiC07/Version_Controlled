dic = dict({1:'apple',2:'nipple',3:'pineapple',4:'triple'})
print(dic)

keyslist = dic.keys()
print(keyslist)
print(1 in dic)
print(dic.items())
l1 = [1,2,3,4]
l2 = ["a","b","c","d"]
dic2 = dict()
for i,j in zip(l1,l2):
    dic2[i] = j
print(next(iter(dic)))
print(dic2)

big = list(filter(lambda x: x&1 != 1, l1))
print(big)
