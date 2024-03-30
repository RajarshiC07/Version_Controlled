import asyncio
import pandas as pd
import time
# async def fn():
#     print('this')
#     await asyncio.sleep(1)
#     print('is')
#     # time.sleep(5)
#     await asyncio.sleep(1)
#     print('programming')

# # asyncio.run(fn())
# fn()

async def a():
    print("line 15")
    task = asyncio.create_task(b())
    print(await b())
    # print(task.done())
    print("line 18")
    await asyncio.sleep(1)
    print('line 20')
    print('line 21')

async def b():
    # await asyncio.sleep(1)
    print("youuu")
    return 1

# asyncio.run(a())
async def fn1(path, start_time, string):
    df = None
    while df is None and (time.time()-start_time) <= 10:
        print(df, time.time()-start_time, string)
        try:
            df = pd.read_json(path)
        except:
            await asyncio.sleep(4)
            continue
    return df

async def fn2(path, start_time):
    df = None
    while df is None and (time.time()-start_time) <= 10:
        print(df, time.time()-start_time )
        try:
            df = pd.read_json(path)
        except:
            await asyncio.sleep(4)
            continue
    return df

async def getfiles(path1, path2):
    task1 = asyncio.create_task(fn1(path1, time.time(), "task1"))
    task2 = asyncio.create_task(fn1(path2, time.time(), "task2"))
    await task1
    task2
    # await task1
    # task2
    # if task1 is not None:
    #     task2 = await asyncio.create_task(fn1(path2, time.time()))
    print(task1)
    print(task2)
    # print(res)
    # print(task2)

path1 = r''
path2 = r'D:\python projects\Practice\MyData.json'

val = asyncio.run(getfiles(path1, path2))
# val = asyncio.run(fn2(path1, time.time()))
# print(val)



