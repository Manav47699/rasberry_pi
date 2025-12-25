from module import *
from module import compoundinterest, simpleinterest
import module

p = int(input("ENter principle: "))
t = int(input("ENter the time period: "))
r = int(input("ENter thr rate: "))

print (f"simle interest is {simpleinterest(p, t, r):.3f}")
print (f"compund interest is {compoundinterest(p, t, r):.3f}")

print(f"simple interest = {module.simpleinterest(p, t, r):3f}")
    
