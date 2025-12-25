alist = [1, 2, 3, 4, 5]
it = iter(alist)
while True:
    try: 
        num = next(it)
        print(num)
    except StopIteration:
        break