my_list = [1,2,3,4,5,6,'varad']

print(my_list)
print(id(my_list))

a = my_list

my_list[2] = 34
print(id(a))
#copying add not values
print(my_list)
print(a)


b= my_list.copy()  #by value creating new list  shallow copy
my_list[3]=55
b[0] = 44
print(b)
print(my_list)
print(id(b))

import copy

c  = [1,2,43,45,[45,66]]
d = copy.deepcopy(c)

c[4][0] = 44
print(id(c))
print(id(d))
print(c)
print(d)