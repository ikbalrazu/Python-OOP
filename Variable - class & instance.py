
#variable: 1. class variable
#          2. instance variable (self diya je variable gula thakbe oigula instance variable)

class Vehcle:
    hey = "hello world" #class variable
    def __init__(self,name,driver,wheel):
        self.name = name #instance variable
        self.driver = driver #instance variable
        self.wheel = wheel #instance variable


    def display(self):
        print(self.name,self.driver,self.wheel)


car = Vehcle("toyota","solimuddin",4)
car.display()
print(car.hey)
print(Vehcle.hey)