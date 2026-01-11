
# Single line comments in Python begin with a hash mark "#". 
# Comments are very import for us and future developers to understand the purpose of a line of code, function, etc.

"""
    triple quotes create a multi-line comment, it is easier than starting every line with a comment.
    multi-line comments are also used for doc strings
"""

# To use external modules (code not in your file) you use the import function to make them available to your code
# There are various ways to import code:

# from file import className, variable name, etc.
# from file import *
# import module
import random


# Printing to the console, you have to start any new language by printing "hello world", it is the rule.
print("hello world")


print("****************************")

# You print numbers either in quotes as strings or without quotes as integers or floats

print("1") # prints 1 as a string
print(2) # prints 2 as an integer
print(3.0) # prints 3.0 as a float


print("****************************")

# You can even do math inside of the print function
print(1+4)
# You can add parentheses to your math statements ...even inside of a print statement to force a specific order of operations
print((250 + 241 + 244 + 255) / 4)


print("****************************")

# Strings in python are enclosed in quotes
# Create strings by wrapping the text in single quotes or double quotes.
# Double quotes are preferred.

character_greeting = 'Good day sir'
character_greeting_alt = "Hullo ther'"
character_greeting_another = "hiya"

print(character_greeting)
print("****************************")

# You can check the length of a string with the len() function
print(len(character_greeting))  # Prints 12

# Python has MANY built-in string methods that can be used to manipulate strings

# For example, you can convert a string to uppercase with the upper() method
print(character_greeting.upper())  # Prints "GOOD DAY SIR"

# You can convert a string to lowercase with the lower() method
print(character_greeting_alt.lower())  # Prints "hullo ther'"

# You can convert a string to Proper case using the capitalize() method
print(character_greeting_another.capitalize())  # Prints "Hiya"

# You can replace characters in a string with the replace() method
print(character_greeting_another.replace('i', 'e'))  # Prints heya

# You can remove whitespace from the beginning or end of a string with the strip method
a_lot_of_whitespace = " oh sorry sir "
print(a_lot_of_whitespace.strip()) # Prints "oh sorry sir" 

# You can check if a string starts with a certain substring with the startswith() method
# Returns a boolean value, either True or False
print(character_greeting.startswith("H"))  # Prints False  

print("****************************")
       
# You can iterate across the characters of a string using a for loop
character_greeting_senior = "Hello There Citizen"
for char in character_greeting_senior:
     print(char)  # prints H
                  # prints e
                  # prints l
                  # prints .... n
 
 print("****************************")

# Variables can be declared on the same line (harder to read if they are the same type though)
sword, shield, armor = "bastard sword", "wooden shield", "dented armor"

print("****************************")

# Numbers in variables
character_age = 45  # integer - whole number
character_weight = 156.5 #float - not a whole number

# Integers in python are not enclosed in quotes. If you did, they become strings not ints
character_age_alt = "46"  # string not int, so can't do math with it, etc


print("****************************")

# Math operations in Python

a = 100
b = 30

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

print("****************************")

## python can use underscores in numbers for readability instead of commas for delimiters
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

print("****************************")

# Similar to the ++, or -- operator in Javascript, C and C#
# python has the +=, -=, /=, *= operators 

character_level = 4
character_level += 1 # character_level is now 5

character_stamina = 4
character_stamina *= 2 # character_stamina is now 8


print("****************************")

# Booleans aren't enclosed in quotes, and are case sensitive
# Booleans are either True or False
character_is_female = True
character_is_adult = False

print("****************************")

# We can use not to negate a boolean value
character_is_adult = not character_is_adult  # character_is_adult is now True
character_is_female = not character_is_female # character_is_female is now False

print("****************************")

# We can use the and operator to combine two boolean values
character_is_elf = True
character_is_archer = False

character_is_elf_archer = character_is_elf and character_is_archer  # False, True and False = False

character_is_elf_or_archer = character_is_elf or character_is_archer # True, True or False = True

print("****************************")

# Variables in Python are dynamically typed, meaning you don't have to declare the type of a variable when you create it.
# In a typed language you might declare a variable like so: variable_type variable_name = value
# int character_age = 54

