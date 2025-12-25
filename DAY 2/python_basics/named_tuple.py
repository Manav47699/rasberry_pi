from collections import namedtuple

Point = namedtuple("point", "x y z")
p1 = Point(1,2,3)
print(p1)

x, y, z = p1

print(x, ' ', y, ' ', z, " ")

