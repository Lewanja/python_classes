from Item import itemm

class Keyboard(itemm):

    pay_rate = 0.7

    def __init__(self, name, price, quantity):
        #call to super to have accessto all attributes/methods
        super().__init__(name, price, quantity)


