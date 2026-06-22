import math


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2*(self.width + self.height)

    def get_diagonal(self):
        return math.sqrt(self.width**2 + self.height**2)

    def get_picture(self):
        shape = ""
        if self.height > 50 or self.width > 50:
            shape+= "Too big for picture." 
            return shape
        for index in range(self.height):
            shape += "*" * self.width + "\n"
        return shape
    
    def get_amount_inside(self, shape):
        cols = self.width // shape.width
        rows = self.height // shape.height
        return cols * rows
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)
        self.side = length

    def set_width(self, new):
        self.set_side(new)
    
    def set_height(self, new):
        self.set_side(new)
    
    def set_side(self, new):
        self.side = new
        super().set_width(new)
        super().set_height(new)

    def __str__(self):
        return f"Square(side={self.side})"

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
