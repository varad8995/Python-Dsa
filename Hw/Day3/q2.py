class_held : int = int(input())
class_attended : int = int(input())


attendance = ((class_attended / class_held)*100)
attendance =  round(attendance,2)

if attendance>=75:
    print(f"Your are  allowed to sit in the class as your attendace is {attendance}% which is greater than 75%")

else:
    print(f"Your are not allowed to sit in the class as your attendace is {attendance}% which is less than 75%")