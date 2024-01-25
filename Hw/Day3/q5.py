final_amount : int = int(input())
dicounted_price = 1

if final_amount>=50000:
    dicounted_price = final_amount*(70/100)
    print(f"your discounted price is {dicounted_price}") 
elif final_amount>=40000 and final_amount<=49999:
    dicounted_price = final_amount*(75/100)
    print(f"your discounted price is f{dicounted_price}")  
elif final_amount>=30000 and final_amount<=39999:
    dicounted_price = final_amount*(80/100)
    print(f"your discounted price is f{dicounted_price}")  
elif final_amount>=10000 and final_amount<=29999:
    dicounted_price = final_amount*(90/100)
    print(f"your discounted price is f{dicounted_price}")  
else:
    dicounted_price = final_amount
    print(f"your discounted price is f{dicounted_price}")      