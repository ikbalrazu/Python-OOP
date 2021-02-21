
#  magic method or Dunder method
#  arithmatic operator
#  +,-,*,/,%,&,//,^,**
#  comparison magic method
#  ==,!=,<,>,<=,>=
# __eq__,__ne__,lt__,__gt__,__le__,__ge__
# __word__()

class Vehcele:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def __add__(self, num2, num3):
        print("Total Price ADD", self.price + num2.price+num3.price)

    def __sub__(self, num2, num3):
        print("Total Price SUB", self.price - num2.price - num3.price)

    def __mul__(self, num2, num3):
        print("Total Price MUL", self.price * num2.price * num3.price)

    def __eq__(self,other):
        print(self.name == other.name, self.price == other.price)

    def __repr__(self):
        return self.name,self.price
    def __str__(self):
        return self.name

    def total_price(self,obj):
        print("Total Price SUB",self.price+obj.price)

a = Vehcele("iqbal",1000)
b = Vehcele("iqbal",500)
c = Vehcele("arif",300)
a.__add__(b,c)
a.__sub__(b,c)
a.__mul__(b,c)
a.__eq__(b)
print(a.__repr__())
print(a.__str__())



