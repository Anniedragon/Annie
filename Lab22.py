#lab 22, task 1
#C:\Users\agush\Desktop\Мосполитех. Программирование\example.txt
print("Enter the full name(path) of the file ")
path = str(input())
element = ""
k = 0
flag = 0
textfile = []
with open(path ,"r") as file :
    element = file.read()
for i in range(len(element)) :
    if (element[i] == " ") and (flag == 0) :
        k = i
        flag = 1
    textfile.append(element[i])
del textfile[0:k+1]
with open(path, "w") as file :
    file.write("".join(textfile))
with open(path, "r") as file :
    print(file.read())
