#lab 16, task 1
A = []
flag = 1
k = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка ")))
for i in range(N-1) :
  if A[i] == A[i+1] :
    k += 1
    flag = 0
for i in range(N-k) :
  if A[i] == A[i+1] :
    A.remove(A[i+1])
if flag == 1 :
  print("В списке нет одинаковых элементов")
else :
  print(A)
