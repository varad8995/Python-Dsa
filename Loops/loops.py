def divisible(num1,num2):
    i = num1
    sum = 0
    while i<=num2:
        if i%3==0 and i%6==0:
            sum = sum+i

        i +=1
    return sum        
       


print(divisible(3,100))