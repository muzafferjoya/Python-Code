from collections import OrderedDict
def diner(orders):
    new_orders=OrderedDict()
    for item,quantity in orders:
        if item not in new_orders:
            new_orders[item]=quantity
        else:
            new_orders[item]+=quantity
    for item, quantity in new_orders.items():
        print(item,quantity)
