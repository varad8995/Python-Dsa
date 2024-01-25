def callSum(n1,n2):
    total = 0
    if n1>n2:
        return "n1 should be smaller"
    
    else:
        i = n1
        while i<=n2:
            total = total+i
            i = i+1
    return total    


print(callSum(12,10))