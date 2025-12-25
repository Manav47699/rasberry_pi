# SYNTAX -> func_name = lambda arg1, arg2 : k_return_grane_ho
add = lambda a, b : a+b
print (add(1, 2))



#used for sorting
students = [("kera_bari", "mausam_vai", 1), ("jhapa","Himal", 2), ("dharan", "manav", 3)]

students_sort = sorted(students)
print (students_sort)

sorted_form_index_1 = sorted(students, key = lambda x: x[1])
sorted_from_index_2 = sorted(students, key = lambda x: x[2])



#used for filtering
nums = [1, 2, 3, 4,8 ,5 ,6 ]

evens = list(filter(lambda x: x%2==0, nums))
print(evens)


#used in mapping
numbers = [12, 3, 4, 5, 6, 6, 8]
square = list(map(lambda x : x*x, nums))
print(square)