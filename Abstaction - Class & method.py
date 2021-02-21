from abc import ABC,abstractmethod
# abstract method: je class e amra abstract method toiri korbo sei class er sub-class e oi method obosoii thakte hobe

class Father(ABC):
    @abstractmethod
    def do_study(self):
        pass

class Son(Father):
    def __init__(self,name):
        print(name)

    def do_study(self):
        print("yes father")

class doughter(Father):
    def display(self):
        print("this is doughter class")

    def do_study(self):
        print("doughter do_study method")

show = Son("Solimuddin")
show.do_study()
pr = doughter()
pr.do_study()