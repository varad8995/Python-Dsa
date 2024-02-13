my_list1 = [1,2,3,4]

my_list2 = [0,1,2,5,6,7]
print(len(my_list2))
my_list3 = []
i = 0
j = 0
while i<len(my_list1) or j < len(my_list2):
    if i==len(my_list1) and j<=len(my_list2):
        my_list3.append(my_list2[j])
        j+=1
    elif j==len(my_list2) and i<=len(my_list1):
        my_list3.append(my_list1[i])
        i+=1    
    elif my_list1[i]<my_list2[j]:
        my_list3.append(my_list1[i])
        i+=1
    elif my_list1[i]==my_list2[j]:
        my_list3.append(my_list1[i])    
        my_list3.append(my_list2[j])  
        i+=1
        j+=1
    else:
        my_list3.append(my_list2[j])
        j+=1    


print(my_list3)        