#instantiating instances(objects)/creating data

from Item import itemm


item1=itemm("myitem",750,8)
item1.__price=900

print(item1.__price)

item1=itemm("myitem",750,8)
item1.apply_increment(0.2)
item1.apply_discount()

print(item1.price)