import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse(r"D:\python projects\Practice\Files\Sample_Prac.xml")
root = tree.getroot()
stack = [root]



def traversal(current):
    print(current.tag)
    for element in current:
        if type(element) is ET.Element:
            traversal(element)
        else:
            print(element.tag)


traversal(root)
# for attr in root.findall("./book"):
#     for ele in attr:
#         print(type(ele))
#         for al in ele:
#             print(type(al))


# visited = set()
#
#
# def dfs(visited, graph, node):  # function for dfs
#     if node not in visited:
#         print(node)
#         visited.add(node)
#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)
#
#
# dfs(visited, root, root)
