def calSum(n1,n2):
    total = 0
    if n1>n2:
        return "n1 should be smaller"
    else:
        i = n1
        while i<=n2:
            if i%5==0:
                total = total+i
            i+=1
    return total            


print(calSum(1,10))

