class A:
    def func(self):
        print("A class")

class B:
    def funcB(self):
        print("B class")

class C(A,B):
    def func3(self):
        print("C class")



obj=C()

obj.func()
obj.funcB()
obj.func3()