from Item import itemm

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