import csv

class itemm:
    pay_rate=0.8 #payrate after 20% discount
    all=[]
    def __init__(self,name:str, price:float,quantity:int):

        assert price>=0, f"price {price} is not greater than zero!"
        assert quantity >= 0, f"quantity {quantity} is not greater or equal to zero!"

        self.__name=name
        self.__price=price
        self.quantity=quantity

        #actions to execute
        itemm.all.append(self)
    #converting name attribute to read only using property decorator
    @property
    def price(self):
        return self.__price

    @property
    def name(self):
        return self.__name

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price=self.__price + self.__price * increment_value
    #enables you to change the parameter of name attribute
    @name.setter
    def name(self,value):
        self.__name=value

    def calculate_total_price(self):
        return self.__price * self.quantity


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
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity")),

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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    def __connect(self,smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello someone.
        we have{self.name} {self.quantity} times
        Regards, JimShapeCoding
        """
    def __send(self):
        pass
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send

