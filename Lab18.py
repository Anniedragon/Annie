#lab 18, task 1 IN PROGRESS (дико костыльный вариант)
N = int(input("Введите к-во строк в массиве "))
A = []
for i in range(N) :
  A.append([int(j) for j in input().split()])
for i in range(N) :
  for j in range(N) :
    if j == 0 :
      print(A[i][j])
for i in range(N) :
  for j in range(N) :
    if (i == N-1) and (A[i][j] != A[N-1][0]) :
      print(A[i][j])
for i in range(N) :
  for j in range(N) :
    if (j == N-1) and (i != N-1) :
      print(A[N-2-i][j])
for i in range(N) :
  for j in range(N) :
    if (j != 0) and (j != N-1) and (i == 0) :
      print(A[i][N-1-j])
for i in range(N) :
  for j in range(N) :
    if (i != 0) and (i != N-1) and (j == 1) :
      print(A[i][j])
      . . .
      
#lab 18, task 2
N = int(input("Введите к-во строк в массиве "))
A = []
Sum = 0
Proisv = 1
for i in range(N) :
  A.append([int(j) for j in input().split()])
K = int(input("Введите номер строки массива(отсчёт идёт с 0) "))
for i in range(N) :
  for j in range(N) :
    if i == K :
      Sum += A[i][j]
      Proisv *= A[i][j]
print("Сумма элементов строки К равна",Sum)
print("Произведение элементов строки К равно",Proisv)

#lab 18, task 3 IN PROGRESS
N = int(input("Введите к-во строк в массиве "))
A = []
k = 0
k1 = 0
MinPr = 1
Pr = 1
Num = 0
for i in range(N) :
  A.append([int(j) for j in input().split()])
for i in range(N) :
  for j in range(N) :
    if j == 0 :
      MinPr *= A[i][j]
while k1 != 2 : 
  for i in range(N) :
    for j in range(N) :
      if j == k :
        Pr *= A[i][j]
      k += 1
      if Pr < MinPr :
        Minpr = Pr    
    Pr = 1
    k = 0
  k1 += 1
print(Num, "out")
print(MinPr, "out")
