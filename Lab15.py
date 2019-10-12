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
