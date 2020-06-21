from xml.etree import ElementTree as ET

file_name = input('Enter the .xml filename:\n') + '.xml'
counter = 1
mytree = ET.parse(file_name)
myroot = mytree.getroot()
line_items = []
# This dictionary contains pricing and name data of the signage
# The format is 'orderform_id':['name','sell','cost']

table = { '116767':['2up Perfed Blank Sign', '39', '13.77'],
           '120429':['4up Perfed Blank Sign', '39', '17.67'],
           '136947':['New HG Sale 1up', '45', '18'],
           '116601':['New HG Sale 2up', '52', '22.43'],
           '116602':['New HG Sale 3up', '52', '22.82'],
           '136949':['New HG Value 1up', '47', '26.30'],
           '175981':['New HG Value 2up', '43', '20.29'],
           '156967':['New HG Value 3up', '47', '26.30'],
           '175189':['1up Clearance', '45', '22.34'],
           '175190':['2up Clearance', '45', '22.34'],
           '175191':['3up Clearance', '45', '22.34'],
           '136950':['New HG Value Greenhouse 10.5 x 6.5', '42', '21.80'],
           '136948':['New HG Sale 11x17 Thin - ERROR PRICING DATA NOT AVAILABLE', '0', '0'],
           '155238':['SYNTHETIC New HG Sale 1up', '137.50', '111.05'] }

orders_by_store_dict = {'Store 12':[],
                        'Store 13':[],
                        'Store 14':[],
                        'Store 16':[],
                        'Store 19':[],
                        'Store 21':[],
                        'Store 31':[],
                        'Store 61':[],
                        'Marketing':[]}

# Currently trying to handle IF Multiple items in one cart, find the subsequent orders

for child in myroot:
    backwards_counter = -1
    try:
        while True:
            print(myroot[counter][5][backwards_counter])
            if myroot[counter][5][backwards_counter] == 'Item':
                # Get this: '155238|1|0.0000|Y|0.0000|1|0|1|'
                form_id = myroot[counter][5][backwards_counter][4][4][6].text[:6]
                qty = myroot[counter][5][backwards_counter][4][4][6].text[7]

                # Organize the line item order
                line_items.append(qty + ' Packs of ' + form_id + ' @ $' + table[form_id][1] + '/pack')
                backwards_counter -= 1
        store_number = myroot[counter][5][-1][4][5][6].text
    except:
        print('error')
        pass



    print(line_item)
    counter += 1

