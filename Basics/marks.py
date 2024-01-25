maths = int(input())
english = int(input())
science = int(input())            #alt shiftdown if you want to copy
physics = int(input())
hindi = int(input())

total = maths+english+science+physics+hindi
percentage = total / 5
# print(f{percentage:.2f})
result = round(percentage,2)
print(result)