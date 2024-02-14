f = open("hello.txt")
r = f.readline(2)


x = f.readline(2)
print(r)
print(x)


f = open("hello.txt", "r")
# x = f.readline()
# print(x)
# x = f.readline()
# print(x)
x = f.readlines()
print(x)
f.close()

f = open("hello.txt", "r")
"""# Print how many lines are there
x = f.readlines()
print(len(x))"""
"""
Print how many words are there
"""
lines = f.readlines()
count = 0
for line in lines:
    words = line.strip().split()
    count = count + len(words)
print(count)
f.close()