# A variables type - boolean, float, integer, string, etc. can be outputed with the type() function
character_age = 100
print(type(MyAge).__name__) # prints int

print("****************************")

# Null variables are set to None
# We can make an "empty" variable by setting it to None. 
# None is a special value in Python that represents the absence of a value. 
# It is not the same as zero, False, or an empty string.

character_blow_count = None

# To check if something is None use the is None 
print(character_blow_count is None)  # prints True

print("****************************")

# Python is dynamically typed, which means a variable can store any type, and that type can change.
# Other dynamically typed languages include JavaScript, Ruby, and PHP
# For example, if I make an integer variable, I can later change that variable to a string
#  In almost all circumstances, it's a bad idea to change the type of a variable.
character_speed = 5
character_speed = "five"

# Languages that aren't dynamically typed are statically typed, such as Go, C, Rust 
# In a statically typed language, if you try to assign a value to a variable of the wrong type, an error would crash the program.

print("****************************")

# Strings can be concatinated via +
character_silly_greeting = "Howdy doody do you do"
character_first_name = "Barty"

character_response = character_greeting + " " + character_first_name

print(character_response) # prints "Howdy doody do you do Barty"

print("****************************")

# Python we can create strings that contain dynamic values with the f-string syntax.
# Formatted strings are used to place different types together in one output
# Notice variables are embedded into formatted strings via the {variableName}

character_age_ancient = 540
print(f"You are {character_age_ancient} years old")  # prints "You are 540 years old"

print("****************************")


# String can be split into a list, basically what would be called an array in other languages, with the split() function which will split on a space by default
character_full_name = "Barty B. Bossman"
character_name_parts = character_full_name.split()
print(character_name_parts) # prints "['Barty', 'B.', 'Bossman']"


# The string split function can also take a character on which to split, in this case a comma

character_first_names = "Billy,Bobby,Barty,Benny"
first_names_list = character_first_names.split(",")
print(first_names_list) # prints ['Billy', 'Bobby', 'Barty', 'Benny']


print("****************************")


# You can check if a string contains a substring with the in operator
character_name_to_find = "Bessy"
print(character_name_to_find in character_first_names) # Prints False

print("****************************")

# You can check if a string is alphanumeric, i.e. contains only ascii/unicode "letters" and not spaces, nonprintable characters, etc.
some_odd_string="abµ"
print(some_odd_string.isalpha()) # returns True

print("****************************")

# Python supports an array like structure called lists
# Lists are declared using square brackets
# Lists can contain items of any data type
inventory_items = ["old socks", "penny", "chipped knife", "rotten apple"]

# You can access an item in a list by using it's index:
# lists are zero based
print(inventory_items[0]) # prints "old socks"
print(inventory_items[3]) # prints "rotten apple"

# Lists allow duplicates
inventory_items_with_duplicates = ["old socks", "penny", "chipped knife", "rotten apple", "rotten apple"]

# len will give you the number of elements in a list
len(inventory_items)  # prints 4

# Lists can be declared using multiple lines
character_ages = [
12,
47,
502
]

# You can change the elements of a list via the index number
character_ages[0] = 11
print(character_ages)


# You can declare an empty list like so MyEmptyList = []
characters_coming_soon = []


# Lists can contain string, int, and boolean and these can be mixed in the same list
mixed_up_inventory = ["1", "Rotten Apple", "False", "Smelly Socks", "3.42"]


# You can add additional items to a list via the append() method
# ListName.append("ThingToAdd")

inventory_items.append("broken bottle")
print(inventory_items)


# You can add an item to a list at a specific spot (index) in the list
inventory_items.insert(0,"war hammer")
print(inventory_items)

# Two lists can be concatenated together - combined into 1 new list
another_characters_inventory = ['peach', 'ripped cloth', 'boots']

group_inventory = inventory_items + another_characters_inventory
print (group_inventory)

# You can use remove() to remove items from a list, if the list contains duplicates the first matching element is removed
another_characters_inventory.remove("peach")
print(another_characters_inventory)

# You can remove an item from a list by index with the pop() function
# By default pop() removes the last item in the list
inventory_items.pop()  # removes the last item in the list
print(inventory_items)


# You can also specify the index of the item to remove with pop()
inventory_items.pop(0)  # removes the first item in the list
print(inventory_items)

