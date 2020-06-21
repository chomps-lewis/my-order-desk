"""
This is a function to sort each of the orders and assign it to
the corresponding store that ordered it. For instance, if store
32 ordered 3 packs of HG Sale, we need to add that to the dict,
that has the 'Store 32' Key. That way we can keep all the stores'
orders straight.

This is, quite frankly, an extremely messy way of doing this.
The current data I have that tells me which store ordered the signs
is <Value>Store 61</Value>. This is messy and  could probably clean
that up. If I had better input I could probably sort without a
gigantic if then function. But this is the easiest way for now.
"""

def assign_order(value, line_item, order_table):
    if '12' in value:
        (order_table['Store 12']).append(line_item)
    elif '13' in value:
        (order_table['Store 13']).append(line_item)
    elif '14' in value:
        (order_table['Store 14']).append(line_item)
    elif '16' in value:
        (order_table['Store 16']).append(line_item)
    elif '19' in value:
        (order_table['Store 19']).append(line_item)
    elif '21' in value:
        (order_table['Store 21']).append(line_item)
    elif '31' in value:
        (order_table['Store 31']).append(line_item)
    elif '32' in value:
        (order_table['Store 32']).append(line_item)
    elif '61' in value:
        (order_table['Store 13']).append(line_item)
    elif 'Marketing' in value:
        (order_table['Marketing']).append(line_item)
    else:
        print('STORE LOOKUP FAILED')