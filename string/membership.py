#in not in

# Membership Operator
# in / not in (iterable)
char = "a"
if char not in "aeiou":
    print("Con")
else:
    print("No")

string = "anirudh   kh76%$"
x = list(string)
print(x)
x[0] = "Z"
print(x)
print(type(x))
r = "".join(i for i in x[::-1])
# r = "".join(i for i in x)
print(r)
print(type(r))