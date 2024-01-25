for i in range(6):
    
    for j in range(6-i,1,-1):
        print(" ",end=" ")

    for k in range(0,i*2-1):
        print("*",end=  " ")

   
    print()

for i in range(5 - 1, 0, -1):
        # Print spaces
        for j in range(5 - i):
            print(" ", end=" ")
        
        # Print asterisks for the second half
        for j in range(2 * i - 1):
            print("*", end=" ")
        print()





for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(0, 2 * i - 1):
        print("*", end=" ")
    print()

for i in range(1,5):
    for j in range(1,i+1):
        print(" ",end=' ')
    for k in range(1,(9-(2*i))):
        print("*",end = " ")    
    print()        