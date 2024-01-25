for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print(i,end=" ")   
    print()    

for i in range(1,5):
    for j in range(1,i+1):
        print(" ",end=" ")
    for k in range(0,9-2*i):
        print(5-i,end=" ")   
    print()      