print("****************************")


# You can radomize a list with random.shuffle
# requires you to import random
my_numbers_list = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(my_numbers_list)
print(my_numbers_list)


# You can find the min and max of a list 
characters_iq_list = [34.00, 67.00, 34.54, -5.00, 123.45, 2.34]

print(min(character_iq_list)) # prints -5
print(max(characters_iq_list)) # prints 123.45



print("****************************")


# For loops allow you to iterate over a range of numbers, items, etc.

# This will print the numbers 0-99
# The numbers a, b in range(a, b) are inclusive of a and exclusive of b. So range(0, 10) includes 0 to 9.
for i in range(0, 100):
        print(i) # prints 0 to 99

# the range function can also take a third parameter, the step
# This will print the numbers 0-99 in increments of 5
for i in range(0, 100, 5):
        print(i) # prints 0, 5, 10 ...95

# You can even count backwards with a negative step
# This will print the numbers 100-0 in decrements of 5
for i in range(100, 0, -5):
        print(i) # prints 100, 95, 90 ...5


print("****************************")

# Iterate over a list using len(the_list) and a for loop
# for i in range(0, len(the_list)):
        # print(i)

# The len() function returns the number of elements in a list...
# which will be one more than the last index number of the listm since lists indexes are 0 based. 

# We can use the range function to iterate, walk through a list of items though...since
# range is inclusive of the first number and exclusive of the end number

# Example:
# for i in range (1, 10):
#       print(i)  # this only prints 1 through 9


for i in range(0, len(inventory_items)):
    print(inventory_items[i])

# Iterate over the elements in a list via the for var in list
for inventory_item in inventory_items:
    print(inventory_item)

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

character_age = 43

if character_age >= 40:
    print(f"You are quite old!")
elif character_age >=30:
    print(f"You are still young!")
else:
    print("You are very very young, get to work")

print("****************************")


# Functions are declared with the def keyword
# The function body is indented with 4 spaces or one tab
# Functions must be declared before they are called
# Most python scripts have an entrypoint function called main() that is called at the end of the file and runs the script
# When no return value is specified in a function, it will automatically return None.


