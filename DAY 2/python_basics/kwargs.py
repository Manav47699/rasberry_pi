def myfun(**kwargs):
    print(kwargs)
    print(type(kwargs))

myfun(a = 10, b = "name")


def sum(**kwargs):
    s = 0
    for value in kwargs:
        s += kwargs[value]
    print(s)

sum (a = 10, b = 30)

