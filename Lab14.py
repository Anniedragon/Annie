#lab 14, task 1
A = []
Sum = 0
N = int(input("Введите к-во элементов списка "))
print("Должно выполняться неравенство 1 <= K <= L <= N")
K = int(input("Введите число K, согласно условию выше "))
L = int(input("Введите число L, согласно условию выше "))
for i in range(1, N+1) :
  A.append(int(input("Введите элемент списка ")))
for i in range(K, L+1) :
  Sum += A[i]
print("Среднее арифметическое элементов с номерами от K до L:",Sum / ((L+1)-K+1))

#lab 14, task 2 In progress
A = []
N = int(input("Введите к-во элементов списка "))
k = 0
flag = 0
for i in range(1, N+1) :
  A.append(int(input("Введите элемент списка (одинаковых чисел быть не должно) ")))
while True :
  k = 0
  for i in A :
    for j in A :
      if i == j :
        k += 1
  if k > N :
    print("Условие не выполнено!")
    A.clear()
    for i in range(1, N+1) :
      A.append(int(input("Введите элемент списка (одинаковых чисел быть не должно) ")))  
  else :
    break 
for i in range(N-2) :
  if (A[i+1] - A[i]) == (A[i+2] - A[i+1]) :
    flag = 1
print(flag)

#lab 14, task 3
A = []
N = int(input("Введите к-во элементов массива "))
for i in range(N) :
  A.append(int(input("Введите элемент списка ")))
min = A[0]
for i in range(N) :
  if i % 2 == 0 :
    if A[i] < min :
      min = A[i]
print(min)

#lab 14, task 4
A = []
max = 0
N = int(input("Введите к-во элементов массива "))
for i in range(N) :
  A.append(int(input("Введите элемент списка ")))
for i in range(N-1) :
  if (A[i] > A[i-1]) and (A[i] > A[i+1]) :
    max = A[i]
print(max)

#lab 14, task 5
A = []
k = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка (должно быть строго 2 одинаковых элемента) ")))
while True :
  for i in A :
    for j in A :
      if i == j :
        k += 1
  if k != N+2 :
    k = 0
    print("Условие не выполнено!")
    A.clear()
    for i in range(N) :
      A.append(int(input("Введите элемент списка (должно быть строго 2 одинаковых элемента) ")))
  else :
    break
for i in range(N) :
  for j in range(N) :
    if (A[i] == A[j]) and (i != j) :
      print(i, j)
      break
