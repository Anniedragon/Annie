#lab 19, task 1
from random import randint
N = int(input("Введите количество строк "))
M = int(input("Введите к-во элементов в строке "))
A = []
k = 0
temp = 0
NumMn = 0
NumMx = 0
for i in range(N) :
  A.append([])
  for j in range(M) :
    A[i].append(randint(-10, 10))
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])
print("\n")
Min = 100
Max = -100
for i in range(N) :
  for j in range(M) :
    if i == k :
      if A[i][j] < Min :
        Min = A[i][j]
        NumMn = j
      elif A[i][j] > Max :
        Max = A[i][j]
        NumMx = j
  temp = A[k][NumMn]
  A[k][NumMn] = A[k][NumMx]
  A[k][NumMx] = temp 
  Min = 100
  Max = -100
  k += 1
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])
