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

#lab 22, task 2
#C:\Users\agush\Desktop\Мосполитех. Программирование\example.txt
print("Enter the full name(path) of the file ")
path = str(input())
N = int(input("Введите к-во строк "))
K = int(input("Введите к-во * в строке "))
textfile = []
element = ""
line = ""
for i in range(K) :
    line += "*"
file = open(path, "w")
for i in range(N) :
    file.write(line + "\n")
file.close()
with open(path, "r") as file :
    print(file.read())
    
#lab 22, task 3
#C:\Users\agush\Desktop\Мосполитех. Программирование\example.txt
#C:\Users\agush\Desktop\Мосполитех. Программирование\example2.txt
print("Enter the full name(path) of two files ")
element = "" 
path1 = str(input())
path2 = str(input())
file1 = open(path1, "a")
file2 = open(path2, "r")
element = file2.read()
file1.write(element)
file1.close()
file2.close()
with open(path1, "r") as file1 :
    print(file1.read())

#lab 22, task 4
#C:\Users\agush\Desktop\Мосполитех. Программирование\test.txt
print("Enter the full name of the file ")
path = str(input())
S = ""
S1 = ""
k = 0
with open(path,'r') as file:
    S = file.read()
for i in range(len(S)) :
    if S[i] != " " :
        S1 += S[i]
        k = 0
    elif S[i] == " " :
        k += 1 
        if k == 1 :
            S1 += S[i]
with open(path, "w") as file :
    file.write(S1)
with open(path, "r") as file :
    print(file.read())
