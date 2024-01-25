def pattern(num: int):
    i: int = 1
    num1: int = 1
    while i <= num:
        print(num1, end=" ")
        num1 = (10**i) + 1
        i = i + 1

pattern(10)

