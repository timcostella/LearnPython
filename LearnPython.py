# Single line comments in Python begin with hash marks

"""
    triple quotes create a multi-line comment
    multi-line comments are also used for doc strings
"""

# Printing to the console
print("hello world")


print("****************************")

# You print numbers either in quotes as strings or without quotes as integers
# You can even do math inside of the print function
print(1)
print(1+4)
# You can add parentheses to your math statements ...even inside of a print statement to force a specific order of operations
print((250 + 241 + 244 + 255) / 4)

print("****************************")

# Strings in python are enclosed in quotes
# Create strings by wrapping the text in single quotes or double quotes. That said, double quotes are preferred.
portuguese_greeting = 'Bom dia'
Greeting = "Hello"
print(Greeting)
print("****************************")

# You can check the length of a string with the len() function
print(len(Greeting))  # Prints 5

# Python has several built-in string methods that can be used to manipulate strings

# For example, you can convert a string to uppercase with the upper() method
print(Greeting.upper())  # Prints "HELLO"

# You can convert a string to lowercase with the lower() method
print(Greeting.lower())  # Prints "hello"

# You can check if a string starts with a certain substring with the startswith() method
print(Greeting.startswith("H"))  # Prints True  

# You can iterate across the characters of a string using a for loop
MyString = "Hello There Citizen"
for char in MyString:
     print(char)

# Variables can be declared on the same line (harder to read if they are the same type though)
sword, shield, armor = "long sword", "bronze shield", "rusty armor"

# Numbers in variables
Age = 41  #integer
Weight = 156.5 #float

# Integers in python are not enclosed in quotes. If you did, they become strings not ints
MyAge = 41


# Math operations in Python
a=100
b=30

sum = a + b  # Addition

diff = a - b # Subtraction

product = a * b    # Multiplication

# division of two integers will result in a float

quotient = a / b   # Division results in a float

# The // operator is used for floor division, which rounds down to the nearest integer
7 // 3
# 2 (an integer, rounded down from 2.333)

-7 // 3
# -3 (an integer, rounded down from -2.333)

# The % operator is used for modulus, which returns the remainder of a division operation
7 % 3
# 1 (7 divided by 3 is 2 with a remainder of 1)
-7 % 3
# 2 (the remainder of -7 divided by 3 is 2, because -7 is -3 * 3 + 2)


# exponents use double splats or *
# reads as "three squared" or
# "three raised to the second power"
3 ** 2
# 9

## scientific notation is also supported using a lowercase e or E
print(16e3)
#Prints 16000.0

## python can use underscores in numbers for readability instead of commas for delimiters
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000


# Similar to the ++, or -- operator in Javascript, C and C#, python has the +=, -=
# 
# operator 
star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2
# star_rating is now 2.0


# Booleans aren't enclosed in quotes, and are case sensitive
# Booleans are either True or False
IsAdult = True
IsFemale = False
# We can use not to negate a boolean value
IsAdult = not IsAdult  # Now IsAdult is False

# We can use the and operator to combine two boolean values
IsAdult = True
IsFemale = False
IsAdultAndFemale = IsAdult and IsFemale  # Now IsAdultAndFemale is False
# We can use the or operator to combine two boolean values
IsAdultOrFemale = IsAdult or IsFemale  # Now IsAdultOrFemale is True

# Variables in Python are dynamically typed, meaning you don't have to declare the type of a variable when you create it.
# A variables type can be outputed with the type() function
MyAge = 41
print(type(MyAge).__name__)


# Null variables are set to None
# We can make an "empty" variable by setting it to None. None is a special value in Python that represents the absence of a value. 
#It is not the same as zero, False, or an empty string.
MyWorth = None

# To check if something is None use the is None 
if(MyWorth is None):
    print("MyWorth is NULL/NONE")


# Python is dynamically typed, which means a variable can store any type, and that type can change.
# Other dynamically typed languages include JavaScript, Ruby, and PHP
# For example, if I make a number variable, I can later change that variable to a string
#  In almost all circumstances, it's a bad idea to change the type of a variable.
speed = 5
speed = "five"

# Languages that aren't dynamically typed are statically typed, such as Go, C, Rust 
# In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash the program.



