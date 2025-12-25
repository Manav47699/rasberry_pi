def cal(a, b):
    s = a+b
    d = a-b
    m = a*b
    return s, d, m

result = cal(10, 2)

print (result)
print (type(result))


sum, diff, mul = cal(15, 2)
print(f"sum = {sum}")