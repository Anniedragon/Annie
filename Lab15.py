#lab 15, task 1 
A = []
B = []
temp = 0
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
  B.append(int(input("Введите элемент списка В ")))
for i in range(N) :
  temp = A[i]
  A[i] = B[i]
  B[i] = temp
print(A)
print(B)

#lab 15, task 2 In progress
A = []
B = []
sum = 0
k = 1
N = int(input("Введите к-во элементов списка "))
for i in range(N) :
  A.append(int(input("Введите элемент списка А ")))
for i in range(N) :
  for k in range(1, i+1) :
    sum += k
  B[i] = sum / (k)
print(B)
