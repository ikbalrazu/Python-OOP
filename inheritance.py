
#super() method

class A:
    def first(self):
        print("This is class A")

class B(A):
    def third(self):
        print("This is class B")

class C(B):
    def third(self):
        print("This is class C")
        super().first()
        super().third()

call = C()
call.third()
