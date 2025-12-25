# it is a built in module -> counter _> it is a class that counts
# it gives a dictonary with the object of list as key and its frequency in the list as the vallue
from collections import Counter


alist = ["manav", 1, 2,1,1, "manav"]
count = Counter(alist)
print(count)    
print(count[1])        #this gives count of 1 in the list -> 3          
print(type(count))

