def pattern2(n):
    i = 1
    sum= 1
    while i<=n:
        if i==1:
            print(sum)
            i+=1
        elif i%2==0:
            sum = sum+2
            print(sum)
            i+=1
        else:
            sum = sum+3
            print(sum)   
            i+=1     
        


        


pattern2(5)            