# Strings can be concatinated via +
Name = "Joe"
Message = Greeting + " " + Name
print(Message)
print("****************************")

# Python we can create strings that contain dynamic values with the f-string syntax.
# Formatted strings are used to place different types together in one output
# Notice variables are embedded into formatted strings via the {variableName}
print(f"You are {Name}")
print("****************************")


# String can be split into a list with the split() function which will split on a space by default
FullName = "Joseph B. Hardy"
NameParts = FullName.split()
print(NameParts)
print("****************************")



# The string split function can also take a character on which to split, in this case a comma
Names="Bill,Bob,Joe,Sam"
Name = Names.split(",")
for N in Name:
    print("Hello " + N + "!")
print("****************************")


# You can check if a string contains a substring with the in operator
if "Tim" in FullName:
    print("Tim is in the full name")


# You can check if a string is alphanumeric, i.e. contains only ascii/unicode "letters" and not spaces, nonprintable characters, etc.
MyStringAlpha="abµ"
print(MyStringAlpha.isalpha()) # returns True



# Lists are created with square brackets
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Lists allow duplicates
fruits = ["apple", "banana", "cherry","apple"]
print(fruits)

# len will give you the number of elements in a list
list=[1,2,3]
len(list)  # prints 3


# You can index into a list, lists are zero based
print(fruits[0])
print("****************************")

# Iterate over a list using len of list
# The len() function returns the number of elements in a list which will be one more than the last index number, 
# but since range is exclusive of the end number we can use it directly
for i in range(0, len(fruits)):
    print(fruits[i])

# Iterate over the elements in a list via the for var in list
for fruit in fruits:
    print(fruit)
print("****************************")


# Lists can contain string, int, and boolean and these can be mixed in the same list
MixedList = ["One",True, 1]
print("****************************")


# Adding to a list ListName.append("ThingToAdd")
fruits.append("pear")
print(fruits)
print("****************************")


# You can add an item to a list at a specific spot (index) in the list
fruits.insert(0,"pinneaple")
print(fruits)

# Two lists can be concatenated together
veggies = ["broccoli","lettuce","peas"]
food = fruits + veggies
print (food)

print("****************************")


# Removing Items from a list, if the list contains duplicates the first matching element is removed
fruits.remove("apple")
print(fruits)
print("****************************")

# You can remove an item from a list by index with the pop() function
# By default pop() removes the last item in the list
fruits.pop()  # removes the last item in the list
print(fruits)
print("****************************")

# You can also specify the index of the item to remove with pop()
fruits.pop(0)  # removes the first item in the list
print(fruits)
print("****************************")







# Comparisons can be done with ==, !=, <=, >=, <, > which result in True or False

# < "less than"
# > "greater than"
# <= "less than or equal to"
# >= "greater than or equal to"
# == "equal to"
# != "not equal to"

# For example:

5 < 6 # evaluates to True
5 > 6 # evaluates to False
5 >= 6 # evaluates to False
5 <= 6 # evaluates to True
5 == 6 # evaluates to False
5 != 6 # evaluates to True


# True and True == True
# True and False == False
# False and False == False

# True or True == True
# True or False == True
# False or False == False

# python supports the logical operator - not 
# not True == False



# If, elif and else
if MyAge >= 40:
    print(f"You are quite old!")
elif MyAge >=30:
    print(f"You are still young!")
else:
    print("You are very very young, get to work")


# Functions are declared with the def keyword
# The function body is indented with 4 spaces or one tab
# Functions must be declared before they are called
# Most python scripts have an entrypoint function called main() that is called at the end of the file and runs the script
# When no return value is specified in a function, it will automatically return None.


def SayHello(fname, lname):
    print(f"Hello {fname} {lname}")

SayHello("Tim","Costella")

# Functions can return values with the return keyword.
def Add(a,b):
    return a + b

Result = Add(1,2)
print(Result)

# Functions can return multiple values
def AddAndSubtract(a,b):
    return a + b, a - b

addition, subtraction = AddAndSubtract(1,2)
print(f"Addition Result: {addition} and Subtraction Result: {subtraction}")


