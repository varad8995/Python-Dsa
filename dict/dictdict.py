student_details = {
    "anirudh": {
        "age": 66,
        "gender": "Male",
        "address": "Surat",
        "phone": 100,
        "maths": 88,
        "english": 45,
    },
    "nihar": {
        "phone": 3213421,
        "gender": "Male",
        "address": "Delhi",
        "age": 16,
        "phone": 100,
        "maths": 88,
        "english": 45,
    },
}
for name, details in student_details.items():
    sum = 0
    for k, v in details.items():
        
        if k == "maths" or k == "english":
            sum += v
    
       
    print(f"{name} {sum}  ")    
# print(details["anirudh"]["address"])
# print(details["nihar"]["age"])



for name, details in student_details.items():
    total = details.get("maths",0)+details.get("english",0)
    details["total"] = total


print(student_details)    