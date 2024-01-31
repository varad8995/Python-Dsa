my_list = [i for i in range(1,20)]


end = int(input())


new_list = my_list[-end:]
new_list.reverse()
print(new_list)