# Parameters are the names used for inputs when defining a function. 
#Arguments are the values of the inputs supplied when a function is called.

# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)


# In Python you can specify a default value for a function argument. It's nice for when a function has arguments that are optional. 

def get_greeting(email, name="there"):
    print("Hello", name, "Welcome! You've successfully registered with your email:", email)

get_greeting("jhardy@example.com", "Joe")


get_greeting("jhardy@example.com")



# Reading files in python, 'r' is read-only
# Notice backslash is a special character, the escape characater, and must be escaped by itself 
with open('C:\\Users\\timco\\.aws\\credentials', 'r') as file:
# Read the entire content of the file
   content = file.read()
   print(content)


# Variables defined outside all functions are global variables and can be used inside a funtion with (or without) the global keyword
c = 13
def MyFunction():
    # global c
    return c + 15

result = MyFunction()
print(result)

# Variables defined inside a function are local variables and aren't accessible outside of the function scope


# Python supports using binary numbers, if you add 0b to the front of a number it will be treated as binary
 print(0b0001)
# Prints 1

 print(0b0101)
# Prints 5

#Bitwise and operator is &
#Bitwise and means to take the binary representation of two numbers and do a column by column AND(&) of bits in the column
#0101 is 5
#0111 is 7

#0101
#&
#0111
#=
#0101

#Bitwise or operator is |
#Bitwise or means to take the binary representation of two numbers and do a column by column OR(|) of bits in the column

# The int() function can be used to convert a number from binary to decimal
# It takes the number as string variable and the base of the number as parameters
binary_string = "101"
print(int(binary_string,2))
# prints 5


# For loops allow you to iterate over a range
# This will print the numbers 0-99
# The numbers a, b in range(a, b) are inclusive of a and exclusive of b. So range(0, 10) includes 0 to 9.
for i in range(0, 100):
        print(i)

# the range function can also take a third parameter, the step
# This will print the numbers 0-99 in increments of 5
for i in range(0, 100, 5):
        print(i)

# You can even count backwards with a negative step
# This will print the numbers 100-0 in decrements of 5
for i in range(100, 0, -5):
        print(i)


# Python supports an array like structure called lists
# Lists are declared using square brackets
# Lists can contain items of any data type
MyPackingList = ["shoes", "hat", "sunscreen", "beer"]

# Lists are indexed based on 0, so index 0 is "shoes" above

# You can access an item in a list by using it's index:
MyPackingList[1]=="hat" # returns True

# To find the number of items in a list you can use the len function
# The length of list is always 1 more than the last index number
len(MyPackingList) == 4


# Lists can be declared using multiple lines
OurAges = [
10,
44,
45
]

# You can change the elements of a list via the index number
OurAges[0] = 11
print(OurAges)

# You can declare an empty list like so MyEmptyList = []
MyList = []

# You can add elements to the end of a list with the append function
MyList.append("Joe")

# You can remove elements from the end of a list using the pop function
MyList.pop()

print(MyList)

# The pop function can remove any element of a list if you specify the index
AnotherListOfVeggies = ["cabbage", "carrots", "apples", "lettuce", "tomatoes"]
AnotherListOfVeggies.pop(2) 
AnotherListOfVeggies

# You can use a for loop to easily iterate over a list
sports =["football","soccer","baseball","basketball","tennis"]

for i in range(0, len(sports)):
    print(sports[i])

# An even better of iterating over a list is to use the for in loop
for sport in sports:
    print(sport)

# Lists can be sliced using the colon operator
# The colon operator takes two parameters, the start and the end and an optional step parameter
# The start is inclusive and the end is exclusive

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]

# If you leave off the start or end, it will default to the beginning or end of the list
print(scores[:5])
# Prints [50, 70, 30, 20, 90]

print(scores[2:])
# Prints [30, 20, 90, 10, 50]

# You can also use negative numbers to slice from the end of the list
print(scores[-3:])
# Prints [90, 10, 50]

print(scores[:-1])
# Prints all the list items except the last item
# You can also slice the last character off a string using this syntax
# Prints [50, 70, 30, 20, 90, 10]

# You can even just specify the step
print(scores[::2])
# Prints [50, 30, 90, 50]

