class Shape:
    def PropertyOfShape(self):
        print("Different Shape Have Different")


class Square(Shape):
    def __init__(self, Name):
        self.Name = Name

    def PropertyOfShape(self):
        print("This Is {}".format(self.Name))
        print("{} has 4 Sides".format(self.Name))


class Triangle(Shape):
    def __init__(self, Name):
        self.Name = Name

    def PropertyOfShape(self):
        print("This Is {}".format(self.Name))
        print("{} has 3 Sides".format(self.Name))


s1 = Shape()
s1.PropertyOfShape()

s2 = Square("Square")
s2.PropertyOfShape()

s3 = Triangle("Triangle")
s3.PropertyOfShape()
