
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("Some generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof, woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow, meow!")
