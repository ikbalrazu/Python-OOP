#encapsulation 1.public 2.protected 3.private


class Vechele:

    def __init__(self,name):
        self.name = name #public
        self._name = name #protected - single undersccore
        self.__name = name #private - double underscore

a = Vechele("solimuddin")
print("Public:",a.name,"\nProtected:",a._name)
#access private data
print("Private:",a._Vechele__name)