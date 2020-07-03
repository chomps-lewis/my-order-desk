from table import prices, orders_by_store_dict
from assign_order import assign_order

orders = []
invoice = []
cost = 0

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

    total_sell = 0 # Total amount the store bought in signage this month
    total_q = 0 # Total amount of packs of signs bought by the store this month

    q = order[1] # Number of packs ordered on one line item
    form = (prices[(order[0])])[0]
    sell = (prices[(order[0])])[1]

    s += q + ' Packs of ' + form + ' @ $' + sell + '/pack'

    # Need to record the cost of these packs as well
    cost += int(q) * float((prices[(order[0])])[2])
    # Need to record total # of packs and total sell for this store for the month
    total_sell += int(q) * int(sell)
    # Now we need to assign this line item to the store that ordered it
    assign_order(order[2], s, orders_by_store_dict)

for store in orders_by_store_dict:
    if orders_by_store_dict[store]:
        invoice.append(store + '\n')
        for order in orders_by_store_dict[store]:
            invoice.append(order + '\n')
        invoice.append('\n')
with open('invoice.txt', 'w') as f:
    f.writelines(invoice)
    f.write('OUR COST (Do not include on invoice): ' + str(cost))
# OK so we got the invoice. Now we just need the COST DATA
# ALSO should add the total sell amount for the

