import xml.etree.ElementTree as etree

print('hello')
tree = etree.parse('Sample_Prac.xml')
root = tree.getroot()
children = [(child.tag, child.attrib, child[0].text) for child in root]
print(root.tag)
print(root[0][1].text)
print(*children, sep="\n")
all_tags = [ele.tag for ele in root.iter()]
print(*all_tags, sep="\n")
all_specific_tags = [ele.text for ele in root.iter('author')]
print(*all_specific_tags, sep="\n")
print('=----------------------------------------=')
for books in root.findall('book'):
    attr = books.attrib
    author = books.get('id')
    title = books.find('title').text
    print(attr, author, title)

print('=----------------------------------------=')
for ele in root.findall('./book/genre'):
    print(ele.text)

val = root.findall("./genre")
print(*val, sep = "\n")
print('=----------------------------------------=')
# Nodes with name='Singapore' that have a 'year' child
root.findall(".//year/..[@name='Singapore']")
print('=----------------------------------------=')
# 'year' nodes that are children of nodes with name='Singapore'
root.findall(".//*[@name='Singapore']/year")