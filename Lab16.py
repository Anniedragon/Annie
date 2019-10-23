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

#lab 16, task 2
A = []
flag = 1
r = 6
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
while flag == 1 :
  flag = 0
  for i in range(N) :
    if A.count(A[i]) % 2 == 0 :
      for j in range(A.count(A[i])) :
        A.remove(A[i])
        N -= 1
      flag = 1
      break
print(A)
  
#lab 16, task 3
A = []
A1 = []
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
A.append(0)
A.append(0)
Min = A[0]
Max = A[0]
for i in range(N) :
  if A[i] < Min :
    Min = A[i]
  if A[i] > Max :
    Max = A[i]
for i in range(N) :
  if A[i] == Min :
    A1.append(0)
    A1.append(A[i])
  elif A[i] == Max :
    A1.append(A[i])
    A1.append(0)
  else :
    A1.append(A[i])
print(A1)

#lab 16, task 4
import random
A = []
A1 = []
k = 0
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(random.randint(-100, 100))
for i in range(N) :
  if A[i] < 0 :
    k += 1
for i in range(k) :
  A.append(0)
for i in range(N) :
  if A[i] < 0 :
    A1.append(A[i])
    A1.append(0)
  else :
    A1.append(A[i])
print(A1)

#lab 16, task 5
import random
A = []
A1 = []
k = 0
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(random.randint(-100, 100))
for i in range(N) :
  if A[i] > 0 :
    k += 1
for i in range(k) :
  A.append(0)
for i in range(N) :
  if A[i] > 0 :
    A1.append(0)
    A1.append(A[i])
  else :
    A1.append(A[i])
print(A1)
