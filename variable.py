name = "Dipesh"
age = 24

print("My name is " + name + " and my age is " + str(age))
print(type(name))

_myVar = True

x, y = 20, 30

a = b = c = 10

fruits = ["apple", "banana", "cherry"]
q, w, e = fruits

print(_myVar, x, y, a, b, c, q, w, e)


def pyFunc():
    global x
    x = "python"
    print(x)


pyFunc()
print(x)

random = "banana"

for i in random:
    print(i)

print(i)
print(type(len(random)))

txt = "The best things in life are free!"
print("free" in txt)
# slice string
print(txt[2:5])

# replace string
txt = "The best things in life are free!"
print(txt.replace("free", "awesome"))

# upper case
txt = "The best things in life are free!"
print(txt.upper())

# lower case
txt = "The best things in life are free!"
print(txt.lower())

# capitalize
txt = "The best things in life are free!"
print(txt.capitalize())

# split string
txt = "The, best, things ,in ,life, are, free!"
print(txt.split(","))

# join string
txt = ["The", "best", "things", "in", "life", "are", "free!"]
print(" ".join(txt))

# strip string
txt = "     The best things in life are free!     "
print(txt.strip())

# length of string
txt = "The best things in life are free!"
print(len(txt))

# F-Strings

name = f"Dipesh {x}"
print(name)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

b = "Hello, World!"
print(b[2:5])
print(b[2:])
print(b[:5])


# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh  Hexadecimal value

# Python String Methods

# capitalize()
my_string = "Hello, World!"

print(my_string.casefold())  # Output: "hello, world!" (converts to lowercase)
print(my_string.capitalize())  # Output: "Hello, world!" (capitalizes the first letter)
print(my_string.center(2, "-"))  # Output:  Hello, World!"
print(my_string.count("l"))  # Output: 3
print(my_string.encode("utf-8"))  # Output: b'Hello, World!'
print(my_string.find("World"))  # Output: 7
print(my_string.isidentifier())  # Output: False
print(my_string.partition(","))  # Output: ("Hello", ",", " World!")
print(my_string.split(","))  # Output: ["Hello", " World!"]
print(my_string.strip())  # Output: "Hello, World!"
print(my_string.title())  # Output: "Hello, World!"
print(my_string.translate(str.maketrans("l", "x")))  # Output: "Hexxo, Worxd!"
# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))
print(txt.center(20, "-"))

test = "SAM"
print(
    test.center(5, "-")
)  # Provides padding of the second argument to the left and right. First it provides in the right and then left in case of odd length.
print(len(test))


print(txt.encode())

print(my_string.find("llo"))
print("This is a {teststring}".format(teststring="test", testing="Test"))

# Operators

# + - * / % ** //
# = += -= *= /= %= **= //= (&= |= ^= >>= <<= >>= >>= :=)
# == != > < >= <=
# and | or | not | is | is not
# in | not in

# List is like array in JS

thisList = ["apple", "banana", "cherry"]
a, b, c = thisList
print(a, b, c)

# List - ordered - Changeable - Allows Duplicates
# Tuple - ordered - Unchangeable - Allows Duplicates
# Set - unordered - unchangeable - No Duplicates
# Dictionary - ordered - changeable - No Duplicates


# Negative Indexing in Python

thisList = thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]


print(thisList[-1])  # Prints the last element

print(thisList[:4])  # start to 3rd index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  # from 2nd(included) element to the end

print(thisList[-4:-1])  # from 4th(included) element to second last element

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]  # replace or adds elements
print(thislist)

thisList.insert(2, "Pumpkin")  # inserts at index 2
thisList.append("Pumpkin")  # adds at the end

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)  # Merge two Lists/tuple/Dictionary/Sets
print(thislist)

thisList = ["apple", "banana", "cherry", "banana"]
thisList.remove("banana")  # remove every occurance of banana

thisList.clear()  # clear the list
del thisList  # delete the list

thisList = ["apple", "banana", "cherry"]

# Loopig over the list
for x in thisList:
    print(x)

# Looping with index
for x in range(len(thisList)):
    print(x)

i = 0
while i < len(thisList):
    print(thisList[i])
    i += 1

[print(x) for x in thislist]  # shorthand


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]  # shorthand
# newlist = [expression for item in iterable if condition == True] syntax
print(newlist)

thisList.sort()  # sort alphanumerically
thisList.sort(reverse=True)  # revere sort


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# By default sort is case sensitive  and Upper case are sorted before lower case

thisList.sort(key=str.lower)  # key = function not function call

# making copies of lists
thisList = ["apple", "banana", "cherry"]
mylist = thisList.copy()
mylist = list(thisList)
mylist = thisList[:]

# join two lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
# list1.extend(list2) -> combines list in list1

print(list3)
# trying using shorthand
list4 = ["a", "b", "c"]
list5 = [1, 2, 3]
[list4.append(x) for x in list5]

print(list4)


# Tuple


thistuple = ("apple", "banana", "cherry", "apple", "cherry")

# create a tuple
thisTuple = tuple(("a", True, 3))
# All the same way to access the variables and Iteration
# You can't update a tuple, you can just convert it to list and then update it
# Also s = ("apple") -> this is not a tuple but a string
# s = ("apple",) -> this is a tuple. Notice the comma at the end
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# Unpack a tuple

fruits = ("apple", "banana", "cherry")

(fruit1, fruit2, fruit3) = fruits
print(fruit1, fruit2, fruit3)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# Use * to assign red all the rest elements as a list
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

# Methods of tuple

# count() -> returns the number of times the value appears
# index() -> returns the index of the first element with the specified value
