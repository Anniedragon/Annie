#lab 17, task 1
A = []
B = []
C = []
k = 1
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
A.append(0)
N += 1
for i in range(N-1) :
  if A[i] == A[i+1] :
    k += 1
  else :
    B.append(A[i])
    C.append(k)
    k = 1
print(B)
print(C)