def say_hello(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")

say_hello("Billy","Baloney")  # prints Hello Billy Baloney!


# Functions can return values with the return keyword.
def add(a,b):
    return a + b

addition_result = add(1,2)
print(addition_result) # prints __ i'll let you figure it out

# Functions can return multiple values
def add_and_subtract(a,b):
    return a + b, a - b

addition, subtraction = add_and_subtract(19, 4)
print(f"Addition Result: {addition} and Subtraction Result: {subtraction}")


print("****************************")

# Parameters are the names used for inputs when defining a function. 
#Arguments are the values of the inputs supplied when a function is called.

# a and b are parameters
def add(a, b):
    return a + b

# 5 and 6 are arguments
sum = add(5, 6)


print("****************************")

# In Python you can specify a default value for a function argument. 
# It's nice for when a function has arguments that are optional. 

def dungeon_greeting(name="Unnamed Explorer"):
    print(f"Hello {name}, You are about to die")

dungeon_greeting("Billy Baloney")
dungeon_greeting()


print("****************************")


# Reading files in python, 'r' is read-only
# Notice backslash is a special character, the escape characater, and must be escaped by itself 
# using with will automatically close the file when you exit the with block, I think...
with open('C:\\Users\\hero\\super_secret_file', 'r') as file:
# Read the entire content of the file
   content = file.read()
   print(content)


# Variables defined outside all functions are global variables and can be used inside a funtion with (or without) the global keyword
armor_strength = 13
def hit_armor(damage):
    global armor_strength
    return armor_strength - damage

armor_left = hit_armor(5)
print(armor_left)

# Variables defined inside a function definition are local variables and aren't accessible outside of the function definition (scope)

print("****************************")

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

# You can retrieve the value for a specified key with the get() method. 
# get() has an optional default value that will be returned if the key you specified is not found

MyPlanetDictionary.get("earth", "not found")  #returns "blue"
MyPlanetDictionary.get("saturn", "not found")  #returns "not found"


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
try:
    with open(file_path, 'r') as file:
    content = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    return False
except Exception as e:
    print(f"An error occurred: {e}")
    return False 


# Python classes are defined with a class keyword
# In Python, if you name a method __init__, that's the constructor and it is called when a new object is created.

class car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

# If you print a class you get a default output that isn't very useful, but you can override the default print operation
MyCar = car("Ford", "F150", "Blue")
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

MyNewCar = UpgradedCar("Ford", "F150", "Blue")
print(MyNewCar)


### Classes have methods, or functions that act on the instance of the class.  
### The first parameter is always the instance of the class that the method is being called on and we use 'self' for this

class MySportsCar:
    def __init__(self, make, model, color, speed, price, x, y, z):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed
        self.x = x
        self.y = y
        self.z = z 
        # You can create private properties or methods by starting them with two underscores __
        self.__price = price


    def __str__:
        return f"The best car ever is a {self.color} {self.make} {self.model} that can go to speeds up to {self.speed}"

    def move(self, x, y, z):
        self.x += x
        self.y += ys
        self.z += z

    # Python allows for operator overload, by default you can't add (+) one instance of a object to another, unless you define an add method 
    def __add__(self, car):
        return self.x + car.x
    
    # Now I can add two car objects together to get the combined x positions, not so useful in this case


MyPorsche = MySportsCar("Porsche", "Some Expensive Model", "Cherry Red")
MyPorsche.move(1,1,1)

# Python supports inheritance - one class can inherit the properties and methods from a parent class
# You add the parent class inside of paranthesis when you define the child class
class MyRaceCar(MySportsCar):
     def __init__(self, make, model, color, speed, price, x, y, z, max_acceleration):
         # We can call the class's parent constructor or methods by using the super() method
         super().__init__(self, make, model, color, speed, price, x, y, z)
         self.max_acceleration = max_acceleration


# In Python, the built-in map function takes a function as an argument and an iterable (list, etc.) as inputs. 
# It returns an iterator that applies the function to every item, yielding the results.
# With map, we can operate on lists without using loops.

# the map function is an example of a higher-order function - which is a function that can accept another function
# as an argument or returns a function

def square(x):
    return x * x

nums = [1, 2, 3, 4, 5]
squared_nums = map(square, nums)
print(squared_nums)
# [1, 4, 9, 16, 25]


# The built-in filter function takes a function and an iterable (in this case a list) and 
# returns an iterator that only contains elements from the original iterable where the result of the function 
# on that item returned True.
def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]


## Add something about the reduce function


## Add something about the zip function



# The join function can take an iterable and combine them together with whatever character you provide
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
        
     
        
# The builtin in python module sys lets us pass in arguments to our script via the commandline
# The list sys.argv is a list of strings representing arguments passed to the script. 
# The first element of sys.argv[0] is the name of the script

# We can check that our script was passed at least 1 argument like so
# If we didn't get the correct number of arguments you can use the sys.exit(1) to exit the script 
if len(sys.argv) < 2:
        print("Usage python3 main.py <argument> <argument2>")
        # sys.exit(1)


# python supports ternary expressions which are used in functional programming - in order to make things harder to debug ;)
# no it isn't to make the code harder to debug, I just don't like functional programming, at least not yet
# format of a ternary expression is:  value if condition else other_value
age  = 50
results = "You are old" if age > 45 else "You are young"  
print(results)


# In python functions can be assigned like other variables/objects
def subtract( num1, num2):
    return num1 - num2

sub = subtract
sub(5, 2) # returns 3


# When you pass a variable into a function as an argument it can either be passed by reference or value. 
# When passed by value, you are essentially passing a copy of the variable into the function.  '
# If you modify the copy nothing happens to the original variable 

num = 10
def increase_number_by_10(number):
    number += 10
    print(number)

increase_number_by_10(num) #prints 20
print(num) # prints 10

# In python integers, floats, strings, booleans, tuples are passed by value

# Alternatively the variable may be passed by reference, in which case if the variable is modified in the function
# the original is also modified

# lists, dictionaries, and sets are passed by reference

name_list = ["Harry", "Sally", "Joe", "Iola"]

def modify_list(list_to_modify):
    list_to_modify.append("Frank")
    print(list_to_modify)

modify_list(name_list)
print (name_list)

