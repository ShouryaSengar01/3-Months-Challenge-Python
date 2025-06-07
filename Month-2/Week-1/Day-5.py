# ░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░    ⭐ SUPER() ⭐    ░░  => This function is used in a Child Class to call methods from Parent Class(Superclass).
# ░░░░░░░░░░░░░░░░░░░░░░░░░░    Allows you to Extend the Funtionality of the Inherited Methods.

# ░░░░░░░░░░░░░░░░░░░░░░░░░░░
# ░░   ⭐ OVERRIDING ⭐   ░░  => You can override the parent method by creatinf smilar one in child class. The one in subclass will be used.
# ░░░░░░░░░░░░░░░░░░░░░░░░░░░    


class Shape():
    def __init__(self, color, is_filled):    
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It's {self.color} and {"Filled" if self.is_filled else "Empty"}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)       #super() being used.
        self.radius = radius

    def describe(self):
        print(f"It's a Circle with an Area of {3.14 * self.radius * self.radius:.2f}cm²")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):                                                                  #OVERRIDING
        print(f"It's a Square with an Area of {self.width * self.width:.2f}cm²")
        super().describe()

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
            print(f"It's a Triangle with an Area of {self.width * self.height / 2:.2f}cm²")
            super().describe()

circle = Circle("Red", True, 6)
square = Square("Green", False, 4)
triangle = Triangle("Blue", True, 5, 7)

# print(triangle.height)
# print(circle.color)
square.describe()
