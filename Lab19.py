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

#lab 19, task 2
from random import randint
N = int(input("Введите количество строк "))
M = int(input("Введите к-во элементов в строке "))
Min = 100
Max = -100
NumMn = 0
NumMx = 0
temp = 0
A = []
for i in range(N) :
  A.append([])
  for j in range(M) :
    A[i].append(randint(1, 10))
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])
print("\n")
for i in range(N) :
  for j in range(M) :
    if A[i][j] < Min :
      Min = A[i][j]
      NumMn = j
    elif A[i][j] > Max :
      Max = A[i][j]
      NumMx = j
for i in range(N) :
  for j in range(M) :
    temp = A[i][NumMn]
    A[i][NumMn] = A[i][NumMx]
    A[i][NumMx] = temp
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])

#lab 19, task 3
from random import randint
N = int(input("Введите к-во строк, чётное "))
M = int(input("Введите к-во элементов в строке, чётное "))
temp = 0
A = []
for i in range(N) :
  A.append([])
  for j in range(M) :
    A[i].append(randint(1, 10))
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])
print("\n")
for i in range(N//2) :
  for j in range(M//2) :
    temp = A[i][j]
    A[i][j] = A[i + N//2][j + M//2]
    A[i + N//2][j + M//2] = temp
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])

#lab 19, task 4 IN PROGRESS
from random import randint
N = int(input("Введите к-во строк, чётное "))
M = int(input("Введите к-во элементов в строке, чётное "))
temp = 0
gran = 0
nte = 0
Min = 0
A = []
for i in range(N) :
  A.append([])
  for j in range(M) :
    A[i].append(randint(1, 10))
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])
print("\n") 
for i in range(N) :
  for j in range(M) :
    if j == 0 :
      ... # надо дописать кусок кода
for i in range(N) :
  for j in range(M) :
    if j != M-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])

#lab 19, task 5
from random import randint
N = int(input("Введите к-во строк "))
k = 1
Sum = 0
SumD = []
A = []
for i in range(N) :
  A.append([])
  for j in range(N) :
    A[i].append(randint(1, 10))
for i in range(N) :
  for j in range(N) :
    if j != N-1 :
      print(A[i][j],"\t",end = "")
    else :
      print(A[i][j])
print("\n")
while k != N :
  for i in range(N) :
    for j in range(N) :
      if j == i-k :
        Sum += A[i][j]
  SumD.append(Sum)
  Sum = 0
  k += 1
k = 1
while k != N :
  for i in range(N) :
    for j in range(N) :
      if j == i+k :
        Sum += A[i][j]
  SumD.append(Sum)
  Sum = 0
  k += 1  
print(SumD)
