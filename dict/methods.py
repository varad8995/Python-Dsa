marks = {
    "physics": 43,
    "chemistry": 91,
    "maths": 84,
}
# print(marks["physicss"])
# print(marks.get("physicss"))
user_key = input("Enter a key name = ")
result = marks.get(user_key)
if result:
    print(result)
else:
    print("Key not found")

# if result != None:
#     print(result)
# else:
#     print("Key not found")
# membership in, not in
# if user_key in marks:
#     print(marks[user_key])
# else:
#     print("Key does not exists")
# if user_key in marks.keys():
#     print(marks[user_key])
# else:
#     print("Key does not exists")
    

marks = {
    "physics": 43,
    "chemistry": 91,
    "maths": 84,
    "english": 0,
    "computer": 44,
}
# x = marks.pop("physicss")
# print(x)
# print(marks)
# To update multiple values
# marks["physics"] = 100
# marks["chemistry"] = 100
# marks["maths"] = 100
marks.update({"physics": 100, "chemistry": 100, "maths": 100, "xyz": 99})
print(marks)    

a = list(map(int, 
    input("\nEnter the numbers : ").strip().split()))[:n]

int(input())


x, y, z = map(int, input().split())
print(x)
print(y)
print(z)
print(x + y + z)