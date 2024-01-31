my_list = [i**2 if i%2!=0 else i**3 for i in range(1,11)]
print(my_list)


my_list2 = [0 if i%2 !=0 else 1 for i in range(1,11)]
print(my_list2)

my_list2 = [i for i in range(1,11) if i%2==0]
print(my_list2)


# my_list2 = [i**2 for i in range(1,21) if i*2 !=0 i**3  ]
# print(my_list2)

original_list = [1,2,3,4,5,7.8,1.2,5.0]
int_list = [i for i in original_list if type(i)==int]
float_list = [i for i in original_list if type(i)==float]
print(int_list)
print(float_list)


def prime_numbers(n):
    if n == 1 or n==2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
        
    return True




prime_numbers = [i for i in range(1,50) if prime_numbers(i) == True]
print(prime_numbers)