# Two lists can be concatenated together with the + operator
# This will create a new list with the elements of both lists
# The original lists will not be modified
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
# Prints [1, 2, 3, 4, 5, 6]

# You can append one list to another
list4 = ["A","B","C"]
list5 = ["D","E","F"]
list4.append(list5) # return None, but list4 now has a new element which is list 5 ["A","B","C",["D","E","F"]]
print(list4)

# If you want to add the elements of a list to the end a current list use extend() instead
list4 = ["A","B","C"]
list5 = ["D","E","F"]
list4.extend(list5)  # return None, but list4 is now ["A","B","C","D","E","F"]
print(list4)

# YOu can check if a list contains an element with the in operator
# This will return a boolean value
# This is case sensitive
print("apple" in ["apple", "banana", "cherry"])
# Prints True

# You can also check if a list does not contain an element with the not in operator
print("apple" not in ["apple", "banana", "cherry"])
# Prints False

# You can check the position of a specific element in the list with the index() function
Mylist = [1,"A", 3, "B", "Z"]

Mylist.index("A")  # prints 1
Mylist.index("Z")  # prints 4

# You can delete elements from a list with the del keyword
# This will remove the element at the specified index
# This will modify the original list
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print(fruits)
# Prints ["apple", "cherry"]

# You can also delete the entire list with the del keyword
del fruits[:]
# This will throw an error if you try to print fruits
# print(fruits)

# You can use slices to delete multiple elements from a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
del fruits[1:3]
print(fruits)
# Prints ["apple", "date", "elderberry"]

# To check if a list is empty you can check the length of the list
if len(fruits) == 0:
   print("Empty list")

# List can of course contain lists
myList = [1,2,[9,8,7],4,5]

# You can use isinstance to check if a item from a list is an integer, list etc.
for item in myList:
    print(item)
    print(type(item))
    if(isinstance(item, list)):
        print(f"{item} is a list")

# To reverse the order of a list
def reverse_list_ver1(items):
    reversed_list = []
    i = len(items) -1 
    while i > -1:
        reversed_list.append(items[i])
        i -= 1
    return reversed_list

# Reverse the list using a range that counts backwards to -1 (inclusive of 0) from the last index of the list len(items) -1 
def reverse_list_ver1(items):
    reverse_list = []
    for i in range(len(items) -1, -1, -1):
        reverse_list.append(items[i])
    return reverse_list

#If you copy a list to another variable, the new variable will point to the same list in memory
# This means that if you change the new variable, the original variable will also change
MyList = [1,2,3]
MyOtherList = MyList
MyOtherList[0] = 4
print(MyList) # Prints [4,2,3]

# To copy a list to another variable without pointing to the same list in memory, you can use the copy() function
MyList = [1,2,3]
MyOtherList = MyList.copy()
MyOtherList[0] = 4
print(MyList) # Prints [1,2,3]

# You can use a slice to copy a list to another variable without pointing to the same list in memory

MyList[1,2,3]
MyOtherList = MyList[:]
MyOtherList[0] = 4
print(MyList) # Prints [1,2,3]



# Tuples are like lists but are immutable, meaning they cannot be changed
# Tuples are declared with parentheses
# Tuples can contain items of any data type
MyTuple = ("shoes", "hat", "sunscreen", "beer")
MyOtherTuple =("book", "sunglasses", "towel", "snorkel")

# Accessing a tuple is the same as a list
print(MyTuple[1])

# Tuples can be stored in a list
MyList = [MyTuple]
MyOtherGreatList = [("Kia","Kacey","2021","Black"), ("Nissan","Roger","2018","Red")]

# You can access a tuple in a list like so
print(MyList[0])    # Prints ("shoes", "hat", "sunscreen", "beer")
print(MyList[0][0]) # Prints "shoes"
print(MyList[0][1]) # Prints "hat"

# You can unpack a tuple into variables
a, b, c, d = MyTuple    # a = "shoes", b = "hat", c = "sunscreen", d = "beer"
print(a)

# Multiple tuples can be concatenated together into 1:
CombinedTuple = MyTuple + MyOtherTuple
print(CombinedTuple)

# When you return multiple values from a function, you're actually returning a tuple.


