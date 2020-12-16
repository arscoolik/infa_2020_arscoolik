class Mother():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.get_str()
    def get_str(self):
        return self.name

class Daughter(Mother):
    def get_str(self):
        return self.name + " is Daughter"
