def calculatefactorssum(num1:int,num2:int):
    i=1
    total = 0
    while i<=num1:
        if i%num2==0:
            total = total+i
        i+=1
    return total

print(calculatefactorssum(40,7))