# Dictionaries allow us to store key value pairs in Python
MyCharacter = {
     "name": "Joe Bream",
     "level": "25",
     "class": "Hunter",
     "id": "122323324433"
}

# Dictionaries are accessed via the key
MyCharacter["name"]

# Blank dictionaries are created with {}
MyPlanetDictionary = {}

# Add items to dictionary like so
MyPlanetDictionary["mars"] = "red"
MyPlanetDictionary["earth"] = "blue"
MyPlanetDictionary["neptune"] = "purple"

print(MyPlanetDictionary)

# You can update a dictionary key value but reassigning it
MyPlanetDictionary["earth"] = "blueish"

# You can delete a dictionary key value using del keyword
del MyPlanetDictionary["mars"]

# You use the in keyword to check if a key exists in a dictionary
"earth" in MyPlanetDictionary  # Prints True

# You can get the number of key value pairs in a dictionary with the len function
len(MyPlanetDictionary)  # Prints 2

# You can iterate over a dictionary using the for in syntax
for planet in MyPlanetDictionary:
     print(f"{planet} ->  {MyPlanetDictionary[planet]}")


# You can nest disctionaries in dictionary
MySolarSystems = {}
MySolarSystems["sol"] = MyPlanetDictionary

# You can chain keys in a dictionary to access a nested value
print(MySolarSystems["sol"]["earth"])

# Sets are like lists, but do not allow duplicates
# Sets are unordered and they guarantee uniqueness
# You declare a set using {} like you would a dictionary
MySet = {"Tim", "John", "Brad", "Brandon"}

# You declare an empty set using the set() keyword
MyEmptySet = set()


# You use the add keyword to add items to a set
MyEmptySet.add("Harry")
MyEmptySet.add("Sally")

print(MyEmptySet)

# You can remove items from a set using the remove keyword
MyEmptySet.remove("Sally")


# You can typecast? a list directly into a set and it will remove all duplicates
set(MyList)

# You can typecast a set directly into a list 
list(MyEmptySet)

# You can subtract a set from another
my_character_set = {"Larry", "Curly", "Mo", "Sandy"}
my_female_character_set = {"Sandy"}
my_male_character_set = my_character_set - my_female_character_set
print(my_male_character_set) # prints Larry Curly Mo

# Python has a try/exception block which can catch errors
try:
     12/0
except Exception as e:
     print(e)

# You can raise your own exceptions with the raise keyword
# This will throw an error with the message "This is an error"
raise Exception("This is an error")


# When handling exceptions, it’s important to catch the most specific ones first, because Python stops checking once it finds a matching exception handler


# You can use a with block to open a file for reading
# with open(path_to_file) as f:
    # do something with f (the file) here


# Python classes are defined with a class keyword
# In Python, if you name a method __init__, that's the constructor and it is called when a new object is created.

class car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

# If you print a class you get a default output that isn't very useful, but you can override the default print operation
MyCar = car("Ford", "F150", Blue)
print(MyCar)


#The __str__ method (short for "string") lets us change what is printed . It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function.

class UpgradedCar:
    def __init__(self, make, model, color, speed):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed

    def __str__:
        return f"The best car ever is a {self.color} {self.make} {self.model} that can go to speeds up to {self.speed}"

MyNewCar = UpgradedCar("Ford", "F150", Blue)
print(MyNewCar)


# In Python, the built-in map function takes a function and an iterable (in this case a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.
# With map, we can operate on lists without using loops and nasty stateful variables. For example:

def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(list(squared_nums))
# [1, 4, 9, 16, 25]


# The built-in filter function takes a function and an iterable (in this case a list) and returns an iterator that only contains elements from the original iterable where the result of the function on that item returned True.
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]


# The join ffunction can take an iterable and combine them together with whatever character you provide
word_list = ["Hello", "I", "am", "Bob"]
sentence = " ".join(word_list)
print(sentence)



# The python switch/case statement is called a match/case statement
def switch_case_example(value):
    match value:
        case 1:
            return "You selected option 1"
        case 2:
            return "You selected option 2"
        case 3:
            return "You selected option 3"
        case _:
            return "Invalid option"
        
     
        
