#lab 21, task 1
S = str(input("Введите строку "))
k = 0
S = S.lstrip(" ")
S += " "
for i in range(len(S)) :
  if S[i] == " " :
    k += 1
print("Количество слов в строке равно",k)

#lab 21, task 2
S = str(input("Введите строку из нескольких слов "))
S += " "
A = []
k = 0
for i in range(len(S)) :
  if S[i] != " " :
    k += 1
  else :
    A.append(k)
    k = 0
Min = A[0]
for i in range(len(A)) :
  if (A[i] < Min) and (A[i] != 0) :
    Min = A[i]
print("Длина самого короткого слова в строке равна",Min)
