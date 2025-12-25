class Point:
    def __init__(self, xx, yy):
        self.x = xx
        self.y = yy
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    
p1 = Point(1, 2)
p2 = Point (3, 4)
p3 = p1+p2  #p1.__add__(p2)
print(p3)