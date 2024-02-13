my_list = [1,1]
cons = []

for i in range(len(my_list)-1):
    if i == (len(my_list)-2):
        break
    elif my_list[i+1] == my_list[i] and my_list[i+2]==my_list[i]:
        cons.append(my_list[i])
if len(cons)==0:
    print( "No")
else:
    print(cons)

 



