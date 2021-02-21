# polimorphism with class method

class Man:
    def leg(self):
        print("has 2 legs")

class Animal:
    def leg(self):
        print("has 4 legs")
    def hand(self):
        print("2 hands")

def fun(obj):
    obj.leg()


a = Man()
b = Animal()
fun(a)
fun(b)
for obj in (a,b):
    obj.leg()