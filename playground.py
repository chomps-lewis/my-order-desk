from table import prices, orders_by_store_dict
from assign_order import assign_order

orders = []

with open('june.txt') as f:
    data = f.readlines()

for i, line in enumerate(data):
    try:

        # First we are looking for form_id and qty
        # It comes in this format: 120429|4|0.0000|Y|0.0000|1|20|1|
        # This works because the only time | is present, that info follows
        # IF the xml contained | for other reasons, we could use regex

        pipe = line.index('|') # | indicates the line has form_id and qty
        form_id = line[(pipe-6):pipe]
        qty = line[(pipe+1)]
        orders.append([form_id, qty]) # find id and qty and add it to a list

    except:
        try:
            if line == '<Prompt>Please Indicate Store Number</Prompt>\n':
                orders[-1].append(data[i+1])
        except:
            pass

for order in orders:
    # First we need to get the line item
    # Format is: 4 Packs of 1up HG Sale @ $45/pack
    # We'll remember the line item as a string, s
    s = ''
    s += order[1] + ' Packs of ' + (prices[(order[0])])[0] + ' @ $' + (prices[(order[0])])[1] + '/pack'
    # Now we need to assign this line item to the store that ordered it
    assign_order(order[2], s, orders_by_store_dict)

# NEXT PROBLEM TO TACKLE
# HOW TO TRANSFORM THE orders_by_store_dict into the format we need it in for the final invoice?

invoice = []

for store in orders_by_store_dict:
    store_orders = []
    store_orders.append(store)
    store_orders.append(orders_by_store_dict[store])

