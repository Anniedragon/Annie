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

#lab 16, task 2 In progress
A = []
k = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка ")))
while True :
  for i in range(N-3) :
    for j in range(N-3) :
      if (N <= 2) :
        break
      if (A[i] == A[j]) and (i != j) :
        print(N)
        k += 1
        ni = i
        nj = j
        print(A)
        if k == 2 :
          k = 0
          A.remove(A[ni])
          A.remove(A[nj])
          N = N - 2
          print(A)
        elif k == 0 :
          break
print(A)
