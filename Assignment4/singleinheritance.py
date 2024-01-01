class Parent:
    def __init__(self,name):
        self.name=name
    def greet(self):
            print(f"Hello my name is {self.name}")


class Child(Parent):
     def __init__(self, name,age):
          super().__init__(name)
          self.age=age

     def describe(self):
        print(f"My name is {self.name} and I am {self.age} years old")


parent=Parent("Alice")
child=Child("Bob",20)


parent.greet()
child.greet()

child.describe()

