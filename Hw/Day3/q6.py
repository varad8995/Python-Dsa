num1 : int = int(input())
num2  :int = int(input())


if num1==num2:
    num2  : int = int(input("Enter diff number"))

num3 : int = int(input())
if num3 == num1 or num3 == num2:
    num3 : int = int(input("Enter diff number"))

num4 : int = int(input())
if num4 == num1 or num4 == num2 or num4==num3:
    num4 : int = int(input("Enter diff number"))     

print(num1)
print(num2)
print(num3)
print(num4)
if num1<num2 and num1<num3 and num1<num4:
    print(f"{num1} is smallest")    
elif num2<num1 and num2<num3 and num2<num4:
    print(f"{num2} is smallest") 
elif num3<num2 and num3<num1 and num3<num4:
    print(f"{num3} is smallest") 

else:
    print(f"{num4} is smallest")        