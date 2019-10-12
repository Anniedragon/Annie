#lab 15, task 1 
A = []
B = []
temp = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
for i in range(N) :
  B.append(int(input("Введите элемент списка В ")))
for i in range(N) :
  temp = A[i]
  A[i] = B[i]
  B[i] = temp
print(A)
print(B)

#lab 15, task 2
A = []
B = []
Sum = 0
k = 1
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
for i in range(N) :
  for k in range(1, i+1) :
    Sum += A[k]
  B.append(Sum / (k))
print(B)

#lab 15, task 3
A = []
k = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
for i in A :
  if i % 2 != 0 :
    k = i
for i in range(N) :
  if A[i] % 2 != 0 :
    A[i] += k
print(A)

#lab 15, task 4
A = []
n1 = 0
n2 = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
Min = A[0]
Max = 0
for i in range(N) :
  if A[i] < Min :
    Min = A[i]
    n1 = i
  elif A[i] > Max :
    Max = A[i]
    n2 = i
for i in range(N) :
  if n1 < n2 :
    if (i > n1) and (i < n2) :
      A[i] = 0
  else :
    if (i > n2) and (i < n1) :
      A[i] = 0
print(A)

#lab 15, task 5
A = []
k = 0
temp = 0
N = int(input("Введите к-во элементов списка "))
print("Все элементы списка, кроме 1ого должны быть упорядочены по возрастанию")
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
while True :
  for i in range(N-1) :
    if A[i] < A[i+1] :
      k += 1
  if k != N-2 :
    k = 0
    A.clear()
    print("Условие не выполнено!")
    print("Все элементы списка, кроме 1ого должны быть упорядочены по возрастанию")
    for i in range(N) :
      A.append(int(input("Введите элемент списка А ")))
  else :
    break
for i in range(N-1) :
  if A[i] > A[i+1] :
    temp = A[i+1]
    A[i+1] = A[i]
    A[i] = temp
print(A)
