#lab 18, task 1
N = int(input("Введите к-во строк в массиве "))
A = []
for i in range(N) :
  A.append([int(j) for j in input().split()])
for k in range(N) :
  for i in range(k,N-k) :
    print(A[i][k])
    x = i
  for j in range(k+1,N-k) :
    print(A[x][j])
    y = j
  for i in range(N-k-2,k-1,-1) :
    print(A[i][y])
    x = i
  for j in range(N-k-2,k,-1) :
    print(A[x][j])
      
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

#lab 18, task 3
N = int(input("Введите к-во строк в массиве "))
A = []
Num = 0
k = 0
MinPr = 1
Pr = 1
for i in range(N) :
  A.append([int(j) for j in input().split()])
for i in range(N) :
  for j in range(N) :
    if j == 0 :
      MinPr *= A[i][j]
while k != N :
  for i in range(N) :
    for j in range(N) :
      if j == k :
        Pr *= A[i][j]
  if Pr < MinPr :
    MinPr = Pr
    Num = k
  Pr = 1
  k += 1
print("Наименьшее произведение",MinPr,"\n","Номер столбца",Num)

#lab 18, task 4
N = int(input("Введите к-во строк в массиве "))
A = []
Count = []
k = 0
k1 = 0
SrAr = 0
Sum = 0
for i in range(N) :
  A.append([int(j) for j in input().split()])
while k != N :
  for i in range(N) :
    for j in range(N) :
      if j == k :
        Sum += A[i][j]
  SrAr = Sum / N
  for i in range(N) :
    for j in range(N) :
      if j == k :
        if A[i][j] > SrAr :
          k1 += 1
  Count.append(k1)
  k1 = 0
  Sum = 0
  SrAr = 0
  k += 1
print("\n")
for i in Count :
  print(i, end = " ")

#lab 18, task 5
N = int(input("Введите к-во строк в массиве "))
A = []
k = 0
k1 = 0
for i in range(N) :
  A.append([int(j) for j in input().split()])
while k != N :
  for i in range(N) :
    for j in range(N) :
      if j == k :
        if A[i][j] % 2 != 0 :
          k1 += 1
  if k1 == N :
    print(k)
    break
  else :
    k1 = 0
    k += 1
if k1 == 0 :
  print("0 - таких столбцов нет")
