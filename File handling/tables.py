with open("tables.txt","a") as f:
    number:int = int(input())

    for i in range(1,11):
        table = f"{number} * {i} "
        table2 = (number*i)
        
        f.write(table)
      
        f.write(str(table2))