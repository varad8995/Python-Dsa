for i in range(6):
    
    for j in range(6-i,1,-1):
        print(" ",end=" ")

    for k in range(0,i+1):
        print("*",end=  " ")

    print()


for i in range(1, 6):
    for j in range(1, 6 - i):
        print(" ", end=" ")
    for k in range(1, i + 1):
        print(i, end=" ")
    print()


for i in range(5, 0, -1):
    for j in range(1, i):
        print(" ", end=" ")
    for k in range(i, 6):
        print(k, end=" ")
    print()