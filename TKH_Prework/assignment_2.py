# Assignment_2
#Programming uses numbers, but thankfully you don't need to be a math genius to program. #Programming can be used to evaluate mathematical statements, you can also compare numbers to each-other #Ex1: 4+4
#Output: 8
#Ex2: 17<3#OUTPUT: False
#We can also place a condition on the result of such a test:
#Ex2 example = 7 if example > 8: print "over" else: print "under"
#OUTPUT: under
#You can do this to compare numbers to each-other
#Lastly we have lists and loops, a list is just a collection of strings, numbers, or other pieces of data nums = [1,14,32,5,7]
#here we have a list of numbers we can write a for loop to list them out for us, note the indented
#command will run on all the numbers in the list num for num in nums: print num
#Output:
#1
#14
#32
#5
#7

#ex 1
4+4

#Ex 2
17<3

#ex 3
example = 7 
if example > 8: 
    print("over")
else: 
    print("under")
    
#ex 4

nums = [1,14,32,5,7]
for num in nums:
    print(num)
    
    
#Now create a loop that compares the list of numbers provided for the number 25,print over if it is over and under if it is under
#over_under_list = [1,45,32,21,5,17,43,93]

over_under_list = [1,45,32,21,5,17,43,93]
for num in over_under_list:
    if num < 25:
        print(num,":under")
    else:
        print(num,":over")
        
#output:
#1 :under
#45 :over
#32 :over
#21 :under
#5 :under
#17 :under
#43 :over
#93 :over