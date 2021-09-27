var1 = 'Hello'
var2 = "Hello"

var3 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

var5 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
# 'hello' is the same as "hello"

print(var1 + " " + var2)
print(var3)
print(var5)

# Strings are Arrays
var4 = 'Hello world'

# Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

print(var4[6])

# String Length
# To get the length of a string, use the len() function.

print(len(var4))
# Modify Strings
print(var4.upper())
print(var4.lower())
print(type(var4))

# Check String

var6 = "The best things in life are free!"

print("life" in var6)

# Check if NOT
print("expensive" not in var6)


print(var6[4:8])
print(var6[:14])
print(var6[4:])

var7 = "       I am shishir "
print(var7.strip())

print(var7.replace("am", "was"))

print(var7.split())

# String Format
age = 22
var8 = "My name is shishir. I am {}"

print(var8.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
var9 = "My name is shishir. I am \(age)"
print("life is \n hell")
print("life is \"super\" hell")

var9 = "life Is Hell"
print(var9.capitalize())
