year : int = int(input())



if year % 4 ==0:
    print(f"year {year} is leap year")
elif year % 4 ==0 and year%100==0:
    print(f"year {year} is not a leap year")

elif year % 4 ==0 and year%400==0:
    print(f"year {year} is leap year")
