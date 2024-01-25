salary : int = int(input())


if salary>50000:
    dicounted_price = salary*(20/100)
    updated_Salary = salary+dicounted_price
    print(f"your updated salary is {updated_Salary}") 
elif salary>20000 and salary<=50000:
    dicounted_price = salary*(15/100)
    updated_Salary = salary+dicounted_price
    print(f"your updated salary is {updated_Salary}")  
elif salary>10000 and salary<=20000:
    dicounted_price = salary*(10/100)
    updated_Salary = salary+dicounted_price
    print(f"your updated salary is {updated_Salary}")  
  
else:
    dicounted_price = salary*(5/100)
    updated_Salary = salary+dicounted_price
    print(f"your updated salary is {updated_Salary}")   