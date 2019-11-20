#lab 17, task 1
A = []
B = []
C = []
k = 1
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
A.append(0)
N += 1
for i in range(N-1) :
  if A[i] == A[i+1] :
    k += 1
  else :
    B.append(A[i])
    C.append(k)
    k = 1
print(B)
print(C)

#lab 17, task 2
A = []
A1 = []
k = 1
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
L = int(input("Введите длину серии "))
A.append(0)
N += 1
for i in range(N-1) :
  if A[i] == A[i+1] :
    k += 1
  else :
    if k == 1 :
      A1.append(A[i])
    elif k > L :
      A1.append(0)
      k = 1
    else :
      A1.append(A[i])
      k = 1
print(A1)

#lab 17, task 3
A = []
A1 = []
DlinyS = []
ElementS = []
Extra = []
k = 1
N = int(input("Введите к-во элементов "))
for i in range(N) :
  A.append(int(input("Введите элемент ")))
K = int(input("Введите номер серии(нумерация серий идёт с 0). Не вводите номер последней серии "))
A.append(0)
N += 1
for i in range(N-1) :
  if A[i] == A[i+1] :
    k += 1
  else :
    ElementS.append(A[i])
    DlinyS.append(k)
    k = 1
for i in range(len(DlinyS)-1) :
  if i != K :
    for j in range(DlinyS[i]) :
      A1.append(ElementS[i])
  else :
    for j in range(DlinyS[len(DlinyS)-1]) :
      A1.append(ElementS[len(DlinyS)-1])
    for j in range(DlinyS[K]) :
      Extra.append(ElementS[K])
A1.extend(Extra)
print(A1)

#lab 17, task 4
A = []
Mn = []
Mx = []
k = 1
flag = 0
flag1 = 0
N = int(input("Введите к-во точек "))
for i in range(N) :
  print("Точка",k)
  A.append(int(input("Введите координату Х точки ")))
  A.append(int(input("Введите координату Y точки ")))
  k += 1
for i in range(N*2-1) :
  if (i % 2 == 0) or (i == 0) :
    flag = 0
  else :
    flag = 1
  if flag == 0 :
    if (A[i] < 0) and (A[i+1] > 0) :
      flag1 = 1
      Mn.append(A[i])
      Mx.append(A[i+1])
if flag1 == 0 :
  print("Точка (0;0)")
Min = Mn[0]
Max = Mx[0]
for i in Mn :
  if i < Min :
    Min = i
for i in Mx :
  if i > Max :
    Max = i
print("Точка (",Min,";",Max,")")

#lab 17, task 5
from random import randint
from math import sqrt
A = []
X = []
Y = []
S1 = 0
S2 = 0
S3 = 0
P = 0
N = int(input("Введите общее к-во координат(чётное) "))
for i in range(N) :
  A.append(randint(-10, 10))
print(A)
for i in range(N) :
  if (i % 2 == 0) or (i == 0) :
    X.append(A[i])
  else :
    Y.append(A[i])
Xmax1 = X[0]
Xmax2 = X[1]
Xmax3 = X[2]
Ymax1 = Y[0]
Ymax2 = Y[1]
Ymax3 = Y[2]
for i in range(len(X)-1) :
  if X[i] > Xmax1 :
    Xmax1 = X[i]
for i in range(len(X)-1) :
  if (X[i] > Xmax2) and (X[i] != Xmax1) :
    Xmax2 = X[i]
for i in range(len(X)-1) :
  if (X[i] > Xmax3) and (X[i] != Xmax2) and (X[i] != Xmax1) :
    Xmax3 = X[i]
for i in range(len(X)-1) :
  if Y[i] > Ymax1 :
    Ymax1 = Y[i]
for i in range(len(X)-1) :
  if (Y[i] > Ymax2) and (Y[i] != Ymax1) :
    Ymax2 = Y[i]
for i in range(len(X)-1) :
  if (Y[i] > Ymax3) and (Y[i] != Ymax2) and (Y[i] != Ymax1) :
    Ymax3 = Y[i]
S1 = sqrt((Xmax2-Xmax1)**2 + (Ymax2-Ymax1)**2)
S2 = sqrt((Xmax3-Xmax2)**2 + (Ymax3-Ymax2)**2)
S3 = sqrt((Xmax3-Xmax1)**2 + (Ymax3-Ymax1)**2)
P = S1 + S2 + S3
print("Периметр треугольника равен",P) 
