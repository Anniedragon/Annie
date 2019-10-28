#lab 20, task 1
B = "B"
D = "D"
print("Дан символ С")
print(B,"- предыдущий символ")
print(D,"- следующий символ")

#lab 20, task 2
S = str(input("Введите строку "))
S1 = ""
for i in range(len(S)-1) :
  if (S[i] == " ") and (S[i-1] != " ") and (S[i+1] != " ") and (i != 0) :
    S1 += S[i-1]
    S1 += S[i+1]
  elif i == 0 :
    if S[i+1] == " " :
      S1 += S[i]
    elif S[0] == " " :
      S1 += S[i+1]
print(S1)

#lab 20, task 3
S = str(input("Введите строку "))
k = 0
for i in range(len(S)) :
  B = S[i].isupper()
  if B == True :
    k += 1
print("Количество прописных букв в строке S равно",k)

#lab 20, task 4 In progress
S = "qwerrttyuyii"
S.replace("q", "qq")
print(S)
'''
S = str(input("Введите строку "))
C = str(input("Введите символ "))
C2 = C*2
print(C2)
k = 0
for i in range(len(S)) :
  if S[i] == C :
    S[i].replace(C, C2)
print(S)
''' 
