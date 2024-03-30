import numpy as nm
import pandas as pd
import matplotlib.pyplot as pl
def prac():
    arr = nm.arange(10).reshape(2, 5)
    df1 = pd.DataFrame(data=arr, index=['a', 'b'], columns=['C1', 'C2', 'C3', 'C4', 'C5'])
    print(df1)
    print(df1.head())

    s1 = pd.Series(nm.arange(10, 20, 2))
    s2 = pd.Series(nm.arange(20, 30, 2))
    df2 = pd.concat([s1, s2], axis=1, ignore_index=True)
    df3 = df2.transpose()
    df3.columns = ['C1', 'C2', 'C3', 'C4', 'C5']
    df3.index = ['c', 'd']
    df4 = pd.concat([df1, df3], axis=0)
    print(df4)

    l = [
        {
            "Student": [{"Exam": 90, "Grade": "a"},
                        {"Exam": 99, "Grade": "b"},
                        {"Exam": 97, "Grade": "c"},
                        ],
            "Name": "Paras Jain"
        },
        {
            "Student": [{"Exam": 89, "Grade": "a"},
                        {"Exam": 80, "Grade": "b"}
                        ],
            "Name": "Chunky Pandey"
        }
    ]
    rows = []
    for data in l:
        data1 = data['Student']
        data2 = data['Name']
        print(data2)
        for row in data1:
            row['Name'] = data2
            rows.append(row)

    df5 = pd.DataFrame(rows)
    print(df5)
    df5.iat[2, 2] = 'Ravi'
    print(df5.iat[2, 2])
    s3 = pd.Series(nm.arange(100, 600, 100))
    df6 = pd.DataFrame(s3, columns=['id'])
    df5['id'] = pd.DataFrame(df5.index + 1, columns=['id'])
    print(df5)
    cols = list(df5.columns.values)
    print(cols)
    df7 = df5.copy(deep=True)
    df7 = df5[[cols[-1]] + cols[0:-1]]
    print(df7.reset_index(drop=True))

    # df7['values'] = df7['id']*100

    print(df7)
    print("hereeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
    for rows in df7.iterrows():
        print(rows)

    s4 = pd.Series(['aab', 'acb', 'ccd', 'cab', 'dab'])
    print(s4)

    df8 = df7.insert(loc=1, column='category', value=s4)

    print(df7)
    print(df7[df7['Exam'] > 90])
    df8 = df7.drop(columns=['Exam'])
    print(df8)
    df8 = df7[df7['Name'].str.contains('Paras')]
    print(df8)
    df8 = df7.rename(columns={'Name': 'Name-of-candidates'})
    print(df7)
    df8 = df7.sort_values(by='Exam', axis=0)
    print(df8)

    print(df8.index.values[-1])
    print(df8.Exam.unique())  # IMPORTANT*****************************************#
    print(df8['Name'].value_counts())  # IMPORTANT*****************************************#
    df8['diff'] = [x - y for x, y in zip(df8['id'], df8['Exam'])]
    print(df8.drop(columns=['diff']))
    print(df8['Exam'].max())
    print(df8.nlargest(2, ['Exam']))  # IMPORTANT*****************************************#
    print(df8.shape)


    def reduce(x):
        x['Exam'] = x['Exam'] - 5
        return x


    print(df8.pipe(reduce).value_counts())
    df9 = df8.reindex([1, 2, 3, 4, 5, 6, 7, 8])
    print(df9)
    df9.loc[7], df9.loc[2] = df9.loc[2], df9.loc[5]
    df10 = df9.fillna(value={'id': 6, 'category': 'ccd'})
    df9.loc[9] = df9.loc[7]

    print(df8)
    print(df10)
    print(pd.merge(df10, df9, how='left'))

    print(df9.count())
    df11 = df9.drop_duplicates(inplace=True)
    print(df9)

    df11 = df9.pivot_table(index=['Name','category'], margins=True, margins_name='Total')
    print(df11)
    df11.plot()
    df12 = df11.melt(id_vars='id',var_name='Exam')
    print(df12)


    df13 = pd.read_csv('csvfile1.csv')
    print(df13.columns)
    count = df13.count().values
    print(count)
    indexes = nm.arange(0,count.max(),1).tolist()
    df13.set_index(['Year', 'Industry_aggregation_NZSIOC'],inplace=True)
    print(df13.head())
    df13.to_csv('csvfile2.csv')
    print(df13.sort_index())
    print(df13.groupby('Units').sum('Value'))
    print(df13['Units'].add_prefix('Amount-').head(5))



if __name__ == '__main__':
    prac()