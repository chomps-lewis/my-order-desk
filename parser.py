from xml.etree import ElementTree as ET

file_name = 'xml.xml'
counter = 0

mytree = ET.parse(file_name)
myroot = mytree.getroot()

for child in myroot:
    try:
        print(myroot[counter][5][-1][4][0].text)
    except IndexError:
        pass
    counter += 1
