# Assignment_5.py
#all strings and lists have individual characters and items respectfully represented by an index number
#this starts at 0, and can be accessed in bracket notation thing = "car" thing[0]#c thing[2]#r list = ["one",2,"3hree"] list[2] # 3hree
# print both lists and then return the even one and print

thing = "car"
thing[0]
thing[2]
list1 = ["one",2,"three"]
list1[2]

#create a function that takes the below list of names, and separates them into two lists one of the names with an even number of letters and one with an odd number of letters. Then take the first letter of each of the names in the even list and make it the letter "b", take the last letter in each of the names in the odd list and make them
#a “c” Print both lists and then return the even one to a variable named even_list and print it again.
#names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]

names_list = ["bob","jimmy","max b", "bernie", "jordan", "future hendrix"]
even_list =[]
odd_list =[]
def even_odd_list(names_list):
    for name in names_list:
        name = name.strip()
        if len(name) % 2 == 0:
            even_change = list(name)
            even_change[0] = "b"
            even_change =''.join(even_change)
            even_list.append(even_change)
        else:
            odd_change = list(name)
            odd_change[-1] = "c"
            odd_change =''.join(odd_change)
            odd_list.append(odd_change)
    return even_list, odd_list

even_list, odd_list = even_odd_list(names_list)
print(even_list)
print(odd_list)

#Oputput:
#['bernie', 'bordan', 'buture hendrix']
#['boc', 'jimmc', 'max c']
