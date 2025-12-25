def simpleinterest(p, t, r):
    return (p*t*r)/100

def compoundinterest(p, t, r):
    return p * ((1+r/100)**t) -p

if __name__ == "__main__":
    p = int(input("ENter principle: "))
    t = int(input("ENter the time period: "))
    r = int(input("ENter thr rate: "))

    print (f"simle interest is {simpleinterest(p, t, r):.3f}")
    print (f"compund interest is {compoundinterest(p, t, r):.3f}")
    



# why not wokring boss????????