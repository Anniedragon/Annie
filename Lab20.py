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

