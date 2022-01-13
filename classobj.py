#creating an instance is same as creating an object

class item:
    pass
#code that we willl not have to repeat ourselves

item1=item()
#assigning attributes to instances of a class
item1.name="Phone"
item1.price=100
item1.quantity=5
#each attribute is assigned one instance of the class. we can create our own datatypes: <class '__main__.item'>
'''print(type(item1))
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))'''

#creating methods
class items:
    def calculate_total_price(self,x,y):
        return x * y

item2=items()
item2.name = "Phone"
item2.price = 100
item2.quantity = 5
        # the function should return total price
print(item2.calculate_total_price(item2.price, item2.quantity))

