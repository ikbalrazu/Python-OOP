
#constructor
#attribute: 1.propertise (jokhon amra data pass korbo tokon __init__ method data gula ke recieve korbe method er peremeter dara ar __init__ method er sobkisui class er
# property)
#           2.method
#           class method: class method kaj kore class niya
#           instance method: instance method kaj kore object niya
#           static method: static method has no perameter this method is independent

class Vehcle:

    hey = "hello world"

    def __init__(self,name,driver,wheel): #instance method
        self.name = name
        self.driver = driver
        self.wheel = wheel


    def display(self): #instance method
        print(self.name,self.driver,self.wheel)

    @classmethod #decorator
    def seen(cls):
        print(cls.hey)

    @staticmethod
    def print(name):
        print("This is static method")
        print(name)


car = Vehcle("toyota","solimuddin",4)
car.display()
car.seen()
car.print("This is static method")