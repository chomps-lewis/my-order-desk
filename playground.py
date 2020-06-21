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

