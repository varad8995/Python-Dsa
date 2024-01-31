my_list = [1,2,3,4,5,6,7]

def even(my_list):
    for i in range(len(my_list)):
        if my_list[i]%2==0:
            my_list[i]=0

    



even(my_list)
print(my_list)