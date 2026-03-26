#data types are categories of values that we store in the memory.
# 1 = numeric, eg int, float, complex
# 2 = string
# 3 = sequence eg list, tuple, range
# 4 = mapping eg dictionary
# 5 = set 
# 6 = boolean 

#integers (int) are whole numbers from 0 to any number
myNum = 200 
print(type(myNum)) 

#a float is any number with a decimal point. eg 3.14, 0.5, -2.5
myNum = 200.0
print(type(myNum))

#let myNum = 200, or var myNum = 200;, or myNum = int(200) are all the same thing in javascript. if its for c language, you would say int myNum = 200. 

# complex number
num1 = 2+3j
print(type(num1))

# string
# a string is a collection of characters eg our names, any values in quotes is what we call a string
name = "Mercy"
my_num = "200"

# the process of creating a variable is called declaring 
# the process of assigning a value to a variable is called initializing.
# in python we declare and initialize a variable in one line, at the same time eg name = "Mercy", num1 = 2+3j, my_num = "200".

# sequence datatype 
# sequence are variables that can store more than one value at a time. eg list, tuple, range.

# first sequence datatype is list. a list is a collection of items that are ordered and changeable. it allows duplicate members. we create a list using square brackets [].
# a list is identified by square brackets [] and the items in a list are separated by commas. eg numbers = [1, 2, 3, 4, 5]. we can also have an empty list eg numbers = [].

numbers = []
numbers2 = [5, 10, 15, 20]

print(name)
print(type(numbers2))
print(numbers2)

print(numbers2[0]) #this is how we access items in a list. we use the index number of the item we want to access. the index number starts from 0. so numbers2[0] will give us 5
print(numbers2[2]) #this will give us 15
print(numbers2[3]) #this will give us 20    
print(numbers2[-1]) #this will give us 20, because -1 is the index number of the last item in the list.

print(numbers2[1] + numbers2[-1]) #this will give us 30, because numbers2[1] is 10 and numbers2[-1] is 20.

myStuff = ["Mercy", 200, 3.14, 2+3j, [1, 2, 3], (4, 5, 6), {"name": "Mercy", "age": 30}, True]
print(myStuff)

# tuple is like a list, a list takes on one or more values of any kind and are identified by parentheses
my_tuple = (1,5,7,4,9)
print(my_tuple[4])

# mapping is a collection of values that are identified by their own keys eg dictionary. a dictionary is a collection of key-value pairs that are unordered, changeable and indexed. we create a dictionary using curly braces {}. eg my_dict = {"name": "Mercy", "age": 30}. we can also have an empty dictionary eg my_dict = {}.

my_dict = {"name": "Mercy", "age": 30}

# dictionary
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car.keys()) #this will give us the keys of the dictionary
print(car.values()) #this will give us the values of the dictionary

car["name"] = "Mercedes" #this is how we add a new key-value pair to the dictionary.

# below i'm accessing all values in a dictionary
print(car.values())
print(car["model"])

# set is an unordered collection of unique data
my_things = {10,20,20,10,20}
print(my_things)

my_things.add(50)
print(my_things)

my_things.discard(10)
print(my_things)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1 & set2) #intersection
print(set1 | set2) #union
print(set1 - set2) #difference
print(set1 ^ set2) #symmetric difference
