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
