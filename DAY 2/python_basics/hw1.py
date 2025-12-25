# wap to create a class named distance which has feet and inches as data member, overload any two operators
# download numpy, scikit-learn pandas, streamlit matplotlib.pyplot
class Distance:

    def __init__(self, feet, inches):
        self.f = feet
        self.i = inches
        self.conversion()

    def conversion(self):
        if self.i >= 12:
            extra_feet = self.i // 12         # / -> this gives float.   // -> this gives int  
            self.f += extra_feet
            self.i = self.i % 12      

        
    def __str__(self):
        return f"({self.f}, {self.i})"
    
    def __add__(self, other):
        new_feets = self.f + other.f
        new_inches = self.i + other.i
        return Distance(new_feets, new_inches)
    
    def __mul__(self, other):
        new_feets = self.f * other.f
        new_inches = self.i * other.i
        return Distance(new_feets, new_inches)
    

        
d1 = Distance(5, 8)
d2 = Distance(6, 4)
d3 = d1 + d2
d4 = d1 * d2
print (f"the addition of distances is: {d3}")
print (f"the product of distances is: {d4}")