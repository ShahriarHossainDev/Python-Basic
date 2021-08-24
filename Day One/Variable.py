# Assigning Values to Variable

counters = 10
miles = 12.23
name = "Shishir"

# Multiple
a = b = c = d = 100

e = f = g = h = 4, 6, 'Ail', "Atik"

# Standard Data Types:
# 1. Number
# 2. String
# 3. List
# 4. Tuples
# 5. Dictionary

# Cstings

x = int(34)
y = float(34)
z = str(34)

# Get the Type
print(type(miles))

# Single or Double Quotes

var1 = "Hello"
var2 = 'Hello'

print(var1)
print(var2)

# case sensitive

m = 7890
M = "Ok"

# Variable names
# Illegal

_my_add = "Hello"

My_Car = "Tata" # Snake case
myCar = "Tatas" # Camel case
MyCar = "Tatess" # Pascal case

# Unpack a collection
fruits = ["apple", "banana", "cherry"]
f1,f2,f3=fruits
print(f1)
print(f2)
print(f3)

# Optput Variables
print("I love " + f1)
print(f1 + " " +f2)

# globel Keyword

def myFun():
    global xs
    xs = "Ok to go"

myFun()

print(xs)