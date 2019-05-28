from menuitem import MenuItem
from orderitem import OrderItem
from payment import Payment

class Order():
    def __init__(self):
        self.orderitems=[]

    def addOrderItems(self, orderitem):
        self.orderitems.append(orderitem)

    def calcTotal(self):
        total=0.0
        for o in self.orderitems:
            total += o.getItem().itemprice * o.quantity
        calculateTotal=Payment(total)
        return calculateTotal