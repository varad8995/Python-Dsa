def printPattern(num):
    if num>0:
        i=-(num)
        while i<=num:
            print(i , end=" ")
            i+=1
    else:
        i = (num)
        while i<= (-(num)):
            print(i , end=" ")
            i+=1

printPattern(6)                    