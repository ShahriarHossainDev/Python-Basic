# Data Types
# Built-in Data Types:
# text: String (str)
# Number: int, float, complex
# Sequence: list, tuple, range
# Mapping: dictionary (dict)
# set : set, frozenset
# boolean: boolean (bool)
# binary : byte, bytearray, memoryview

import random

x_string = "Hello World!"   # String
x_int = 20                  # Int
x_float = 3.1416            # Float
x_complex = 33J             # Complex

x_list = ["apple", 78, "cherry", 232.2] # List
x_tuples = ("apple", "banana", "cherry") # tuple
x_range = range(4)                       # range

x_dict = {"name" : "Shishir", "description" : "iOS Developer"} # dictionary

x_bools = True # Boolean
x_bytes = bytes(5)
x_bytesArray = bytearray(3)
x_memoryview = memoryview(bytes(25))

print (x_memoryview)
print(x_bytes)
print(x_complex)

print(type(x_int))
print(type(x_float))
print(type(x_complex))

y = int(x_float)

print(random.randrange(1,100))
print(random.randint(3,9))
# KU5675-76A
