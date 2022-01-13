import csv
import csv

class itemm:
    pay_rate=0.8 #payrate after 20% discount
    all=[]
    def __init__(self,name, price,quantity):

        #assert price>=0, f"price {price} is not greater than zero!"
        #assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        self.name=name
        self.price=price
        self.quantity=quantity

        #actions to execute
        itemm.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price=self.price * self.pay_rate
    #convert to a class method using decorators by creating them just before lines

    @classmethod
    #class object is passed as first arguement in the background

    def instantiate_from_csv(cls):
        with open("text.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

            #for item in items:
            #    print(item)
            for item in items:
                itemm(
                    name=item.get("name"),
                    price=(item.get("price")),
                    quantity=(item.get("quantity")),

            )
    @staticmethod
    def is_integer(num):
        #we will count out votes that are point zero
        if isinstance(num,float):
            #count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False

#changing how instanceis represented:representing your objects
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"



#class method
#itemm.instantiate_from_csv()
#print(itemm.all)
#print(itemm.is_integer(7))


class Phone(itemm):

    def __init__(self, name, price, quantity, broken_phones=0):
        #call to super to have accessto all attributes/methods
        super().__init__(name, price, quantity)


        assert broken_phones >= 0, f"Broken Phones {broken_phones} is not greater or equal to zero!"

        self.broken_phones=broken_phones



phone1=Phone("jscPhonev10",500,5,1)
print(phone1.calculate_total_price())
#phone2=Phone("jscPhonev20",700,5,1)
print(itemm.all)
print(Phone.all)