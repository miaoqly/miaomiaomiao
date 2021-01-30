from homework_phases1 import Animal


class Cat(Animal):

    def __init__(self,name,colour,age,gender):
        self.hair = "短毛"
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

    def catchmouse(self):
        print("会抓老鼠")

    def cry(self):
        print("喵喵叫")
if __name__ == '__main__':

    miao = Cat("喵喵","白色",3,"female")
    print(f"(猫名：{miao.name},毛色：{miao.colour},年龄：{miao.age},性别：{miao.gender},毛发：{miao.hair})")