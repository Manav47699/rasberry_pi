# cla = command line argumnet -> 
import sys

# print (sys.argv)   # this gives a list -> ['command_line_argument.py', 'hello', '123']

n = int(sys.argv[1])
for i in range(1, 11):
    print(f'{n}*{i} = {n*i}')


###############
'''
in the termianl do the fwollowing

python cla.py 1 2 3 -> run 
this will give the table of 1 as 1 is at index [1] -> ['cla.py', '1', '2', '3']
'''