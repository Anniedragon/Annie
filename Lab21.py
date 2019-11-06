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

#lab 21, task 3
S = str(input("Введите строку из нескольких слов "))
S1 = ""
S = S.upper()
for i in range(len(S)) :
  if (S[i] == S[0]) and (i == 0):
    S1 += S[i]
  elif (S[i] == S[0]) and (i != 0) :
    S1 += "."
  else :
    S1 += S[i] 
print(S1)

#lab 21, task 4
S = str(input("Введите строку на русском языке "))
Sgl = "уеыаоэяию"
k = 0
for i in S :
  for j in Sgl:
    if i == j :
      k += 1
print("Количество гласных в строке равно",k)

#lab 21, task 5
S = str(input("Введите строку вида C:/python/prog123.py\n "))
k = 0
k1 = 0
for i in range(len(S)) :
  if S[i] == "/" :
    k += 1
for i in range(len(S)-1) :
  if S[i] == "/" :
    k1 += 1
  if k1 == k :
    n1 = i
    break
for i in range(len(S)) :
  if S[i] == "." :
    n2 = i
print(S[n1+1:n2])

#lab 21, task 7
S = str(input("Введите строку на русском языке "))
S1 = ""
k = 0
for i in range(len(S)) :
  if (i % 2 == 0) or (i == 0) :
    S1 += S[i] 
for i in range(len(S)) :
  if (len(S)-i) % 2 == 0 :
    S1 += S[i]
print(S1)
