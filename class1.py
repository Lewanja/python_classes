#set of rules by initiating; methods with name __init__ also known as constructor, method with unique name
#magic methods
class item1:
    def __init__(self,name:str, price:float,quantity:int):
        #run validations to the received arguements\
        assert price>=0, f"price {price} is not greater than zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        print("Instances is printed twice because there are two instances")
        print(f"An instance is created:{name}")
        #assigning attributes to each name
        self.name=name
        self.price=price
        self.quantity=quantity
        #assert is used to check if there is a match with your expectation

    def calculate_total_price(self):
        return self.price * self.quantity
    #avoid hard coding attributes

#instance1


"""print(insta1.name, insta1.price, insta1.quantity)
print(insta2.name, insta2.price, insta2.quantity)"""


insta1=item1("Phone", 100, 5)

insta2=item1("Computer",900, 20)

print(insta1.calculate_total_price())
print(insta2.calculate_total_price())