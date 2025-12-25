
class Animal:

    # it is a parameterized contructor of every class meaning that every objects of this class will have these parameter
    def __init__(self, name):
        self.name = name


    # it allows us to directly print an object eg -> print (a1)
    def __str__(self):
        return f"ANimal is {self.name}"
    

    #this only works in ipynb file. yesle chai sidddai a1 matrai lekhdiye yo function ko kura print hunxa
    def __repr__(self):
        return f"animal: {self.name}"
    
    def sayhello(self):
        print (f"{self.name} says hellow")

a1 = Animal("Tommay")
a1.sayhello()

print (a1)
a1