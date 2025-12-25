# python can seperate them under the hood
def both (*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 2, 3, a = 10, b = 10)


#difference -> args gives a tuple, kwargs gives a dictonary