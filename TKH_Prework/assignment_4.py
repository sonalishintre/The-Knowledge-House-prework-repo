# Assignment_4.py
#Functionally Literate:
#So far all the code we created only runs once, however code can be encapsulated in a
#function to be run multiple times, and to be run with placeholder inputs
#ex1 greeting def greet(name): print "hello " + name
#the indented code runs every-time we call the function into existence greet('joe')# "hello joe" greet('sam')# "hello sam"
#functions can and usually do return a value this is not going to print, but can be assigned
#to a variable and printed def add(num1,num2): return num1+num2 add(1,2) #no output num_sum = add(1,2) print num_sum # OUTPUT: 3
    
def greet(name):
    print("hello " + name)
    
greet('joe')
greet('sam')

def add(num1,num2):
    return num1 + num2

num_sum = add(1,2)
print(num_sum)

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
def long_name(names_list):
    longest_name = ''
    for name in names_list:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name

big_name = long_name(names_list)
print(big_name)

#Output: future hendrix