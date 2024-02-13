my_string = input("Enter a String= ")


def funQ1(s: str):
    l = ""
    for i in s:
        if i.islower() == True:
            i = i.upper()
            l = l + i
        elif i.isupper() == True:
            i = i.lower()
            l = l + i
    print(l)


funQ1(my_string)


