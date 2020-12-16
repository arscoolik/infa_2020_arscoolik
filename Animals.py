class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def whatisme(self):
        return self.name + "\n" + str(self.age)
class Zebra(Animal):
    def whatisme(self):
        return self.name + "\n" + str(self.age) + "\n" + "Zebra"

class Dolphin(Animal):
    def whatisme(self):
        return self.name + "\n" + str(self.age) + "\n" +  "Dolphin"
