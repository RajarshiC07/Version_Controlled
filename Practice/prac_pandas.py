import pandas as pd
import numpy as nm
data = {"a":100, "b":200, "c":300}
s = pd.Series([1,2,3,4,5])
print(s)
data1 = nm.arange(10).reshape(2,5)
print(data1)
s1 = pd.DataFrame(data1, index = ['Upper','lower'])
print(s1)
s2 = pd.read_json("file.json")
print(s2)