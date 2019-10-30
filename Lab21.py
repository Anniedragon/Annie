#lab 21, task 1
S = str(input("Введите строку "))
k = 0
S = S.lstrip(" ")
S += " "
for i in range(len(S)) :
  if S[i] == " " :
    k += 1
print("Количество слов в строке равно",k)
