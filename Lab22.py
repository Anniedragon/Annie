#lab 22, task 1
S = str(input("Введите строку, содержащую хотя бы 1 пробел\n "))
for i in range(len(S)) :
  if S[i] == " " :
    S = S[i+1:]
    break
print(S)

#lab 22, task 2
S = "*"
K = int(input("Введите к-во * в строке "))
N = int(input("Введите к-во строк "))
for i in range(N) :
  print(S * K, end = "\n")

#lab 22, task 3
S = " " + str(input("Введите строку "))
S = S.rstrip()
S1 = str(input("Введите другую строку "))
S = S.replace(" ", S1)
print(S)

#lab 22, task 4
S = str(input("Введите строку "))
S1 = ""
k = 0
for i in range(len(S)) :
  if S[i] != " " :
    S1 += S[i]
  elif (S[i] == " ") and (S[i+1] != " ") :
    S1 += S[i]
print(S1)
