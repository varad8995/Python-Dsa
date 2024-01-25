# num : int = int(input())
# i = 1
# while i<=num:
#     print(i)
#     i+=1



def printusingwhile(num1,num2):
    if num1>num2:
        
        j = num2
        while j<=num1:
            print(j)
            j=j+1
    else:
        i= num1
        while i<=num2:
            print(i)
            i=i+1            


printusingwhile(15,11)            



def printusingwhile1(num1,num2):
    start = num1 if num1<num2 else num2
    end = num2 if num1<num2 else num1

    while start<=end:
        print(start) 
        start = start+1


printusingwhile1(15,11)     