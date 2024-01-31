my_list = [i for i in range(1,20)]

start = my_list[0]
end = my_list[-1]

my_list[0] = end
my_list[-1]=start

print(my_list)
