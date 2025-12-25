# it saves memory as it only producces the result when needed

def square(x):
    for i in range (x):
        yield i*i                      

square(10)

for num in square(10):
    print (num)



# why use it????????