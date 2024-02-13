my_dict = {"name": "Akul", "age": 66, "gender": "Male"}
key=input()




try:
    value = my_dict[key]
    print(value)
except KeyError:
    print(f"{key} key not found")
except:
    print("Unexpected error")