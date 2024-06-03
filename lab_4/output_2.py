import math


class Shape:
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


def main():
    square = Square(5)
    print("Area of square:", square.area())

    circle = Circle(3)
    print("Area of circle:", circle.area())


if __name__ == "__main__":
    main()
