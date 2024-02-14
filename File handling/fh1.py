f = open("hello.txt", "r")
r = f.read()
print(r)
f.close()

# File handling
# Read, Write, Delete, Create, rename, move, copy
"""
3 modes to open a file
1. Read (r)
2. Write (w)
3. Append (a)
"""

r = f.read(6)
# print(r)
# x = f.read(6)
# print(x)
# x = f.read(10)
# print(x)
x = f.read()
print(x)
print("---------")
x = f.read()
print(x)
f.close()
print("---------")
f = open("hello.txt", "r")
x = f.read()
print(x)
f.close()