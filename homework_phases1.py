
class Animal:

    def __init__(self,name,colour,age,gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

    def cry(self):
        print("会叫")

    def run(self):
        print("会跑")

class Cat(Animal):

    Animal.__init__(name = "猫",colour = "白",age = 3,gender = "female")

    hair = "短毛"

    def catchingmouse(self):
        print("会捉老鼠")

    miao = Animal()
    print(miao.cry())
