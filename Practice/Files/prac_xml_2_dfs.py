import xml.etree.ElementTree as etree
from anytree import Node, RenderTree, PreOrderIter


def etreeTraversal():
    tree = etree.parse('Sample_Prac.xml')
    root = tree.getroot()
    print(root.tag)

    all_tags = [ele.tag for ele in root.iter()]
    print(*all_tags, sep="\n")


def treeMaker():
    root = Node("catalogue")
    c1 = Node("child1", parent=root)
    c2 = Node("child2", parent=root)
    gc1 = Node("grandchild1", parent=c1)
    gc2 = Node("grandchild2", parent=c1)
    ggc1 = Node("greatgrandchild1", parent=gc1)

    tree = RenderTree(root)
    print(tree)
    # values = [node for node in RenderTree(tree)]
    # print(values)
    for pre, fill, node in RenderTree(root):
        # print("%s%s" % (pre, node.name))
        print(node.name,'\t', node.children)
        # print(pre, fill, node.name)
treeMaker()