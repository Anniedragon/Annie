#lab 17, task 1 Способ 1
A = []
B = []
C = []
k = 1
flag = 1
N = int(input("Введите к-во переменных "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
while flag == 1 :
  flag = 0
  for i in range(N-1) :
    if A[i] == A[i+1] :
      k += 1
      print(k)
    else :
      print(A)
      print("k=",k)
      B.append(k)
      C.append(A[i])
      k = 1
      for j in range(k) :
        A.remove(A[i])
        N -= 1
      flag = 1
      break
print(B)
print(C)
