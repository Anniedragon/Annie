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
