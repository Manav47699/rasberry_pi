# *args use garda jati ota ni argyuument dinu milxa
# it returns a tuple

def myfun(*args):
    print(args)
    print (type(args))

myfun(1, 2, 3)


def avg(*args):
    s=0
    for arg in args:
        s += arg
    print(s/len(args))

avg(1, 2, 3)