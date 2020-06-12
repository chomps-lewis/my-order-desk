from xml.etree import ElementTree as ET

file_name = 'xml.xml'
counter = 0

mytree = ET.parse(file_name)
myroot = mytree.getroot()


def get_qty(s):
    # I had to put a try except because non-signage orders breaks everything
    # TO DO either get better xml input (signage orders only) or make a rule
    # Have script check the SKU, if not signage then pass

    # This takes a string in this format 120429|4|0.0000|Y|0.0000|1|20|1|
    # The second value after the | is the qty '4' here
    try:
        return s[int(s.index('|')+1)]
    except:
        print('Not a valid order')

for child in myroot:
    try:
        print(myroot[counter][5][-1][4][0].text) # Grab SKU
        print(myroot[counter][5][-1][4][5][6].text) # Grab Store #
        print(get_qty(myroot[counter][5][-1][4][4][6].text))# Grab Qty
    except IndexError:
        print('Something wrong happened')
        pass
    counter += 1
