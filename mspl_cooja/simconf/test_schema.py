from __future__ import print_function
import simconf

xml = open('server-only.csc').read()
simconf = simconf.CreateFromDocument(xml)


print('simconf title:%s' % simconf.simulation.title)

"""
print('%s is sending %s %d thing(s):' % (order.billTo.name, order.shipTo.name, len(order.items.item)))
for item in order.items.item:
    print('  Quantity %d of %s at $%s' % (item.quantity, item.productName, item.USPrice))

order.to_csc()
"""