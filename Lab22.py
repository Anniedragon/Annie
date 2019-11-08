#lab 22, task 1
S = str(input("Введите строку, содержащую хотя бы 1 пробел\n "))
for i in range(len(S)) :
  if S[i] == " " :
    S = S[i+1:]
    break
print(S)
