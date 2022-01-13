#class attributes, global attributes
class itemm:
    pay_rate=0.8 #payrate after 20% discount
    def __init__(self,name:str, price:float,quantity:int):

        assert price>=0, f"price {price} is not greater than zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        self.name=name
        self.price=price
        self.quantity=quantity


    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate
insta1=itemm("Phone", 200, 5)

insta2=itemm("Computer",900, 20)
insta1.apply_discount()
print(insta1.price)
#print(insta1.calculate_total_price())
#print(insta2.calculate_total_price())
print(itemm.pay_rate)
print(insta1.pay_rate)
print(insta2.pay_rate)

#checking attributes use __dict__
print(itemm.__dict__)
print(insta1.__dict__)

#apply different discount
insta2.pay_rate=0.7
insta2.apply_discount()
print(insta2.price)