'''
Create two classes named Mammals and MarineAnimals. Create another class named BlueWhale which inherits both the above classes. Now, create a function in each of these classes which prints "I am mammal", "I am a marine animal" and "I belong to both the categories: Mammals as well as Marine Animals" respectively. Now, create an object for each of the above class and try calling
1 - function of Mammals by the object of Mammal
2 - function of MarineAnimal by the object of MarineAnimal
'''

class Mammals:
    def funcM(self):
        print("I am mammal ")
class MarineAnimals:
    def funcMA(self):
        print("I am a marine animal")

class BlueWhale(Mammals,MarineAnimals):
    def funcboth(self):
        print("I am a marine animal and I belong to both the categories: Mammals as well as Marine Animals")


obj1=Mammals()
obj2=MarineAnimals()
obj3=BlueWhale()

obj1.funcM()
obj2.funcMA()

#Multiple Inheritance
obj3.funcboth()
obj3.funcM()
obj3.funcMA()
