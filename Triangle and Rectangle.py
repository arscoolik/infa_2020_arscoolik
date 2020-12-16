class Shape():
    def __init__(self, height, width):
        self.height = height
        self.width = width

class Rectangle(Shape):
    def area(self):
        return self.height * self.width

class Triangle(Shape):
    def area(self):
        return self.height * self.width/2
