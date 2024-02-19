with open("hello.txt", "w") as file:   #if file is there it'll overwrite the content and if file is not there it'll give error
    file.write("python\nis\na\ngood\n")
with open("abc.txt", "a") as file: #if file is there it'll add the content and if file is not there it'll create new file
    file.write("xyz")
