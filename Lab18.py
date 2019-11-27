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
while k != 3 :
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
