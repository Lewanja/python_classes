#class attributes, global attributes
class itemm:
    pay_rate=0.8 #payrate after 20% discount
    all=[]
    def __init__(self,name:str, price:float,quantity:int):

        assert price>=0, f"price {price} is not greater than zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        self.name=name
        self.price=price
        self.quantity=quantity

        #actions to execte
        itemm.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate

#changing how instanceis represented:representing your objects
    def __repr__(self):
        return f"itemm('{self.name}', {self.price}, {self.quantity})"

insta1=itemm("Phone", 200, 5)
insta2=itemm("Computer",900, 20)
insta3=itemm("Mouse", 30, 20)
insta4=itemm("Keyboard", 50,20)
insta5=itemm("Cables",25,80)

print(itemm.all)


#to print a specific arguement
for instance in itemm.all:
    print(instance.name)