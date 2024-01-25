# Default Parameters / Required Parameter
def marks(physics, chemistry, hindi, english=0, science=0):
    total = physics + chemistry + english + science + hindi
    per = total / 500 * 100
    print(f"Your total marks = {total}")
    print(f"Your percentage scored = {per:.2f}")

# marks(56, 11, 89, 78, 99)
# marks(english=99, hindi=45, chemistry=11, science=34, physics=89)
marks(50, 10, hindi=90)





def greet(num):
    print(num)


x = greet(1)
print(greet(1))    