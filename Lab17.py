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
