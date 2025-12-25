# 1st way to use decorators
def mydec1(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper
    
@mydec1
def helo():
    print ("say hellow")

helo()


# 2nd way to use decoators
def mydec2(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

def heloo():
    print ("SAYY")

heloo = mydec2(heloo)
heloo()



### 

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"time elpased={(end - start):.8f} seconds")
        return result

    return wrapper

# @timer 
# def fibo(n):
#     if n ==1 or n==2:
#         return n
#     else:
#         return fibo(n-1) + fibo(n-2)

@timer
def fact(n):
    f = 1
    for i in range (1, n+1):
        f = f *i
    return f

fact(20)