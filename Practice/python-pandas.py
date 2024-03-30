import pandas as pd

#
file1 = pd.read_csv('csvfile1.csv')

#
# print(file1.columns)
# # print(file1['Year'][0:5])
# # print(file1.Year[0:5])
# # print(file1[['Year','Units','Value']])
# # # print(file1.iloc[3:7])
# # # print(file1.iloc[4,0])
# # #
# # # print(file1.iterrows())
# # print(file1.loc[file1['Value'] == "49,593"])
# # file1.sort_values(['Year'])
# # file1['Total'] = file1['Value'].items() + '1000'
#
# print(file1.head(5))
# print(type(file1['Value'].values))
# modified = file1.drop(columns=['Industry_code_ANZSIC06'])
# print(modified.columns)
cols = list(file1.columns.values)
file2 = file1.copy(deep=True)
print(len(list(file1.columns.values)))
print(len(list(file2.columns.values)))
file2 = file1[cols[0:1] + [cols[-1]] + cols[1:-1]]
print(file1.columns)
# print(file2.columns)
# print(len(list(file1.columns.values)))
# print(len(list(file2.columns.values)))
#
# file1.to_csv('texts.txt', index=False, sep="\t")
# print(type(file1['Year'][0:5]))
#
# file3 = file1.loc[(file1['Year'] == '2021')]
# print(file3)
#
#
# file2 = pd.read_csv('texts.txt', delimiter='\t', index_col= False)
# print(file2.iloc[0:5])
#
import numpy as nm

arr = nm.arange(0, 15).reshape(3, 5)
s = pd.DataFrame(arr)
print(s)

file3 = file1.filter(file1['Year'] == '2013')
file3.to_csv('texts.txt')
file2.to_csv('texts.txt')
# print(file3.head(3))
#
# print(file1.columns)
file4 = file1.loc[file1['Year'] == 2013]
file5 = file1.loc[~(file1['Year'] == 2013)]
# print(file4['Year'])
# print(len(file5))
# print(len(file4))
# print(len(file1))
file1.loc[file1['Year'] == 2013, 'Year'] = 1900
# print(len(file1))

file6 = file1.loc[file1['Year'] == 1900]
# print(len(file6))
# print(len(file4))

file1.loc[file1['Year'] == 2013, ['Year', 'Value']] = [1900, 100]
# print(file1.loc[file1['Year'] == 1900]['Value'][0:5])
#
#
# print(file1.loc[file1['Value'] == 100])
# for file7 in pd.read_csv('csvfile1.csv', chunksize=5):
#     print('chunk')
#     print(file7)
print(file1.index)
print(file1.columns)
print(file1.describe())
# print(file1.T)
# print(file1.sort_index(ascending=True, axis=1))
# print(file1.sort_values(by = 'Year'))
file7 = file1.sort_values(by='Year')
# print(file7['Year'][0:5])
# print(file7.reset_index())
# print(file7['Year'][0:5])
# print(file1.loc[0:5,['Year','Value']])
# print(file1[file1['Year'] > 2020])
# file1['Test'] = file1['Year'] - 1000
# print(file1.head(3))
# print(file1[file1['Test'].isin([1021,1020])])
# file1.dropna(how="any")
file8 = pd.read_csv('csvfile2.csv')
print(file8.head(5))
print(len(file8))


def check(s):
    print(s)
    series = pd.Series(s)
    val = list(series.values)
    return val[0]


# print(file8.apply(check))
# print(file8.stack())
print(nm.random.randint(0, 100, 6))
file9 = pd.DataFrame(
    {
        "A": ["foo", "foo", "foo", "foo", "foo", "foo"],
        "B": ["bar", "bar", "bar", "bar", "bar", "bar"],
        "C": nm.random.randn(6),
        "D": nm.random.randint(0, 100, 6),
    }
)
file9.to_csv('texts.txt')
print(file9)
# print(file9.apply(check, axis=1))
# import matplotlib as plt
#
# file9.plot()
# plt.pyplot.show()

file9.loc[file9['A'] == 'foo', 'A'] = "Loo"
print(file9)
file9.iloc[4:6,2:4] = [2, 3]
print(file9)
filter1 = file9['D'] == 3
filter2 = file9['C'] == 2
file9.where(filter1)
print(file9.where(filter1))

file10 = file9.groupby(['A','B']).sum()
print(type(file10))
file11 = pd.read_csv('csvfile1.csv')
file9['D'] = file11['Value']
print(file9)
print(type(file9['D'].values))

def conversion(s: str):
    string = s.split(',')
    new_string = ''.join(string)
    try:
        val = int(new_string)
        return val
    except ValueError:
        print('Not compatible')

file9['E'] = file9['D'].transform(conversion)
print(file9)
print(file9.drop(columns = ['D']))
print(file9)

path = r'C:\Users\abc.xlsx'
#df.to_excel(path, sheet_name='sheet1', header=None, index=False, startcol=4, startrow=5)