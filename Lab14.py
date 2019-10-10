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
for i in range(1, N+1) :
  A.append(int(input("Введите элемент списка (одинаковых чисел быть не должно) ")))
while True :
  for i in A :
    for j in A :
      if i == j :
        k += 1
  if k > N :
    print("Условие не выполнено ")
    for i in range(1, N+1) :
      A.append(int(input("Введите элемент списка (одинаковых чисел быть не должно) ")))
  else :
    break   
print(A)
