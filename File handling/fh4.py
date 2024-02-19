"""good morning hello
ok bye
done
have a great day"""

f = open("hello.txt", "r")
lines = f.readlines()
for line in lines:
    words_list = line.strip().split()
    reverse_list = words_list[::-1]
    result = " ".join(reverse_list)
    print(result)

f.close()


        
        # print(i)
        
    # print(words)
    # count = count + len(words)

